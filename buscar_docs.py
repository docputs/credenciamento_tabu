import os


def buscar_doc(nome, tipo):
    print(f'\033[1;33mBuscando documento...\033[m')

    nome = nome.split()
    nome = ''.join(nome)
    print(f'buscando {nome}')

    if not os.getcwd() == '/home/jovi/PycharmProjects/credenciamento/credenciamento-tabu-arquivos/arquivos_documentos':
        os.chdir('arquivos_documentos')
    arquivos = os.listdir('.')

    for arquivo in arquivos:
        if nome in arquivo:
            if tipo == 'DOC':
                if 'DOC' in arquivo:
                    return arquivo[:-5]
            elif tipo == 'COMP':
                if 'COMP' in arquivo:
                    return arquivo[:-5]

    return 'Arquivo não encontrado\n'

