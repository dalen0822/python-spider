# coding=utf-8
import sys


class htmlOutputer():
    cont_list = []
    sysCharType = sys.getfilesystemencoding()
    def collect_data(self,data):
        if data is None:
            return
        print data
        self.cont_list.append(data)

    def output_html(self):



        f = open('output.html','w')
        f.write('<html>')
        f.write('<meta charset="UTF-8">')
        f.write('<body>')
        f.write('<table>')
        for data in self.cont_list:
            f.write('<tr>')
            f.write('<td>%s</td>' % data['url'])
            f.write('<td>%s</td>' % data['title'])
            f.write('<td>%s</td>' % data['summary'])
            f.write('</tr>')

        f.write('</table>')
        f.write('</body>')
        f.write('</html>')
        f.close()
