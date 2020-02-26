#-------------Mensajes---------------#
PREGUNTA_PACIENTES="ingrese cantidad pacientes \n"
PREGUNTA_PACIENTES_UCI="ingrese cantidad pacientes en UCI \n"
MENSAJE_BIENVENIDA="Bienveinido al programa de detección \n de riesgo operacional"
MENSAJE_RIESGO_BAJO = "Se en encuentra en riesgo bajo"
MENSAJE_RIESGO_MEDIO = "Se en encuentra en riesgo medio"
MENSAJE_RIESGO_ALTO = "Se en encuentra en riesgo alto"
MARCO = "#"*60
MENSAJE_DESPEDIDA="Gracias pro usar el codigo"
#---------------------------------------
#-------------Entradas---------------#
_cantidadPacientes = 0
_cantidadPacientesUCI = 0
#---------------------------------------
#-------------Salidas---------------#
riesgoOperacional = ""
#---------------------------------------
print(MARCO)
print(MENSAJE_BIENVENIDA)
print(MARCO)
_cantidadPacientes = int (input(PREGUNTA_PACIENTES))
if (_cantidadPacientes>0 and _cantidadPacientes <= 1000):
  riesgoOperacional=MENSAJE_RIESGO_BAJO
elif (_cantidadPacientes <5000):
  print(MARCO)
  _cantidadPacientesUCI = int (input(PREGUNTA_PACIENTES_UCI))
  print(MARCO)
  if (_cantidadPacientesUCI >1000 ):
    riesgoOperacional = MENSAJE_RIESGO_ALTO
  else:
    riesgoOperacional = MENSAJE_RIESGO_MEDIO
else:
  riesgoOperacional = MENSAJE_RIESGO_ALTO

print(MARCO)
print("Su hospital {} durante el dia de hoy".format(riesgoOperacional))
print(MARCO)