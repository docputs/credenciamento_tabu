from webbot import Browser
from time import sleep
from pynput.keyboard import Key, Controller


class Navegador:
    def __init__(self):
        print('Abrindo navegador...')
        self.site = Browser()
        self.contador = 0

    def logar(self, login, senha):
        print('Entrando em https://credenciamento.ligalnbu.com.br/')
        self.site.go_to('https://credenciamento.ligalnbu.com.br/')
        sleep(3)
        self.site.click('ENTRAR')
        print(f'Fazendo login como \033[34m{login}\033[m...')
        self.site.type(text=login, into='Email')
        self.site.type(text=senha, into='Senha')
        print('\033[1;33mLogin realizado com sucesso!\033[m')
        self.site.click('Entrar')
        sleep(3)
        self.site.click('CREDENCIAMENTO')
        sleep(3)

    def cadastrar_ritmista(self, ritmista):
        print(f'''\033[1;4;36m-> Cadastrando {ritmista.nome}\033[m:
        - Gênero: {ritmista.genero}
        - Instrumento: {ritmista.instrumento}
        - Documento: {ritmista.doc}
        - Nome do arquivo do documento: {ritmista.arquivo_doc}
        - Número do(a) {ritmista.doc}: {ritmista.num_doc}
        - Número USP: {ritmista.nusp}
        - Nome do arquivo do comprovante: {ritmista.comprovante}''')

        self.site.click('Criar registro de ritmista')
        self.site.type(ritmista.nome, xpath='//*[@id="licensingTable"]/form/div[3]/input[1]')

        print('\033[32m', end='')
        print('-' * 50)
        print('Preenchendo formulário de registro de ritmista')
        print('-' * 50)
        print('\033[m', end='')

        if ritmista.genero == 'M':
            self.site.click(xpath='//*[@id="licensingTable"]/form/div[3]/input[2]')
        elif ritmista.genero == 'F':
            self.site.click(xpath='//*[@id="licensingTable"]/form/div[3]/input[3]')
        else:
            self.site.click(xpath='//*[@id="licensingTable"]/form/div[3]/input[4]')

        self.site.click(id='selecionar-instrumento')
        self.site.click(text=ritmista.instrumento)

        if ritmista.doc == 'RG':
            self.site.click(xpath='//*[@id="licensingTable"]/form/div[3]/input[5]')
        elif ritmista.doc == 'CNH':
            self.site.click(xpath='//*[@id="licensingTable"]/form/div[3]/input[6]')
        else:
            self.site.click(xpath='//*[@id="licensingTable"]/form/div[3]/input[7]')

        self.site.type(ritmista.num_doc, xpath='//*[@id="licensingTable"]/form/div[3]/input[8]')

        self.site.driver.find_element_by_xpath('//*[@id="l_Up_Doc_File"]').click()
        selecionar_arquivo(nome_foto=ritmista.arquivo_doc, nome_pasta='arquivos_documentos', vez=self.contador)

        self.site.type(ritmista.faculdade, xpath='//*[@id="licensingTable"]/form/div[3]/input[10]')

        self.site.type(ritmista.curso, xpath='//*[@id="licensingTable"]/form/div[3]/input[11]')

        self.site.type(ritmista.nusp, xpath='//*[@id="licensingTable"]/form/div[3]/input[12]')

        self.site.driver.find_element_by_xpath('//*[@id="l_Up_Ra_File"]').click()
        selecionar_arquivo(nome_foto=ritmista.comprovante)

        self.site.click(xpath='//*[@id="licensingTable"]/form/div[3]/button')

        self.contador += 1

        print(f'\033[1;31m{ritmista.nome} cadastrado(a) com sucesso!\033[m\n')


def selecionar_arquivo(nome_foto, vez=1, nome_pasta=None):
    print(f'    Selecionando arquivo {nome_foto}...')
    teclado = Controller()

    if vez == 0:
        teclado.type('PycharmProjects')
        teclado.press(Key.enter)
        teclado.release(Key.enter)
        sleep(1)
        teclado.type('credenciamento')
        teclado.press(Key.enter)
        teclado.release(Key.enter)
        sleep(1)
        teclado.type('credenciamento-tabu-arquivos')
        teclado.press(Key.enter)
        teclado.release(Key.enter)
        sleep(1)
        teclado.type(nome_pasta)
        teclado.press(Key.enter)
        teclado.release(Key.enter)
        sleep(1)

    teclado.type(nome_foto)
    sleep(3)
    teclado.press(Key.enter)
    teclado.release(Key.enter)
    sleep(1)
