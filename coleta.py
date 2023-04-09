import sys
from library import formata_arquivo, coleta_Snmp, purgeFile

argumentos = len(sys.argv)
opcao = sys.argv[1]
pad = (f'python coleta.py ')
usoC1 = (f'{pad}-c 10.0.0.1 10.0.0.10 NOME_DA_PASTA\n\n')
usoC2 = (f'{pad}-c 10.0.0.1 NOME_DA_PASTA\n\n')
usoF = (f'{pad}-e NOME_DA_PASTA\n\n')
usoP = (f'{pad}-c json PASTA\n\n')
usoA = (f'{pad}?\n\n')
mensagem = (f'\n\nOpcoes de uso:\n\nCOLETA DE DADOS: -c\n\nIndividual: {usoC1}ou\n\nColetiva: {usoC2}EXPORTA JSON: -e pastaorigem\n{usoF}APAGA ARQUIVOS BASEADO NA EXTENSAO E PASTA INFORMADOS: -p extensaodoarquivo pasta\n{usoP}AJUDA: ?\n{usoA}')
if opcao == '-c'and (argumentos == 4 or argumentos == 5):
    if argumentos == 4:
        a = sys.argv[2]
        b = sys.argv[3]
        coleta_Snmp(a, a, b)
    elif argumentos == 5:
        a = sys.argv[2]
        b = sys.argv[3]
        c = sys.argv[4]
        coleta_Snmp(a,b,c)
else:
    print(mensagem)
    quit()

if opcao == '-e' and argumentos == 3:
    a = sys.argv[2]
    formata_arquivo(a)
else:
    print(mensagem)
    quit()

if opcao == '-p' and argumentos == 4:
    a = sys.argv[2]
    b = sys.argv[3]
    purgeFile(a, b)
else:
    print(mensagem)
    quit()

if opcao == '?':
    print(mensagem)
    quit()