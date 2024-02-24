import requests
import config


requisicao = requests.get(config.link)
print(requisicao.json())

class WeatherRequest:
    """ Classe que ficará responsável pelas requisições das previsões do tempo """
    def __init__(self, link):
        self.link = link

    def get(self):
        """ Método para fazer solicitação da API"""
        request = requests.get(self.link)
        if request.status_code == 200:
            return request.json()
        return print("Erro ao fazer requisição", request.status_code)



tempo = WeatherRequest(config.link)
tempo.get()