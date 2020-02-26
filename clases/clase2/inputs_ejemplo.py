
#-------------Mensajes---------------#
PREGUNTA_NOMBRE="ingrese su nombre \n "
MENSAJE_BIENVENIDO="Bienveinido"
MENSAJE_DESPEDIDA="CHAO"
#---------------------------------------

_nombrePersona = input(PREGUNTA_NOMBRE)
print(MENSAJE_BIENVENIDO,_nombrePersona, "a este programa")
_edadPersona =int(input("ingrese su edad \n "))
print("Tu edad es",_edadPersona)
print (type(_edadPersona))
_estaturaPersona =float(input("ingrese su estatura \n "))
print("Tu estatura es",_estaturaPersona)
print (type(_estaturaPersona))
print(MENSAJE_DESPEDIDA)
