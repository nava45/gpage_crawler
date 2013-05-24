import sys
import os
import subprocess
from lib.BeautifulSoup import BeautifulSoup

#Optinal Crawler module for Google search results
def exe_cmd(url):
    path = os.getcwd()
    cmd = "xvfb-run python /work/ws/hg_intcen/lib/webpage_scrapper.py"+" "+str(url)
    proc = subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    proc.wait()
    sys.stdout.flush()
    result = proc.stdout.readlines()
    return result


#Fetch sidebar ads from google search results
def get_sidebar_ads(html_data):
    """
    Code to fetch ads also
    """
    return []


#Get center ads from Google search results
def get_center_ads(html_data):
    """
    Center ads in search results page
    """
    return []


#Get Organic Contents from Google search results
def get_organic_data(html_data):
    bs = BeautifulSoup(str(html_data))
    div_filter = bs.find('div',{'id':'ires'})
    if div_filter:
        contents = div_filter.findAll('li',{'class':'g'})
        return contents
    return None


def crawl_refiner(url):
    from web_scrap import scrap

    #Crawl
    html_string = scrap(url)
      

    html_ad = get_sidebar_ads(html_string)
    html_center_ad = get_center_ads(html_string)
    html_content = get_organic_data(html_string)

    return {"sidebar_ads":html_ad,"center_ad":html_center_ad,"organic_content":html_content}
