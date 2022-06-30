from cmath import e
import re


class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanetiza_url(url)
        self.valida_url()
        
    def sanetiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
            
    def valida_url(self):
        if not self.url:
            raise ValueError('URL Vazia')
        
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