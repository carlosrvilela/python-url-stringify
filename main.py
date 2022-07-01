from extrator_url import ExtratorUrl


url = "  https://apibank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100 "
extrator_url = ExtratorUrl(url)
# print (extrator_url.url)
# print(extrator_url.get_url_base())
# print(extrator_url.get_url_parametros())
valor_quantidade = extrator_url.get_valor_parametro('moedaOrigem')
print (valor_quantidade)
print(len(extrator_url))
print(extrator_url)

extrator_url2 = ExtratorUrl(url)
print(extrator_url == extrator_url2)