import datetime # Importa a biblioteca datetime

class Contrato: # Define a classe Contrato
    def __init__(self, cod_banco, valor):
        self.__banco = self.__get_banco(cod_banco)
        self.__valor = self.__formata_valor(valor)
        self.__data = self.__get_data()
        self.__contrato = f'{self.__banco} {self.__valor} {self.__data}\n'

    
    def __get_data(self): # Método que retorna a data formatada
        return datetime.date.today().strftime('%d/%m/%y')
    

    def __formata_valor(self, valor): # Retorna  valor formatado
        return f'R${float(valor):.2f}'
    

    def __get_banco(self, cod_banco):# Retorna código mais o seu respectivo banco
        lista_bancos = {'Caixa':'1', 'Santander': '2', 'Itaú': '3', 'BB': '4', 'Safra': '5'} # Dicionário com os bancos
        for k,v in lista_bancos.items():
            if v == cod_banco: # Verfica se o código está na lista
                return f'{v} {k}'
            elif cod_banco not in lista_bancos.values(): # Se não estiver retorna um erro
                raise ValueError('Código inválido')
               

    @property # Getter do contrato
    def contrato(self):
        return self.__contrato