import PySimpleGUI as sg # Importa a biblioteca de interface gráfica
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED,WIN_CLOSED, Window #Importa os métodos da classe "PySimpleGUI"
from Contrato import * # Importa a classe "Contrato"

class Sistema_contratos: # Define a classe "Sistema de contratos"
    
    def __janela_cadastro(self): # Função que retorna a janela de cadastro
        layout = [
        [sg.Text('Código do banco:',  justification='left'),sg.InputText(key='codigo-banco')], 
        [sg.Text('Valor do contrato:', justification='left'), sg.InputText(key='valor')], 
        [sg.Button('Salvar'), sg.Button('Cancelar'), sg.Button('Exibir contratos')]
    ]

        return sg.Window(title='Contratos', layout=layout)
    

    def __janela_contratos(self, lista): # Função que retorna a janela com a lista dos contratos
        headers = ['COD','Banco', 'Valor', 'Data do registro']
        layout = [
            [sg.Table( headings=headers,values=lista, justification='center', size=(65, len(lista)), auto_size_columns=False)], [sg.Button('Sair')]
        ]

        return sg.Window(title='Janela contratos',layout=layout )


    def window_init(self): # Função que administra a dinãmica das janelas
        window = self.__janela_cadastro() # Atribui a variável "window" à função "__janela_cadastro"

        while True: # Looping da primeira janela
            event, values = window.read() # Verifica os eventos ocorridos na janela e recolhe os valores digitados

            if event == 'Cancelar' or event == WINDOW_CLOSED: # Verifica o se a janela foi fechada
                break

            elif event == 'Salvar': # Verifica se o botão "Salvar foi clicado"
                try:
                    contato = Contrato(values['codigo-banco'], values['valor']) # Cria um objeto do tipo "Contrato"
                except Exception as E: # Trata os erros
                    sg.popup(E) # Mostra um popup com a mensagem de erro
                    continue
                else:
                    with open('arquivo.csv', mode='a', encoding='UTF-8') as arquivo: # Abre o arquivo
                        arquivo.write(contato.contrato) # Escreve os dados no arquivo
                
                sg.popup('Contrato salvo !') # Exibe um popup com a mensagem "Contrato salvo!"

            elif event == 'Exibir contratos': # Verifica se o botão "Exibir contratos" foi clicado
        
                with open('arquivo.csv', mode='r', encoding='UTF-8') as arquivo: # Abre o arquivo
                    window2 = self.__janela_contratos(arquivo.readlines()) # Atribui a lista de contratos à janela 2
                        
                while True: # Looping da segunda janela
                    e ,v = window2.read() # leitura da segunda janela

                    if e == 'Sair' or e == WIN_CLOSED: # Verifica se a janela foi fechada
                        break

                window2.close() # Fecha a segunda janela

        window.close() # Fecha a primeira janela

if __name__ == '__main__': # Verifica se o contexto de execução está no contexto global
    sistema = Sistema_contratos() # Cria um objeto do tipo "Sistema_contratos"
    sistema.window_init() # Inicializa o programa
