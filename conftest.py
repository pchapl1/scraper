import pytest
from scraper import *

@pytest.fixture
def page_request():
    request = requests.get(URL)
    return request

@pytest.fixture
def page_html(page_request):
    bs = BeautifulSoup(page_request.content, 'html.parser')
    return bs