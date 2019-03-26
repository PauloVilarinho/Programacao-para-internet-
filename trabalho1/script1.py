import requests


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
    print("status code:" ,response.status_code)
    print("cabeçalhos: " + response.headers['content-type'])
    print("tamanho da resposta:" , len(response.text))
    print("resposta: " + response.text )


if __name__ == '__main__':
    main()
