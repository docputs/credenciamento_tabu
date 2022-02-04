from robo_navegador import *
from dados_ritmistas import ler_dados
from alterar_docs import *

nomes = ('Matheus Delaqua Rocha De Jesus',
         'Cecília')

if __name__ == '__main__':
    renomear(nome_atual_pasta='Credenciamento TABU (File responses)')
    mover(path=('Arquivo do Documento (File responses)', 'Comprovante de Matrícula (File responses)'))

    site = Navegador()
    site.logar('amandaturno@usp.br', 'asequith')
    lista = ler_dados()

    for pessoa in lista:
        if not (pessoa.arquivo_doc or pessoa.comprovante) == 'Arquivo não encontrado\n':
            if pessoa.nome not in nomes:
                site.cadastrar_ritmista(pessoa)
                sleep(5)
        else:
            print(f'\033[1;7;30mPulando {pessoa.nome}...\033[m')

    print(f'\033[1;7;30mPrograma finalizado, {site.contador} ritmistas cadastrados\033[m')
