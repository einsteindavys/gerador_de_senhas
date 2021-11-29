import random
import PySimpleGUI as tema
import os


class GerarSenha:
    def __init__(self):
# Layout do popup
        tema.theme('Default')
        layout = [
            [tema.Text('Site', size=(10, 1)),tema.Input(key='site', size=(20, 1))],
            [tema.Text('Login', size=(10, 1)),tema.Input(key='login', size=(20, 1))],
            [tema.Text('Qual o Tamanho da senha:'), tema.Combo(values=list(range(31)), key='total_chars', default_value=6, size=(3, 1))],
            [tema.Output(size=(32, 5))],
            [tema.Button('Gerar Senha')]
        ]
# Atributos do popup
        self.janela = tema.Window('Gerador de Senhas', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == tema.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)

    def gerar_senha(self, valores):
        char_list = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%¨&*()_+-=[],.;<>:^}{'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(
                f"\nsite: {valores['site']}, login: {valores['login']}, nova senha: {nova_senha}")

        print('Arquivo salvo')


gerador = GerarSenha()
gerador.Iniciar()
