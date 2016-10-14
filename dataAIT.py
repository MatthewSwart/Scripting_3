#BeautifulSoup: Parsing data from AIT timetable website.

'''
    Libraries:
        urlLib:
            Documentation: https://docs.python.org/2/library/urllib.html
        bs4:
            Download: https://www.crummy.com/software/BeautifulSoup/
            Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
'''
import urllib
from bs4 import BeautifulSoup
'''
    Set the url for the website you require the code of.
'''
url = ("http://timetable.ait.ie/reporting/individual;student+set;id;AL_KNTWM_7_3%0D%0A?t=student+set+individual&days=1-5&weeks=&periods=3-20&template=student+set+individual")
'''
    html:
        open the url using urllib
    page:
        Parse the page using BeautifulSoup.
'''
html = urllib.urlopen(url).read()
page = BeautifulSoup(html, "html.parser")
'''
    For lines in page:
       This section prints out all the HTML code that was requested by bs4 earlier.
'''
for lines in page:
    print lines