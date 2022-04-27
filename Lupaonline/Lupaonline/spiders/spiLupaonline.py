import scrapy
import csv
from datetime import date
import json
import re

class SpilupaonlineSpider(scrapy.Spider):
    
    fecha_actual = date.today()
    
    file_name = open('E:\\zzretail\\Scrapy\\ficheros\\Lupa online\\' + str(fecha_actual) + '.csv', 'w', newline='', encoding='utf-8')
    
    field_names = ['Descripcion', 'Precio', 'Fecha', 'Url', 'Unit_size', 'ID_Producto']
    
    writer = csv.DictWriter(file_name, fieldnames=field_names,delimiter='#')
    
    writer.writeheader()
    
    name = 'spiLupaonline'
    allowed_domains = ['www.lupaonline.com']
    start_urls = ['https://www.lupaonline.com/santander/quitagrasa-asevi-pistola-750-ml',
                  'https://www.lupaonline.com/santander/suavizante-selex-concentrado-72-lavados-lavanda-2-litros']
    
    ID_Producto = ['BPTM00008445', 'BPTM00005319']
    i = 0  

    def parse(self, response):
        
        for sel in response.xpath('//script[@data-cookieconsent="marketing"]'):
            script = sel.xpath('text()').get(default='not-found')
            
            if script.find("\"products\":") == -1:
                print('not-found')
                
            else:
                print('yes-found')
                iniciosubstring = script.find("dataLayer.push(") + len("dataLayer.push(")
                finalsubstring = script.find("(function (w, d, s, l, i)") - 11
                string = script[iniciosubstring:finalsubstring]
                
                offers = json.loads(string)
                #products = re.sub('\'','\"',str(offers["products"]))
                products = json.loads(re.sub('True','true',re.sub('False','false',re.sub('\'','\"',str(offers['ecommerce']["detail"]["products"][0])))))
                price = products["price"]
                name = products["name"]
                
                
                
                
                
                
                
                #price = offers['ecommerce']["detail"]["products"]["price"]
                url_img = response.xpath('//img[@class="etalage_source_image"]/@src').extract_first()
                
                self.writer.writerow({'Descripcion': name, 'Precio': price, 'Fecha': self.fecha_actual, 'Url': url_img, 'ID_Producto': self.ID_Producto[self.i]})
       
                self.i = self.i + 1
                
        
