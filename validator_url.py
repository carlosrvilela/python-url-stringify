# Exemplos de URLs válidas:

urls_validas = [
    'apibank.com/cambio ',
    'apibank.com.br/cambio',
    'www.apibank.com/cambio',
    'www.apibank.com.br/cambio',
    'http://www.apibank.com/cambio',
    'http://www.apibank.com.br/cambio',
    'https://www.apibank.com/cambio',
    'https://www.apibank.com.br/cambio']

# Exemplos de URLs inválidas:

urls_invalidas = [
    'https://apibank/cambio',
    'https://apibank.naoexiste/cambio',
    'ht://apibank.naoexiste/cambio']

import re
urls = urls_validas+urls_invalidas
padrao_url = re.compile('(http(s)?://)?(www.)?apibank.com(.br)?/cambio')
for url in urls:
    match = padrao_url.match(url)
    if match:
        print(f'{url} é valida' )
    else:
        print(f'{url} não é valida')