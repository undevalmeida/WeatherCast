import requests
from src.utils.config_api.config import link
import json

class WeatherRequest:
    """ Classe que ficará responsável pelas requisições das previsões do tempo no período de 15 dias"""
    def __init__(self, link):
        self.link = link

    @property
    def three_days_forecast(self):
        """ Método para fazer solicitação da API"""
        request = requests.get(self.link)
        if request.status_code == 200:
            previsao_tempo = request.json()

            for data in previsao_tempo['data'][:3]:
                print(f"Data: {data['date_br']}")
                print(f"Probabilidade de Chuva: {data['rain']['probability']}%")
                print(f"Temperatura: Minima - {data['temperature']['min']}Cº Máxima - {data['temperature']['max']}Cº")
                print("-="*20)
        return print("Erro ao fazer requisição", request.status_code)

weather_request = WeatherRequest(link)
weather_request.three_days_forecast