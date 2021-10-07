from scraper import *
from pathlib import Path

def test_html_source_exists(page_html):
    assert page_html != None


def test_question_summary_exists(page_html):
    class_divs = page_html.findAll('div', {'class' : 'question-summary'})
    assert len(class_divs) > 0


def test_file_path_valid():
	path_to_file = "stack_overflow.csv"
	path = Path(path_to_file)
	assert path.is_file()


def test_write_to_file():
    with open('stack_overflow.csv', 'r') as f:
        count = 0
        for row in f:
            count +=1
    assert count > 0