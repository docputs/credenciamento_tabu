import os
from shutil import move


def renomear(nome_atual_pasta):
    print(f'\033[1;33mRenomeando documentos...\033[m')

    try:
        os.rename(nome_atual_pasta, 'credenciamento-tabu-arquivos')
    except FileNotFoundError:
        print(f'    "{nome_atual_pasta}" já está renomeado.')
    else:
        print(f'    "{nome_atual_pasta}" renomeado com sucesso!')

    try:
        os.mkdir('credenciamento-tabu-arquivos/arquivos_documentos')
        print('     Pasta "arquivos_documentos" criada com sucesso!')
    except FileExistsError:
        print('     Pasta "arquivos_documentos" já existe.')

    print('\033[1;33mPronto!\033[m')
    print('\n')


def mover(path):
    print(f'\033[1;33mMovendo documentos...\033[m')

    os.chdir('credenciamento-tabu-arquivos')

    for diretorio in path:
        os.chdir(diretorio)
        pasta = os.listdir('.')
        print(f'\033[31mArquivos no diretório atual: {os.getcwd()}\033[m')

        for arquivo in pasta:
            novo_nome = arquivo.lower().split()

            if diretorio == 'Arquivo do Documento (File responses)':
                novo_nome.insert(0, 'DOC-')
            else:
                novo_nome.insert(0, 'COMP-')

            novo_nome = ''.join(novo_nome)
            os.rename(arquivo, novo_nome)

            move(novo_nome, f'../arquivos_documentos/{novo_nome}')
            print(f'    {novo_nome}')
        print('\033[35m -> Arquivos movidos para fora da pasta atual.\033[m')

        os.chdir('..')

    print('\033[1;33mPronto!\033[m')
    print('\n')


if __name__ == '__main__':
    renomear(nome_atual_pasta='Credenciamento TABU (File responses)')
    mover(path=('Arquivo do Documento (File responses)', 'Comprovante de Matrícula (File responses)'))