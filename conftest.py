import pytest
from selenium import webdriver

lang_access = ['ar', 'ca', 'ru', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi', 'fr', 'it', 'ko', 'nl', 'pl', 'pt',
               'pt-br', 'ro', 'sk', 'uk', 'zh-cn']


@pytest.fixture(scope='function')
def language(request):
    lang = request.config.getoption('language')
    if lang in lang_access:
        yield lang
    else:
        raise pytest.UsageError("--language not available, please choose language from this list: ar, ca, ru, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, sk, uk, zh-cn")


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose site language")


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser')
    browser.close()