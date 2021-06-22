import grequests  # for Async requests
from bs4 import BeautifulSoup
import validators
import urllib
import gevent  # For Async event execution
import logger
import os
import time

LOGGER = logger.get_logger(__name__)


def create_session():
    return grequests.Session()


def get_file_path(filename):
    filepath = os.path.abspath(os.path.join(
        os.path.dirname(__file__), f"temp/{filename}"))
    return filepath


def save_links_in_file(filepath, links):
    """
    Function save links into given file.
    """
    with open(filepath, 'a+', encoding="utf-8") as f:
        f.writelines(list("%s\n" % link for link in links))


def get_links_in_page(main_url, session, filepath):
    """
    Function find all the available and valid links in page.
    """
    main_page = session.get(main_url)
    main_page_html = BeautifulSoup(main_page.text, 'html.parser')
    links = [a['href'] for a in main_page_html.find_all(
        'a', href=True) if validators.url(a['href'])]
    save_links_in_file(filepath, links)
    return links


def get_hostname(url):
    """
    Function return hostname from any url.
    """
    parsed_url = urllib.parse.urlparse(url)
    return parsed_url.netloc


def crawl_domain(main_url):
    """
    Function crawls the given url and write extracted urls into file under temp/.
    """
    LOGGER.info("Crawler started")
    main_hostname = get_hostname(main_url)
    session = create_session()
    threads = list()
    filepath = get_file_path(f"extracted_links{int(time.time())}.txt")
    links = get_links_in_page(main_url, session, filepath)

    for link in links:
        if main_hostname == get_hostname(link):
            LOGGER.debug(f"Searching links for : {link}")
            threads.append(gevent.spawn(
                get_links_in_page, link, session, filepath))
    gevent.joinall(threads)

    LOGGER.info(f"Crawl links available in : PATH :: {filepath}")
    LOGGER.info("Crawler Stopped")


if __name__ == '__main__':
    domain = "https://news.ycombinator.com/"
    crawl_domain(domain)
