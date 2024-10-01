"""
Arquivo de Desencriptação
"""

import os
import cryptography.fernet as cripto

files = []

with open("chave.key", "rb") as key:
    secretkey = key.read()

for file in os.listdir():
    if file == "darth_vader.py" or file == "chave.key" or file == "luke_sky.py" or file == "README.md":
        continue
    if os.path.isfile(file):
        files.append(file)


for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()
    conteudo_decrypted = cripto.Fernet(secretkey).decrypt(conteudo)
    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_decrypted)


