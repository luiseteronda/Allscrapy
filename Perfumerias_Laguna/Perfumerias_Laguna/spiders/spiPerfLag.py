import scrapy
import csv
from datetime import date

class SpiperflagSpider(scrapy.Spider):
    
    fecha_actual = date.today()
    
    file_name = open('E:\\zzretail\\Scrapy\\ficheros\\Perfumerias Laguna\\' + str(fecha_actual) + '.csv', 'w', newline='', encoding='utf-8')
    
    field_names = ['Descripcion', 'Precio', 'Fecha', 'Url', 'Unit_size', 'ID_Producto']
    
    writer = csv.DictWriter(file_name, fieldnames=field_names, delimiter='#')
    
    writer.writeheader()
    
    name = 'spiPerfLag'
    allowed_domains = ['www.perfumeriaslaguna.com']
    start_urls = ['https://www.perfumeriaslaguna.com/champu-agrado-cabello-graso',
                  'https://www.perfumeriaslaguna.com/mascarilla-agrado-reparadora-500-ml',
                  'https://www.perfumeriaslaguna.com/mascarilla-agrado-keratina-500-ml',
                  'https://www.perfumeriaslaguna.com/champu-agrado-cabello-fino',
                  'https://www.perfumeriaslaguna.com/agua-de-colonia-gotas-de-agrado-1000ml',
                  'https://www.perfumeriaslaguna.com/agrado-bifasico-400ml',
                  'https://www.perfumeriaslaguna.com/ambientador-mayordomo-spray-250-talco',
                  'https://www.perfumeriaslaguna.com/ambientador-mayordomo',
                  'https://www.perfumeriaslaguna.com/ambientador-mayordomo-spray-250-colonia',
                  'https://www.perfumeriaslaguna.com/ambientador-mayordomo-1',
                  #'https://www.perfumeriaslaguna.com/ambientador-un-toque-flores-blancas-aparato2rec',
                  'https://www.perfumeriaslaguna.com/ambientador-mayordomo-spray-250-esencia-tahiti',
                  'https://www.perfumeriaslaguna.com/ambientador-mayordomo-spray-250-aire-de-sevilla'
                  # Son los ambientadores
                  ]
    
    ID_Producto_URL = {'https://www.perfumeriaslaguna.com/champu-agrado-cabello-graso' : 'BPTM00005972',
                       'https://www.perfumeriaslaguna.com/mascarilla-agrado-reparadora-500-ml' : 'BPTM00005506',
                       'https://www.perfumeriaslaguna.com/mascarilla-agrado-keratina-500-ml' : 'BPTM00005504',
                       'https://www.perfumeriaslaguna.com/champu-agrado-cabello-fino' : 'BPTM00005971',
                       'https://www.perfumeriaslaguna.com/agua-de-colonia-gotas-de-agrado-1000ml' : 'BPTM00004896',
                       'https://www.perfumeriaslaguna.com/agrado-bifasico-400ml' : 'BPTM00004826',
                       'https://www.perfumeriaslaguna.com/ambientador-mayordomo-spray-250-talco' : 'BPTM00004522',
                       'https://www.perfumeriaslaguna.com/ambientador-mayordomo' : 'BPTM00006140',
                       'https://www.perfumeriaslaguna.com/ambientador-mayordomo-spray-250-colonia' : 'BPTM00004616',
                       'https://www.perfumeriaslaguna.com/ambientador-mayordomo-1' : 'BPTM00004615',
                       'https://www.perfumeriaslaguna.com/ambientador-mayordomo-spray-250-esencia-tahiti' : 'BPTM00003671',
                       'https://www.perfumeriaslaguna.com/ambientador-mayordomo-spray-250-aire-de-sevilla' : 'BPTM00003670'}
    
    
    def parse(self, response):
        
        price = response.xpath('//meta[@itemprop="price"]/@content').extract_first()
        
        name = response.xpath('//meta[@itemprop="name"]/@content').extract_first()
        
        url_img = response.xpath('//li/span/a/@href').extract_first()
        for d in range(len(name.split(" "))):
            print(d)
            
            if name.split(" ")[d] == ("250"):
                print('tekeennn')
                sizeOUTml = name.split(" ")[d]
                print(sizeOUTml)
                sizeOUTmlInLiters = int(sizeOUTml) / 1000
            
                self.writer.writerow({'Descripcion': name, 'Precio': price, 'Fecha': self.fecha_actual, 'Url': url_img, 'Unit_size': sizeOUTmlInLiters, 'ID_Producto': self.ID_Producto_URL[response.url]}) #writing data into file.
                
            else:
                print('no hubo sort')    
            
            if name.split(" ")[d].find("ml") == -1:
                
                print('no hubo sort')
                
                
            else:
                
                size = name[-6:].replace("ml", "").strip()
        
                print(size)
                sizeInLiters = int(size) / 1000
            
                self.writer.writerow({'Descripcion': name, 'Precio': price, 'Fecha': self.fecha_actual, 'Url': url_img, 'Unit_size': sizeInLiters, 'ID_Producto': self.ID_Producto_URL[response.url]}) #writing data into file.

 