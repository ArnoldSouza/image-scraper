#  coding: utf-8

import csv
import os
import os
import time

# inicia contador geral
tinicio = time.time()

os.chdir(r'C:\Users\Arnold\Desktop\google-images-download-master')

csvfile = open('Cadastro.txt', encoding='utf-8', errors='ignore')
readCSV = csv.reader(csvfile, delimiter='\t')
itens = [row for row in readCSV]
csvfile.close()

info = open('log de evolução', 'a')  # Open the text file called database.txt
info.write('item' + '\t' + 'codigo' + '\t' + 'descrição' + '\t' + 'tempo (segundos)' + '\n')
info.close()  # Close the file
i = 1
for item in range(len(itens)):
    info = open('log de evolução', 'a')

    # inicia contador
    t0 = time.time()

    # pega informações de produto
    codigo = itens[item][0]
    nome = itens[item][1]
    nomeCompleto = itens[item][0]+'-'+itens[item][1]

    # cria string de comando
    stringConfig = 'python googleImagesDownload.py --keywords "' + nome + '" --limit 5 --cod "' + codigo + '"'

    # executa string
    print('configuração: ' + stringConfig)
    os.system(stringConfig)

    # computa o tempo
    t1 = time.time()
    total_time = t1 - t0
    print("Tempo de busca: " + str(total_time) + " segundos")

    # escreve em log
    info.write(str(i) + '\t' + itens[item][0] + '\t' + itens[item][1] + '\t' + str(total_time).replace('.', ',') + '\n')
    info.close()
    i += 1

# inicia contador geral
tfim = time.time()

total = tfim - tinicio

print('--->>> OPERAÇÃO FINALIZADA <<<---')
print("Tempo total: " + str(total) + " segundos")
