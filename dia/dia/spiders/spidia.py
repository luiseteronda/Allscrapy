import scrapy
import csv
from datetime import date
import json
import re

class SpidiaSpider(scrapy.Spider):
    
    fecha_actual = date.today()
    
    file_name = open('E:\\zzretail\\Scrapy\\ficheros\\Dia\\' + str(fecha_actual) + '.csv', 'w', newline='', encoding='utf-8')
        
    field_names = ['Descripcion', 'Precio', 'Fecha', 'Url', 'Unit_size', 'ID_Producto']
      
    writer = csv.DictWriter(file_name, fieldnames=field_names,delimiter='#')
        
    writer.writeheader()
    
    name = 'spidia'
    allowed_domains = ['https://www.dia.es/compra-online/']
    start_urls = ['https://www.dia.es/compra-online/cuidado-del-hogar/ambientadores/p/230609',
                  'https://www.dia.es/compra-online/cuidado-personal/bano-e-higiene-personal/cuidado-del-cabello/p/215379',
                  'https://www.dia.es/compra-online/cuidado-personal/bano-e-higiene-personal/cuidado-del-cabello/p/151756',
                  'https://www.dia.es/compra-online/cuidado-del-hogar/ambientadores/p/277498',
                  'https://www.dia.es/compra-online/cuidado-del-hogar/ambientadores/p/277497',
                  'https://www.dia.es/compra-online/cuidado-del-hogar/ambientadores/p/277499',
                  'https://www.dia.es/compra-online/cuidado-del-hogar-de-limpieza/hogar/p/159540'
                  ]
    
    ID_Producto_URL = {'https://www.dia.es/compra-online/cuidado-del-hogar/ambientadores/p/230609' : 'BPTM00005940',
                       'https://www.dia.es/compra-online/cuidado-personal/bano-e-higiene-personal/cuidado-del-cabello/p/215379' : 'BPTM00004907',
                       'https://www.dia.es/compra-online/cuidado-personal/bano-e-higiene-personal/cuidado-del-cabello/p/151756' : 'BPTM00004887',
                       'https://www.dia.es/compra-online/cuidado-del-hogar/ambientadores/p/277498' : 'BPTM00006724',
                       'https://www.dia.es/compra-online/cuidado-del-hogar/ambientadores/p/277497' : 'BPTM00006722',
                       'https://www.dia.es/compra-online/cuidado-del-hogar/ambientadores/p/277499' : 'BPTM00006140',
                       'https://www.dia.es/compra-online/cuidado-del-hogar-de-limpieza/hogar/p/159540' : 'BPTM00003089'}
    

    def parse(self, response):
        
        for sel in response.xpath('//script'):
            
            script = sel.xpath('text()').get(default='not-found')
            if script.find("obj = {") == -1:
                print('not-found')
            else:
                print('yes-found')
                iniciosubstring = script.find("obj = {") + len("obj = ")
                finalsubstring = script.find("obj[\"typePage\"]") -9
                string = json.loads(re.sub('\'','\"',(script[iniciosubstring:finalsubstring]).replace("// Incidencia DIAEC-584, EMF, 201507", "")))
                
                size = string["productdescription"][-6:-3]
                sizeInLiters = int(size) / 1000
                
                self.writer.writerow({'Descripcion': string["productdescription"], 'Precio': string["prize"], 'Fecha': self.fecha_actual, 'Url': string["photo"], 'Unit_size': sizeInLiters, 'ID_Producto': self.ID_Producto_URL[response.url]})
       