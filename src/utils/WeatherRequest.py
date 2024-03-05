import requests
from config_api.config import link
from datetime import datetime


class WeatherRequest:
    """ Classe que ficará responsável pelas requisições das previsões do tempo """

    def __init__(self, link):
        self.link = link

    def get_temperatura(self):
        """ Método para fazer solicitação da API sobre a temperatura em celsius"""
        request = requests.get(self.link)
        if request.status_code == 200:
            return request.json()
        return print("Erro ao fazer requisição", request.status_code)


tempo = WeatherRequest(link)
json_data = tempo.get_temperatura()
local = json_data['name']
descricao = json_data['weather'][0]['description'].capitalize()
temperatura = json_data['main']['temp']
sensacao = json_data['main']['feels_like']
umidade = json_data['main']['humidity']
data = json_data['dt']
# ainda esturando a api advisor api clima tempo, quero trazer previsões
print(f"Local: {local}\nData: {datetime.utcfromtimestamp(data).date()}\nDescrição: {descricao}\nTemperatura: {temperatura - 273.15:.2f}ºC\nSensação Térmica: {sensacao - 273.15:.2f}\nUmidade: {umidade}")