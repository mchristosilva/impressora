import json, os, sys
from library import ver_Pasta

def isIp(ip):
    
    ip = ip.split('.')
    ip_sz = len(ip)
    
    if ip_sz == 4:
        ip = [int(item) for item in ip]
        a = []

        for n in ip:
            if n < 0 or n > 255:
                quit()

        for o in range (0, ip_sz):
            a.insert(o, ip[o])

        return (f'{a[0]}.{a[1]}.{a[2]}.{a[3]}'), True
    else:
        quit()

lArg = len(sys.argv)-1

if lArg == 0 or lArg == 1 or lArg > 3:
    pass
elif lArg == 2:
    op2 = sys.argv[2]
    ipI2,ipI2S = isIp(sys.argv[1])
    ipF2 = ipI2
    if ipI2S and op2.isalpha():
        print(f'{ipI2} , {op2}')
elif lArg == 3:
    op3 = sys.argv[3]
    ipI3, ipI3S = isIp(sys.argv[1])
    ipF3, ipF3S = isIp(sys.argv[2])
    if ipI3S and ipF3S and op3.isalpha():
        print(f'{ipI3} , {ipF3} , {op3}')
else:
    quit()

def criajson(pasta):
    ver_Pasta(pasta)
    x = os.listdir()
    dados_json = {'Equipamento':""}
    for file in x:
        with open(file, 'r+') as f:
            fdata = json.load(f)
            dados_json.update({'Equipamento':fdata})
            with open('dados.json', 'a+') as saida:
                json.dump(dados_json, saida, indent=4)