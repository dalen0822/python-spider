# coding=utf-8
import re
import urlparse

import sys
from bs4 import BeautifulSoup


class htmlParser():
    def __init__(self):
        pass

    def get_soup_url(self,page_url,soup):
        new_urls = set()

        #/view/2323.html
        links = soup.find_all('a',href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def get_soup_data(self,page_url,soup):

        #<dd class="lemmaWgt-lemmaTitle-title">
        res_data = {}
        res_data['url'] = page_url

        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text().encode('utf-8')

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_='lemma-summary')
        res_data['summary'] = summary_node.get_text().encode('utf-8')
        #.decode(self.sysCharType).encode('utf-8')
        return res_data

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self.get_soup_url(page_url,soup)
        new_datas = self.get_soup_data(page_url,soup)
        return new_urls,new_datas
