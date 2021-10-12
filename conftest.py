import pytest
from scraper import *
from database import *

@pytest.fixture
def page_request():
    request = requests.get(URL)
    return request

@pytest.fixture
def page_html(page_request):
    bs = BeautifulSoup(page_request.content, 'html.parser')
    return bs
    
@pytest.fixture
def conn_to_db():
    con = sqlite3.connect('scrapeymcscraperton.db')
    cur = con.cursor()
    return cur
