from requests_html import HTMLSession


class LectorTitulo:

    def __init__(self, url):
        self.url = url
        self.session = HTMLSession()

    def leer_titulo(self):
        titulo = self.url
        try:
            r = self.session.get(self.url)
            if r.status_code == 200:
                html_element = r.html.find('h1', first=True)
                if html_element is not None:
                    titulo = html_element.text
        except Exception as ex:
            print(ex)
            titulo = ex.__str__()
        return titulo
