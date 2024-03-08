import requests
from src.utils.config_api.config import link
import json

class WeatherRequest:
    """ Classe que ficará responsável pelas requisições das previsões do tempo no período de 15 dias"""
    def __init__(self, link):
        self.link = link

    def get(self):
        """ Método para fazer solicitação da API"""
        request = requests.get(self.link)
        if request.status_code == 200:
            return request.json()
        return print("Erro ao fazer requisição", request.status_code)




tempo = WeatherRequest(link)
previsao = tempo.get()

def three_days_forecast():
    """Retorna três próximos dias """


temperatura = previsao['data'][1]['temperature']
data = previsao['data'][1]

print(f"Data: {previsao['data'][1]['date_br']}", f"\nProbabilidade de Chuva: {previsao['data'][1]['rain']['probability']}%", f"\nTemperatura: Minima - {temperatura['min']}Cº Máxima - {temperatura['max']}Cº")
print("-" * 10)
print(json.dumps(previsao, indent=4, ensure_ascii=False))

