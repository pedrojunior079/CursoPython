tenho_sede = True
tenho_fome = False
estou_em_dieta = True

if tenho_sede and tenho_fome:
   print("fazer sanduiche e suco")
elif tenho_sede and not(tenho_fome):
    if estou_em_dieta:
       print("tomar agua")
    else:
       print("Tomar um suco")
elif not(tenho_sede) and tenho_fome:
    print("Fazer um sanduiche")
else:
    print("Ficar vendo netflix")

