tecnologias = ["HTML5","CSS3","Javascript","PHP"]
#             0       1          2        3

#print(tecnologias[2])  - retorna um indice
#print(tecnologias[-3]) - retorna um indice de traz para frente
#print(tecnologias[2:])  # retorna a partir do indice 2

tecnologias.extend(["Laravel","Django"])

#tecnologias.append("React")
tecnologias.insert(3,"React")
#tecnologias.pop()
tecnologias.remove("PHP")
print(tecnologias)


