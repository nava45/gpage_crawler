from webkit_browser import Browser
from pyvirtualdisplay import Display
from lxml import html
import sys

def scrap(url):
    try:
        reload(sys)
        sys.setdefaultencoding('utf-8')
        
        display = Display(visible=0, size=(800, 600))
        display.start()

        b = Browser()
        b.open(url)
        content = b.main_frame['content'].read()
        #print "=====Crawled====="
        #print content
        #dom = html.fromstring(content)
        b.close()
        display.stop()
        del b
        return str(content)
    except Exception as e:
        print "===Scrapping Exception====="
        print str(e)
        b.close()
        display.stop()

if __name__ == '__main__':
    default_url = "http://google.com/search?q=gridlex$start=40"
    scrap(default_url)
