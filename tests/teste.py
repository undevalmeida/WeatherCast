import requests
import json
import src.utils.config as config

simao_dias = config.simao_dias
api_key = config.API_KEY
link = f"http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{simao_dias}/hours/72?token={api_key}"
link2 = f"http://apiadvisor.climatempo.com.br/api/v1/locale/city?state=SE&token={api_key}"
link3 = f"http://apiadvisor.climatempo.com.br/api-manager/user-token/{api_key}/locales"
link4 = f"http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{simao_dias}/days/15?token={api_key}"


request_url = requests.get(link4)
print(request_url.status_code)

print(json.dumps(request_url.json(), indent=4, ensure_ascii=False))