try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
    
from bs4 import BeautifulSoup

url = urllib2.urlopen( 'http://www.csc.ncsu.edu/faculty/healey/msa-17/python/index.html' )
doc = url.read()
tree = BeautifulSoup( doc )

div = tree.find( 'div', { 'class': 'footer' } )
div

span = div.find( 'span', { 'id': 'mod-date' } )
span

span.getText()
