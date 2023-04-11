

def formata_arquivo(pasta):
    pastA = ver_Pasta(pasta)
    arquivos = os.listdir()
    ext = str('.txt')
    for arquivo in arquivos:
        x = str(arquivo).endswith(ext)
        if x:
            f = open(arquivo,'r')
            listaSuja = []
            for linha in f:
                doispontos = linha.find(':')+2
                linhaTam = len(linha)-1
                aspas = linha.rfind('\"')
                texto = linha[doispontos:linhaTam]
                if aspas != -1:
                    texto = texto.replace('\"',"")
                    texto = texto.replace(',',"")
                    texto = texto.replace('S/N:"',"")
                    texto = texto.rstrip()
                    texto = cores(texto)
                    listaSuja.append(texto)
                else:
                    listaSuja.append(int(texto))

            listaSujaTam = len(listaSuja)

            dic = {'Data':'',
                    'IP':'',
                    'Fabricante':'',
                    'Modelo':'',
                    'Hostname':'',
                    'SerialNumber':'',
                    'Suprimentos':''}

            dataCabecalhos = []
            consumoSuprimentos = []

            if listaSujaTam > 6:
                cabecalhoTam = len(listaSuja)-6
                suprimentosTam = int(cabecalhoTam/3)

                divideSubListaSuja = [listaSuja[i:i + suprimentosTam] for i in range(6,listaSujaTam,suprimentosTam)]

                if not 'Amarelo' or not 'Ciano' or not 'Magenta' in divideSubListaSuja[0]:
                    a = 0
                else:
                    a = 3

                k = len(divideSubListaSuja[0])-1
                while k != a:
                    divideSubListaSuja[0].pop(k)
                    divideSubListaSuja[1].pop(k)
                    divideSubListaSuja[2].pop(k)
                    k-=1

                subLista1Tam = len(divideSubListaSuja[1])
                subLista2Tam = len(divideSubListaSuja[2])
                if subLista1Tam == subLista2Tam:
                    for i in range(0,subLista1Tam):
                        valor = calcula_Insumo(divideSubListaSuja[1][i],divideSubListaSuja[2][i])
                        consumoSuprimentos.append(valor)

                for i in range(0,6):
                    dataCabecalhos.append(listaSuja[i])

                dic['Data'] = dataCabecalhos[0]
                dic['IP'] = dataCabecalhos[1]
                dic['Fabricante'] = dataCabecalhos[2]
                dic['Modelo'] = dataCabecalhos[3]
                dic['Hostname'] = dataCabecalhos[4]
                dic['SerialNumber'] = dataCabecalhos[5]

                juntaLista = {i:j for i,j in zip(divideSubListaSuja[0],consumoSuprimentos)}
                dic['Suprimentos'] = juntaLista

                nomeJson = f'{pastA}_{dataCabecalhos[1]}.json'
                f.close()
                with open(nomeJson, 'w') as g:
                    json.dump(dic, g)
                    print(f'{nomeJson}: JSON ok')
            else:
                pass