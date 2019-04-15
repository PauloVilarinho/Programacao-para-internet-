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
