from SaveInBigQuery import Csv2BQ 
import sys
import os
import shutil

csv2BQ1 = Csv2BQ()

pathMercadona="E:\\zzretail\\Scrapy\\ficheros\\mercadona\\"
pathDia="E:\\zzretail\\Scrapy\\ficheros\\Dia\\"
pathCarrefour="E:\\zzretail\\Scrapy\\ficheros\\Carrefour\\"
pathMaquillalia="E:\\zzretail\\Scrapy\\ficheros\\Maquillalia\\"
pathPrimor="E:\\zzretail\\Scrapy\\ficheros\\Primor\\"
pathPerfumeriasLaguna="E:\\zzretail\\Scrapy\\ficheros\\Perfumerias Laguna\\"
   
    
def SaveOnBQ(distributor,file_name):
           


    Csv2BQ.read_csv(csv2BQ1, file_name)

    Csv2BQ.SaveOnBQ(csv2BQ1, distributor)



# shutil.move(pathMercadona, pathMercadona+"old\\")
# recibir parámetros con los directorios, es decir se llamara a la funcion
# python EjecutarCSV2BQ.py E:\\zzretail\\Scrapy\\ficheros\\mercadona\\ .......................... (LOS 4 DIRECTORIOS)

# Mirar r ficheros .csv del pathMercadona
# for file in os.listdir(pathMercadona):
#    if file.endswith(".csv"):
#         fichero  = file   
#

distribuidor = 'Mercadona'

for file in os.listdir(pathMercadona):
    
    if file.endswith(".csv"):
        
        fichero = pathMercadona + file

        SaveOnBQ(distribuidor, fichero)
        
        shutil.move(fichero, pathMercadona+"old\\")


distribuidor = 'Dia'

for file in os.listdir(pathDia):
    
    if file.endswith(".csv"):
        
        fichero = pathDia + file

        SaveOnBQ(distribuidor, fichero)
        
        shutil.move(fichero, pathDia+"old\\")

'''
distribuidor = 'Carrefour'

for file in os.listdir(pathCarrefour):
    
    if file.endswith(".csv"):
        
        fichero = pathCarrefour + file

        SaveOnBQ(distribuidor, fichero)
        
        shutil.move(fichero, pathCarrefour+"old\\")
'''

distribuidor = 'Maquillalia'

for file in os.listdir(pathMaquillalia):
    
    if file.endswith(".csv"):
        
        fichero = pathMaquillalia + file
        
        SaveOnBQ(distribuidor, fichero)
        
        shutil.move(fichero, pathMaquillalia+"old\\")


distribuidor = 'Primor'

for file in os.listdir(pathPrimor):
    
    if file.endswith(".csv"):
        
        fichero = pathPrimor + file

        SaveOnBQ(distribuidor, fichero)
        
        shutil.move(fichero, pathPrimor+"old\\")


distribuidor = 'Perfumerias Laguna'

for file in os.listdir(pathPerfumeriasLaguna):
    
    if file.endswith(".csv"):
        
        fichero = pathPerfumeriasLaguna + file

        SaveOnBQ(distribuidor, fichero)
        
        shutil.move(fichero, pathPerfumeriasLaguna+"old\\")