import requests
import shutil




def main():
    url = receive_url()
    path, response = get_url_data(url)
    download_data(path, response)


def receive_url():
    url = input("Digite a url a ser pesquisada.")
    return url


def get_url_data(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        path = input("qual vai ser o nome do arquivo: ")
    return path, response


def download_data(path,response):
    with open("fotos_script2/" + path+".jpg", 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)


if __name__ == '__main__':
    main()