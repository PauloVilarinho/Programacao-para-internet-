import requests
from html.parser import HTMLParser

def main():
    url = receive_url()
    response = get_url_data(url)
    print_data(response)


def receive_url():
    url = input("Digite a url a ser pesquisada.")
    return url


def get_url_data(url):
    response = requests.get(url)
    return response


def print_data(response):
    html_body = response.text
    parser = MyParser()
    parser.feed(html_body)
    print(parser.output_list)



class MyParser(HTMLParser):
    def __init__(self, output_list=None):
        HTMLParser.__init__(self)
        if output_list is None:
            self.output_list = []
        else:
            self.output_list = output_list
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.output_list.append(dict(attrs).get('href'))


if __name__ == '__main__':
    main()
