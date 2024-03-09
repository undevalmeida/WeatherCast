import requests
from src.utils.config_api.config import link
import json

class WeatherRequest:
    """ Classe que ficará responsável pelas requisições das previsões do tempo no período de 15 dias"""
    def __init__(self, link):
        """
        Inicializa a instância da classe WeatherRequest.
        Args:
            link (str): O link para a API de previsão do tempo.
        """
        self.link = link

    @property
    def three_days_forecast(self):
        """
        Obtém a previsão do tempo para os próximos três dias.

        Este método faz uma solicitação à API de previsão do tempo e imprime as informações de previsão para os próximos três dias,
        incluindo a data, a probabilidade de chuva e a temperatura mínima e máxima.

        Returns:
            None. As informações de previsão são impressas na saída padrão.
        """
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