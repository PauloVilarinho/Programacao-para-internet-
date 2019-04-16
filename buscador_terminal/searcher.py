from bs4 import BeautifulSoup
import requests
import requests_cache

requests_cache.install_cache('Search_Cache')


class Searcher:

    def __init__(self, keyword, url, layers):
        self.keyword = keyword
        self.url = url
        self.layers = layers
        self.list = []
        self.search(url, layers)
        self.list.sort(key=lambda x: x['score'],reverse=True)

    def feed(self, keyword, url, layers):
        self.keyword = keyword
        self.url = url
        self.layers = layers
        self.list = []
        self.search(url, layers)
        self.list.sort(key=lambda x: x['score'],reverse=True)

    def search(self, url, layers):
        if self.url_in_list(url):
            self.add_to_list(url)
        elif self.keyword_in_url(url):
            self.add_to_list(url)
        if layers != 0:
            for links in self.get_all_links(url):
                self.search(links, layers - 1)

    def get_url_response(self, url):
        return requests.get(url)

    def get_all_links(self, url):
        response = self.get_url_response(url)
        html_text = response.text
        soup = BeautifulSoup(html_text, 'lxml')
        anchors = soup.find_all('a')
        links = []
        for anchor in anchors:
            if 'href' in anchor.attrs:
                if anchor['href'][0:2] == 'ht':
                    links.append(anchor['href'])
        return links[0:5]

    def keyword_in_url(self, url):
        response = self.get_url_response(url)
        html_text = response.text
        html_content = BeautifulSoup(html_text.lower(), 'lxml').find_all(text=True)
        result = True
        for x in self.keyword.lower().split():
            if x not in " ".join(html_content):
                result = False
                break
            result = True
        return result

    def get_description(self, url):
        html_text = self.get_url_response(url).text
        metas = BeautifulSoup(html_text.lower(), 'lxml').find_all('meta')
        for meta in metas:
            if 'name' in meta.attrs:
                if meta.attrs['name'] == 'description':
                    if meta.attrs['content'] is not None:
                        return meta.attrs['content']

        return "não tem descrição"

    def get_sentence(self,url):
        response = self.get_url_response(url)
        html_text = response.text
        html_content = BeautifulSoup(html_text.lower(), 'lxml').find_all(text=True)
        text = " ".join(html_content)
        word = self.keyword.lower().split()[0]
        position = text.find(word)
        return text[position-20:20+position]

    def add_to_list(self, url):

        if self.url_in_list(url):
            self.list[self.get_url_position(url)]["score"] += 1
        else:
            url_data = {
                "url": url,
                "description": self.get_description(url),
                "sentence": self.get_sentence(url),
                "score": 1,
            }
            self.list.append(url_data)

    def url_in_list(self, url):
        for url_data in self.list:
            if url_data["url"] == url:
                return True
        return False

    def get_url_position(self, url):
        aux = 0
        for url_data in self.list:
            if url_data["url"] == url:
                return aux
            aux += 1
        return None


if __name__ == '__main__':
    searcher = Searcher('charmander', 'https://www.pokemon.com/br/', 2)
    print(searcher.list)
