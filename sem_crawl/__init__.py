from webpage_parser import main

import sys

def gsearch(url):
    return main(url)
    
if __name__ == '__main__':
    res = None
    if len(sys.argv) == 2:
        url = sys.argv[1]
        res = gsearch(url)
    else:
        print "usgae: python __init__.py http://www.google.ca/search?q=navaspot"

    print res
