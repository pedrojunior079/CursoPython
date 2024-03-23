def fazer_big_mac(nome):
    print(f"sanduiche big mac {nome}")


fazer_big_mac("Andre")
fazer_big_mac("João")
fazer_big_mac("Carla")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def preparar_refrigerante(tipo,tamanho):
    print(f"{tipo} {tamanho}")

#fazer_big_mac("Andre")
#fazer_batata("Grande")
#preparar_refrigerante("Guarana","Media")

def fazer_combo_big_mac(nome,tamanho_batata,tipo_refri,tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri,tamanho_refri)

fazer_combo_big_mac("Andre","Grande","Guarana","Medio")




