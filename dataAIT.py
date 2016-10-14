#
import urllib
from bs4 import BeautifulSoup

url = ("http://timetable.ait.ie/reporting/individual;student+set;id;AL_KNTWM_7_3%0D%0A?t=student+set+individual&days=1-5&weeks=&periods=3-20&template=student+set+individual")

html = urllib.urlopen(url).read()
page = BeautifulSoup(html, "html.parser")

for lines in page:
    print lines