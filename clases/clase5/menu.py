listaNombres = ["Santiago",
                "juanes",
                "marco",
                "elena",
                "mch betancur",
                "mch mesa",
                "leslly",
                "ysabella",
                "santiago el humilde",
                "daniel",
                "mafer",
                "david",
                "susi",
                "daniel h"]
listaNombres[4] = "Maria Camila Betancur"
listaNombres[5] = "Maria Camila Mesa"
listaNombres.pop(-1)
listaNombres.append("Daniel Herrera")

_decision = int (input("""
      ingrese :
      1-para ver lista de Nombres
      2- para ver edades
      3-para ver notas
      4-salir  
"""))
while (_decision!=4):
  if (_decision == 1):
    print(listaNombres)
  elif (_decision == 2):
    print("aqui van las edades")
  elif (_decision ==3):
    print("aqui van las  notas")
  else:
    print("ingrese un valor valido")
  _decision = int (input("""
      ingrese :
      1-para ver lista de Nombres
      2- para ver edades
      3-para ver notas
      4-salir  
    """))
print("Gracias por usar el programa")
