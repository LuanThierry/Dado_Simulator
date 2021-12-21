# iremos simular o dado, mostrando o valor do 1 a o 6 que é o tanto de lado que o dado tem
# biblioteca que gera valores aleatorios
import random
# criador de interfaces do python
import PySimpleGUI as sg

sg.popup('Bem vindo ao Simulador de Dados Virtual')


class DadoSimulator:
    # definindo as configuraçõrs iniciais
    def __init__(self):
        # nos precisamos do valor inicial
        self.valor_min = 1
        self.valor_max = 6
        # vamos criar um layout e dps uma janela pra ler os valores da tela e dps fzr... com os valores
        self.layout = [
            [sg.Text('Deseja rolar o Dado?')],
            [sg.Button('sim', size=(40, 1)),
             sg.Button('não', size=(12, 1))]
        ]
        # inicio de verdade, sem precisar configurar o atributo or serve para gerar novas possibilidades de comandos em sequencia de sua variavel

    def Iniciar(self):
        # criação da janela
        self.janela = sg.Window('Dado Simulator', layout=self.layout)
        # ler os eventos da janela
        self.eventos, self.valores = self.janela.Read()
        # temos que tratar a excessao de respostas usando o try
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.DadoValor()
            # possibilidades de respostas
            elif self.eventos == 'não' or self.eventos == 'n':
                sg.popup('Bye')
            else:
                sg.popup('Digite apenas sim ou não')
        except:
            sg.popup(
                'Sua resposta não é válida, por favor reinicie e tente novamente')
    # imprimindo o valor do dado jogado

    def DadoValor(self):
        sg.popup(random.randint(self.valor_min, self.valor_max))


simulator = DadoSimulator()
simulator.Iniciar()
