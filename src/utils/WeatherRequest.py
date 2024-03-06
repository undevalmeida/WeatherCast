import requests
import config
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



tempo = WeatherRequest(config.link)
previsao = tempo.get()
#print(previsao['data']['date'])
#print(previsao)
print(f"Data: {previsao['data'][0]['date_br']}", f"Probabilidade de Chuva: {previsao['data'][0]['rain']['probability']}", f"Temperatura:{previsao['data'][0]['temperature']}", f"Texto: {previsao['data'][0]['text_icon']['text']['pt']}")
#print(json.dumps(previsao, indent=4, ensure_ascii=False))

