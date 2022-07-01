import re

from matplotlib.pyplot import get
class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanetiza_url(url)
        self.valida_url()
        
    def __len__(self):
        return len(self.url)
        
    def sanetiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
            
    def valida_url(self):
        if not self.url:
            raise ValueError('URL Vazia')
        
        padrao_url = re.compile('(http(s)?://)?(www.)?apibank.com(.br)?/cambio')
        if not padrao_url.match(self.url):
            raise ValueError('A URL não é válida')
        
        
    def get_url_base(self):
        indice_quebra = self.url.find('?')
        return self.url[:indice_quebra]
    
    def get_url_parametros(self):
        indice_quebra = self.url.find('?')
        return self.url[indice_quebra+1:]
    
    def get_valor_parametro(self, nome_parametro):
        url_parametros = self.get_url_parametros()
        indice_parametro = url_parametros.find(nome_parametro)
        indice_valor = indice_parametro + len(nome_parametro) + 1
        indice_e_comercial = url_parametros.find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = url_parametros[indice_valor:]
        else:
            valor = url_parametros[indice_valor:indice_e_comercial]
        return valor
    
    def __str__(self):
        return self.url + '\nURL Base: ' + self.get_url_base() + '\nParâmetros: ' + self.get_url_parametros()
    
    def __eq__(self, other):
        return self.url == other.url