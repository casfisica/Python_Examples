# Definicion de la funcion
def Duplica( lista ):
   "Funcion que duplica los valores de una lista dada"
   print "Valores fuera de la funcion ", lista
   for i in range(len(lista)):
     lista[i]=2*lista[i]
   print "Valores dentro de la funcion: ", lista
   return

# Ahora se llama a la funcion Duplica 
mi_lista = [10,20,30]
Duplica( mi_lista )
print "Valores fuera de la funcion: ", mi_lista
