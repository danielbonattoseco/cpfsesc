import requests
# Parâmetros (com @select codificado)
params = {
}

# Headers com User-Agent realista
headers = {
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

# Requisição
response = requests.get('http://www.ipeadata.gov.br/api/odata4/Territorios', headers=headers, params=params)

# Resultado
if response.status_code == 200:
    dados2 = response.json()
else:
    print(f"Erro {response.status_code}")

