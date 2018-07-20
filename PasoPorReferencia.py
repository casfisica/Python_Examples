# Definición de la función
def Duplica( lista ):
   "Función que duplica los valores de una lista dada"
   print ("Valores fuera de la función ", lista)
   for i in range(len(lista))::
     lista[i]=2*lista[i]
   print ("Valores dentro de la función: ", lista)
   return

# Ahora se llama a la función Duplica 
mi_lista = [10,20,30]
Duplica( mi_lista )
print ("Valores fuera de la función: ", mi_lista)
