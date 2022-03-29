
from parsel import Selector
#from bs4 import BeautifulSoup

def templated_parse(template, page):
    page_ = Selector(page)
    return template.apply(page_)