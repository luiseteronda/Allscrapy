import scrapy
import json
import csv
from datetime import date

class SpidermercaSpider(scrapy.Spider):
    name = 'spidermerca'
    fecha_actual = date.today()
    file_name = open('E:\\zzretail\\Scrapy\\ficheros\\mercadona\\' + str(fecha_actual) + '.csv', 'w', newline='', encoding='utf-8')
    allowed_domains = ['https://tienda.mercadona.es/']
    field_names = ['Descripcion', 'Precio', 'Fecha', 'Url', 'Unit_size', 'ID_Producto']
    writer = csv.DictWriter(file_name, fieldnames=field_names, delimiter='#')
    writer.writeheader()
    start_urls = [
          'https://tienda.mercadona.es/api/products/45994/?lang=es&wh=vlc1', 
          'https://tienda.mercadona.es/api/products/46699/?lang=es&wh=vlc1',
          'https://tienda.mercadona.es/api/products/46567/?lang=es&wh=vlc1', 
          'https://tienda.mercadona.es/api/products/23184/?lang=es&wh=vlc1', 
          'https://tienda.mercadona.es/api/products/44326/?lang=es&wh=vlc1', 
          'https://tienda.mercadona.es/api/products/46497/?lang=es&wh=vlc1', 
          'https://tienda.mercadona.es/api/products/75997/?lang=es&wh=vlc1', 
          'https://tienda.mercadona.es/api/products/79201/?lang=es&wh=vlc1', 
          'https://tienda.mercadona.es/api/products/79631/?lang=es&wh=vlc1', 
          'https://tienda.mercadona.es/api/products/46791/?lang=es&wh=vlc1', 
          'https://tienda.mercadona.es/api/products/46440/?lang=es&wh=vlc1', 
          'https://tienda.mercadona.es/api/products/46444/?lang=es&wh=vlc1', 
          'https://tienda.mercadona.es/api/products/44332/?lang=es&wh=vlc1', 
          'https://tienda.mercadona.es/api/products/44273/?lang=es&wh=vlc1',
          'https://tienda.mercadona.es/api/products/40180/?lang=es&wh=vlc1',
          'https://tienda.mercadona.es/api/products/40732/?lang=es&wh=vlc1',
          'https://tienda.mercadona.es/api/products/72405/?lang=es&wh=vlc1',
          'https://tienda.mercadona.es/api/products/72536/?lang=es&wh=vlc1',
          'https://tienda.mercadona.es/api/products/67997/?lang=es&wh=vlc1'
          ]          
    ID_Producto = ['MER45994', 'MER46699', 'MER46567', 'MER23184', 'MER44326', 'MER46497', 'MER75997', 'MER79201', 'MER79631', 'MER46791', 'MER46440', 'MER46444', 'MER44332', 'MER44273', 'MER40180', 'MER40732', 'MER72405', 'MER72536', 'MER67997']
    i = 0
    
    def parse(self, response):
        
        datos_json = json.loads(response.body)
        price_instructions = datos_json['price_instructions']
        precio = price_instructions["unit_price"]
        details = datos_json['details']
        legal_name = details["description"]
        url_img = datos_json['thumbnail']
        size = price_instructions["unit_size"]

        self.writer.writerow({'Descripcion': legal_name, 'Precio': precio, 'Fecha': self.fecha_actual, 'Url': url_img, 'Unit_size': size, 'ID_Producto': self.ID_Producto[self.i]}) #writing data into file.
        self.i = self.i + 1
        
        return