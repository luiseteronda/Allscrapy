import scrapy
import csv
from datetime import date
import json
import re

class SpicarreSpider(scrapy.Spider):
    

    fecha_actual = date.today()
    
    file_name = open('E:\\zzretail\\Scrapy\\ficheros\\Carrefour\\' + str(fecha_actual) + '.csv', 'w', newline='', encoding='utf-8')
    
    field_names = ['Descripcion', 'Precio', 'Fecha', 'Url', 'Unit_size', 'ID_Producto']
    
    writer = csv.DictWriter(file_name, fieldnames=field_names,delimiter='#')
    
    writer.writeheader()

    name = 'spicarre'
    
    allowed_domains = ['www.carrefour.es']
    
    start_urls = ['https://www.carrefour.es/mascarilla-capilar-reparadora-keratine-agrado-500-ml/8433295048273/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns',
                  'https://www.carrefour.es/agrado-champu-cabellos-grasos-750-ml-750-ml/8433295030872/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns']
    
    ID_Producto_URL = {'https://www.carrefour.es/mascarilla-capilar-reparadora-keratine-agrado-500-ml/8433295048273/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns' : 'BPTM00005504',
                       'https://www.carrefour.es/agrado-champu-cabellos-grasos-750-ml-750-ml/8433295030872/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns' : 'BPTM00005972'}
                  
    
    def parse(self, response):
        
        for sel in response.xpath('//script[@type="application/ld+json"]'):
            
            script = sel.xpath('text()').get(default='not-found')
            print('-----------------')
            print(script)
            print('-----------------')
            if script.find("\"offers\":{") == -1:
                print('-----------------')
                print('not-found')
                print('-----------------')
                
            else:
                print('-----------------')
                print('foundedd')
                print('-----------------')
                json_datos = json.loads(script)
                print('-----------------')
                print(json_datos)
                print('-----------------')
                json_offers = json.loads(re.sub('\'','\"',str(json_datos["offers"])))
                price = json_offers['price'].replace("€", "").replace(",", ".").strip()
                
                self.writer.writerow({'Descripcion': json_datos['name'], 'Precio': price, 'Fecha': self.fecha_actual, 'Url': json_datos['image'], 'ID_Producto': self.ID_Producto_URL[response.url]})
       