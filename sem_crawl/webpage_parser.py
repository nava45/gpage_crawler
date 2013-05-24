import sys
import re
import urllib as ul
from lib.BeautifulSoup import BeautifulSoup
from lxml import etree
from lxml.html import fromstring
from webpage_splitter import crawl_refiner


p = re.compile(r'<.*?>')


def parse_display_url(tag):
    bs = BeautifulSoup(tag)
    display_url = bs.find('cite')
    dis_url = p.sub('',str(display_url))
    return str(dis_url)


def parse_organic_contents(raw_content,organic_pos):
    data_dict = {}
    data_dict['position'] = organic_pos

    b = BeautifulSoup(raw_content)
    rtitle = b.find('a')
    headline = p.sub('',str(rtitle))
    data_dict['title'] = headline

    display_url = parse_display_url(str(raw_content))
    data_dict['display_url'] = display_url

    rhref=b.find('a',href=True)
    url = str(rhref['href'])
    data_dict['url'] = ul.unquote(url)

    rtext=b.findAll('div',{'class':'s'})
    text=p.sub('',str(rtext))
    data_dict['text'] = text.replace(']','').replace('[','')
    return data_dict


def main(url):
    global overall_position
    overall_position = 0
    raw_dict = crawl_refiner(url)

    result_content = []

    organic_pos = 0
    for raw_content in raw_dict['organic_content']:
        organic_pos += 1
        parsed_content = parse_organic_contents(str(raw_content),organic_pos)
        result_content.append(parsed_content)
    
    #print "==================Parsed Content=======================\n"
    #print result_content
    """
    Parsed Content Output is a list result_content=[(Headline,URL,Text),(),()....]
    """

  
    return {"center_ad":[],"sidebar_ad":[],"contents":result_content}
