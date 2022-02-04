from csv import DictReader
from buscar_docs import *


class Ritmista:
    def __init__(self, nome, genero, instrumento, doc, num_doc, arquivo_doc, nusp, comprovante):
        self.nome = nome
        self.genero = genero
        self.instrumento = instrumento
        self.doc = doc
        self.num_doc = num_doc
        self.arquivo_doc = arquivo_doc
        self.nusp = nusp
        self.comprovante = comprovante
        self.faculdade = 'USP'
        self.curso = 'Farmácia e Bioquímica'


def ler_dados():
    print('Lendo dados do formulário...')
    with open('/home/jovi/PycharmProjects/credenciamento/Credenciamento TABU (respostas).csv') as arquivo:
        leitor = DictReader(arquivo)
        lista = list()

        for linha in leitor:
            nome = linha['Nome Completo'].title()
            genero = linha['Gênero'][0]

            if linha['Instrumento'] in ('Terceira', 'Primeira', 'Segunda'):
                instrumento = 'Surdo'
            elif linha['Instrumento'] == 'Agogô':
                instrumento = 'Agogo'
            elif linha['Instrumento'] == 'Xequerê':
                instrumento = 'Chocalho'
            elif linha['Instrumento'] == 'Repique':
                instrumento = 'Repinique'
            else:
                instrumento = linha['Instrumento']

            doc = linha['Qual documento será usado? Lembrando que ele será o apresentado no dia do torneio'].strip()

            if '.' and '-' in linha['Número do documento']:
                linha['Número do documento'] = linha['Número do documento'].replace('.', '')
                linha['Número do documento'] = linha['Número do documento'].replace('-', '')
            num_doc = linha['Número do documento']

            arquivo_doc = nome.split()[:2]
            arquivo_doc = ''.join(arquivo_doc).lower()
            arquivo_doc = buscar_doc(arquivo_doc, 'DOC')
            if arquivo_doc == 'Arquivo não encontrado\n':
                arquivo_doc = nome.split()[0]
                arquivo_doc = ''.join(arquivo_doc).lower()
                arquivo_doc = buscar_doc(arquivo_doc, 'DOC')
            print(arquivo_doc)

            nusp = linha['Número USP']

            comprovante = nome.split()[:2]
            comprovante = ''.join(comprovante).lower()
            comprovante = buscar_doc(comprovante, 'COMP')
            if comprovante == 'Arquivo não encontrado\n':
                comprovante = nome.split()[0]
                comprovante = ''.join(comprovante).lower()
                comprovante = buscar_doc(comprovante, 'COMP')
            print(comprovante)

            pessoa = Ritmista(nome, genero, instrumento, doc, num_doc, arquivo_doc, nusp, comprovante)
            lista.append(pessoa)
        print(f'Dados de {len(lista)} ritmistas extraídos do formulário com sucesso!\n')
        return lista


if __name__ == '__main__':
    ler_dados()
