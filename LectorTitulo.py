from requests import Session
from bs4 import BeautifulSoup
import unicodedata


def remove_control_characters(s):
    return "".join(ch for ch in s.strip() if unicodedata.category(ch)[0] != "C")


def eur2str(eur_list):
    """
    Strip non-printable symbols from list of _ElementUnicodeResult and convert to list of string

    """
    str_list = []
    for x in range(len(eur_list)):
        value = eur_list[x].format('s').strip()
        if value != '':
            str_list.append(value)
    return str_list


class LectorTitulo:

    def __init__(self, url):
        self.url = url
        self.session = Session()

    def leer_titulo(self):
        links = ('h1', 'h2',)
        titulo = self.url.rstrip()
        try:
            r = self.session.get(self.url)
            if r.status_code == 200:
                r.raise_for_status()
            soup = BeautifulSoup(r.content, "lxml")
            for link in links:
                html_link = soup(link)
                if html_link:
                    try:
                        if html_link[0]['id'] == "unavailable-message":
                            titulo = remove_control_characters(html_link[1].contents[1].contents[0])
                    except KeyError as ex:
                        titulo = remove_control_characters(html_link[0].text)
        except Exception as ex:
            titulo = ex.__str__()
        return titulo
