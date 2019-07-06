lista = [1,2,3,4,5,6,7,8,9]
archivo = open("resultados.txt", "w+")
for i in lista:
    archivo.write( "{} \r\n".format(i) )
archivo.close()
