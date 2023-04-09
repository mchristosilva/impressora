import os, re, json
from datetime import datetime as dt

def faixa_Ip(ipi, ipf):
    ipi = ipi.split('.')
    ipi_sz = len(ipi)
    ipi = [int(item) for item in ipi]

    ipf = ipf.split('.')
    ipf_sz = len(ipf)
    ipf = [int(item) for item in ipf]

    for x in ipi or ipf:
        if x < 0 or x > 255:
            quit()

    if ipi_sz == 4 and ipf_sz == 4:
        a = []
        b = []
        for n in range (0, 4):
            if n < 3 and ipi[n] == ipf[n]:
                a.insert(n, ipi[n])
                b.insert(n, ipf[n])
            elif n == 3 and ipi[n] <= ipf[n]:
                a.insert(n, ipi[n])
                b.insert(n, ipf[n])
            else:
                quit()

    cadeia = f'{ipi[0]}.{ipi[1]}.{ipi[2]}'
    inicio = int(ipi[3])
    faixa = int((ipf[3]-ipi[3])+1)

    return cadeia, inicio, faixa

def snmp(ip, arquivo):
    coleta1 = os.system(f'snmpwalk -v1 -Oav -t1 -c public -r1 {ip} iso.3.6.1.2.1.43.8.2.1.14.1.1 >> {arquivo}')   # Fabricante
    coleta2 = os.system(f'snmpwalk -v1 -Oav -t1 -c public -r1 {ip} iso.3.6.1.2.1.25.3.2.1.3.1 >> {arquivo}')       # Modelo de impressora
    coleta3 = os.system(f'snmpwalk -v1 -Oav -t1 -c public -r1 {ip} iso.3.6.1.2.1.43.5.1.1.16.1 >> {arquivo}')     # Hostname
    coleta4 = os.system(f'snmpwalk -v1 -Oav -t1 -c public -r1 {ip} iso.3.6.1.2.1.43.5.1.1.17.1 >> {arquivo}')     # Serial Number
    coleta5 = os.system(f'snmpwalk -v1 -Oav -t1 -c public -r1 {ip} iso.3.6.1.2.1.43.11.1.1.6.1 >> {arquivo}')     # Dispositivos
    coleta6 = os.system(f'snmpwalk -v1 -Oav -t1 -c public -r1 {ip} iso.3.6.1.2.1.43.11.1.1.9.1 >> {arquivo}')     # Capacidade utilizada
    coleta7 = os.system(f'snmpwalk -v1 -Oav -t1 -c public -r1 {ip} iso.3.6.1.2.1.43.11.1.1.8.1 >> {arquivo}')     # Capacidade total

def tempo():
    estampa = dt.now()
    estampa = dt.timestamp(estampa)
    estampa = dt.fromtimestamp(estampa)
    estampa = estampa.strftime('%d-%m-%Y %H:%M:%S')

    return estampa

def coleta_Snmp(ipi, ipf, pasta):
    cadeia, inicio, faixa = faixa_Ip(ipi,ipf)
    for x in range(inicio, inicio + faixa):
        ver_Pasta(pasta)
        ip = f'{cadeia}.{str(x)}'
        arquivo = f'{pasta}_{ip}.txt'

        ping = os.system(f'ping -n 1 {ip} > null')

        if ping == 0:
            hora = tempo()
            arquivo = ver_Arquivo(arquivo)
            print(f'{ip}: Sucesso')
            arquivo.write(f'STRING: "{hora}"\n')
            arquivo.write(f'STRING: "{ip}"\n')
            arquivo.close
            # snmp(ip,arquivo)
        else:
            print(f'{ip}: Falha')
        os.chdir('..')

def ver_Arquivo(arquivo):
    existe = os.path.exists(arquivo)
    if existe:
        os.remove(arquivo)
        arquivo = open(arquivo, 'at')
    else:
        arquivo = open(arquivo, 'at')

    return arquivo

def ver_Pasta(pasta):
    existe = os.path.exists(pasta)
    if existe:
        os.chdir(pasta)
    else:
        os.mkdir(pasta)
        os.chdir(pasta)

    return pasta

def calcula_Insumo(n1, n2):
    if n2 != 0:
        porcentagem = n1 / n2 * 100
    else:
        quit()

    return int(porcentagem)

def cores(cor):
    if re.findall('yellow',cor,re.IGNORECASE) or re.findall('amarelo',cor,re.IGNORECASE):
        cor = ''
        cor = 'Amarelo'
    elif re.findall('cyan',cor,re.IGNORECASE) or re.findall('ciano',cor,re.IGNORECASE):
        cor = ''
        cor = 'Ciano'
    elif re.findall('magenta',cor,re.IGNORECASE):
        cor = ''
        cor = 'Magenta'
    elif re.findall('black',cor,re.IGNORECASE) or re.findall('preto',cor,re.IGNORECASE):
        cor = ''
        cor = 'Preto'
        
    return cor

def formata_arquivo(pasta):
    arquivos = os.listdir(pasta)
    for arquivo in arquivos:
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
            suprimentosTam = int(cabecalhoTam)

            divideSubListaSuja = [listaSuja[i:i + suprimentosTam] for i in range(5,listaSujaTam,suprimentosTam)]

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

            nomeJson = f'{pasta}_{dataCabecalhos[1]}.json'
            f.close()
            with open(nomeJson, 'w') as g:
                json.dumps(dic, g)
        else:
            pass
    os.chdir('..')
