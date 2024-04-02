#open("caminho","r")
# r - Leitura
# a - Append / Incrementar 
# w - Escrita 
# x - Criar Arquivo
# r+ Leitura + Escrita

MeuArquivo = open("Aula12/teste.txt")

#print(arquivo.readable())
#print(arquivo.read())
#print(arquivo.readline())
#print(arquivo.readline())

lista = MeuArquivo.readlines()

print(lista)
print(lista[3])

MeuArquivo.close()



