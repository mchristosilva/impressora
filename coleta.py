import os
from library import formata_arquivo, coleta_Snmp, purgeFile, criajson

a = input('Entre com IP inicial                     : ')
b = input('Entre com IP final                       : ')
c = input('Nome da Pasta                            : ')

coleta_Snmp(a,b,c)
os.chdir('..')
formata_arquivo(c)
os.chdir('..')
purgeFile('txt', c)
os.chdir('..')