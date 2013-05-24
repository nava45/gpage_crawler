import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

import pickle

class Render(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()


def crawl(url):
    #url = 'http://www.google.ca/search?q=navaspot'
    r = Render(url)
    html = r.frame.toHtml()
    reload(sys)
    sys.setdefaultencoding('utf-8')
    return str(html)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "USAGE:python webpage_scrapper.py 'http://navaspot.wordpress.com'"
        sys.exit(0)
    url = sys.argv[1]
    print "URL 2 Crawl : ",url
    result = crawl(url)
    print result
    """
    DO NOT COMMENT THIS PRINT STATEMENT :: print result
    """
