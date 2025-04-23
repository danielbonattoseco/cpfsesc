import requests
from xml.dom.minidom import parseString

# Define os parâmetros da requisição
params = {
    'siglaPartido': 'PT',  # Substitua 'PT' pela sigla do partido desejado
    'ordem': 'ASC',
    'ordenarPor': 'nome'
}

# Define os headers da requisição
headers = {
    'Accept': 'application/xml'
}

# Faz a requisição GET para o endpoint de deputados
response = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados', params=params, headers=headers)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    if headers['Accept'] == 'application/json':
        # Converte a resposta para JSON
        dados = response.json()
        # Itera sobre os dados dos deputados retornados
        for deputado in dados['dados']:
            print(f"{deputado['nome']} ({deputado['siglaPartido']}) - {deputado['siglaUf']}")
    elif headers['Accept'] == 'application/xml':
        raw_xml = response.text
        parsed_xml = parseString(raw_xml)
        pretty_xml = parsed_xml.toprettyxml(indent="  ")
else:
    print(f"Erro na requisição: {response.status_code}")
    
a = response.text
