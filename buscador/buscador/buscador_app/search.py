import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser


class LinkParser(HTMLParser):

    def error(self, message):
        pass

    def __init__(self, output_list=None):
        HTMLParser.__init__(self)
        if output_list is None:
            self.output_list = []
        else:
            self.output_list = output_list

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.output_list.append(dict(attrs).get('href'))

    def get_output_list(self):
        list = []
        for url in self.output_list:
            if url == "#" or url[0] != "h":
                pass
            else:
                list.append(url)

        return list;


def main():
    url = "https://duckduckgo.com/?q=beautiful+soup+python&atb=v163-5_p&ia=web"


def add_to_list(response, url_list):
    url_data = {
        "url": response.url,

    }
    pass


def search(keyword, url, depth,url_list = []):
    response = requests.get(url)
    if has_keyword(keyword,response):
        add_to_list(response,url_list)
    links = get_all_links(response)


def get_all_links(response):
    parser = LinkParser()
    parser.feed(response.text)
    return parser.get_output_list()

def has_keyword(keyword,response):
    return keyword in response.text

if __name__ == '__main__':
    main()