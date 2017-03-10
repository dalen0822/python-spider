from html_downloader import htmlDownloader
from url_manager import urlManager
from html_parser import htmlParser
from html_outputer import htmlOutputer


class spiderMain():
    def __init__(self):
        self.urls = urlManager()
        self.parser = htmlParser()
        self.downloader = htmlDownloader()
        self.outputer = htmlOutputer()

    def craw(self,url):
        self.urls.add_new_url(url)
        count = 0
        while self.urls.has_new_url():
            try:
                page_url = self.urls.get_new_url()
                html_cont = self.downloader.download(page_url)
                new_urls,new_data = self.parser.parse(page_url,html_cont)
                print "craw the %s url %s" % (count,page_url)
                print new_data
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count += 1
                if count == 8:
                    break
            except:
                print "fail"
        self.outputer.output_html()

if __name__ == '__main__':
    root_url = "http://baike.baidu.com/item/Python"

    obj_spider = spiderMain()
    obj_spider.craw(root_url)
