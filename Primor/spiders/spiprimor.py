import scrapy

from datetime import date

import csv

class SpiprimorSpider(scrapy.Spider):
    
    fecha_actual = date.today()
    
    file_name = open('E:\\zzretail\\Scrapy\\ficheros\\Primor\\' + str(fecha_actual) + '.csv', 'w', newline='', encoding='utf-8')
    
    field_names = ['Descripcion', 'Precio', 'Fecha', 'Url', 'Unit_size', 'ID_Producto']
    
    writer = csv.DictWriter(file_name, fieldnames=field_names,delimiter='#')
    
    writer.writeheader()
    
    name = 'spiprimor'
    allowed_domains = ['www.primor.eu']
    start_urls = ['https://www.primor.eu/agrado/57807-mascarilla-capilar-reparadora.html',
                  'https://www.primor.eu/agrado/23619-crema-suavizante-keratina.html',
                  'https://www.primor.eu/agrado/33488-mascarilla-capilar-keratina.html',
                  'https://www.primor.eu/agrado/21427-colonia-gotas-agrado.html?q=%2Fagrado%2F21427-colonia-gotas-agrado-8433295043599.html',
                  'https://www.primor.eu/agrado/32022-acondicionador-bifasico.html?q=%2Fagrado%2F32022-acondicionador-bifasico-8433295048266.html',
                  'https://www.primor.eu/agrado/73694-locion-solar-spf50-kids-pieles-sensibles.html?q=%2Fagrado%2F73694-locion-solar-spf50-kids-pieles-sensibles-8433295073121.html',
                  'https://www.primor.eu/agrado/36629-agua-micelar-desmaquillante.html',
                  'https://www.primor.eu/agrado/53840-bruma-seca-kids-pieles-sensibles.html',
                  'https://www.primor.eu/agrado/58704-gel-de-bano-y-ducha-tropical.html',
                  'https://www.primor.eu/agrado/45694-after-sun-hidrocalmante-locion-en-aerosol.html',
                  'https://www.primor.eu/agrado/44209-spray-texturizante-ondas-surferas.html',
                  'https://www.primor.eu/agrado/31408-jabon-intimo-con-dosificador.html',
                  'https://www.primor.eu/agrado/21389-tonico-facial.html',
                  'https://www.primor.eu/agrado/57803-champu-reparador-nutritivo.html',
                  'https://www.primor.eu/agrado/35459-quitaesmalte-hidratante.html',
                  'https://www.primor.eu/agrado/33487-champu-tratamiento-keratina.html',
                  'https://www.primor.eu/agrado/36630-crema-de-manos-concentrada.html',
                  'https://www.primor.eu/agrado/73695-crema-solar-alta-proteccion-spf50.html',
                  'https://www.primor.eu/agrado/73688-champu-profesional-reparacion-brillo-intenso.html',
                  'https://www.primor.eu/agrado/73687-champu-profesional-nutricion-cabellos-secos-y-fragiles.html',
                  'https://www.primor.eu/agrado/52393-mini-crema-go-rosa-mosqueta.html',
                  'https://www.primor.eu/agrado/51813-desodorante-body-spray-sweet-love.html',
                  'https://www.primor.eu/agrado/58703-gel-de-bano-y-ducha-mediterraneo.html',
                  'https://www.primor.eu/agrado/57805-body-milk-rosa-mosqueta.html',
                  'https://www.primor.eu/agrado/44230-gel-de-bano-y-ducha-sales-minerales.html',
                  'https://www.primor.eu/agrado/38344-desodorante-roll-on.html',
                  'https://www.primor.eu/agrado/76703-desodorante-roll-on-rosa-mosqueta.html',
                  'https://www.primor.eu/agrado/33441-keratina-liquida-anti-encrespamiento.html',
                  'https://www.primor.eu/agrado/21388-leche-limpiadora-facial.html',
                  'https://www.primor.eu/agrado/53842-hidragel-aloe-vera-after-sun.html',
                  'https://www.primor.eu/agrado/70041-champu-en-seco.html',
                  'https://www.primor.eu/agrado/36276-desodorante-body-spray-para-hombre.html',
                  'https://www.primor.eu/agrado/36277-enjuague-bucal.html'
                  ]
    
    
    
    ID_Producto_URL = {'https://www.primor.eu/agrado/57807-mascarilla-capilar-reparadora.html' : 'BPTM00005506',
                       'https://www.primor.eu/agrado/23619-crema-suavizante-keratina.html' : 'BPTM00004907',
                       'https://www.primor.eu/agrado/33488-mascarilla-capilar-keratina.html' : 'BPTM00005504',
                       'https://www.primor.eu/agrado/21427-colonia-gotas-agrado.html?q=%2Fagrado%2F21427-colonia-gotas-agrado-8433295043599.html' : 'BPTM00004896',
                       'https://www.primor.eu/agrado/32022-acondicionador-bifasico.html?q=%2Fagrado%2F32022-acondicionador-bifasico-8433295048266.html' : 'BPTM00004826',
                       'https://www.primor.eu/agrado/73694-locion-solar-spf50-kids-pieles-sensibles.html?q=%2Fagrado%2F73694-locion-solar-spf50-kids-pieles-sensibles-8433295073121.html' : 'BPTM00007312',
                       'https://www.primor.eu/agrado/36629-agua-micelar-desmaquillante.html' : ['BPTM00006030', 'BPTM00006282'],
                       'https://www.primor.eu/agrado/53840-bruma-seca-kids-pieles-sensibles.html' : 'BPTM00006223',
                       'https://www.primor.eu/agrado/58704-gel-de-bano-y-ducha-tropical.html' : 'BPTM00006180',
                       'https://www.primor.eu/agrado/45694-after-sun-hidrocalmante-locion-en-aerosol.html' : 'BPTM00006079',
                       'https://www.primor.eu/agrado/44209-spray-texturizante-ondas-surferas.html' : 'BPTM00006240',
                       'https://www.primor.eu/agrado/31408-jabon-intimo-con-dosificador.html' : 'BPTM00005769',
                       'https://www.primor.eu/agrado/21389-tonico-facial.html' : 'BPTM00004904',
                       'https://www.primor.eu/agrado/57803-champu-reparador-nutritivo.html' : 'BPTM00004882',
                       'https://www.primor.eu/agrado/35459-quitaesmalte-hidratante.html' : 'BPTM00004878',
                       'https://www.primor.eu/agrado/33487-champu-tratamiento-keratina.html' : 'BPTM00004828',
                       'https://www.primor.eu/agrado/36630-crema-de-manos-concentrada.html' : 'BPTM00005964',
                       'https://www.primor.eu/agrado/73695-crema-solar-alta-proteccion-spf50.html' : 'BPTM00008332',
                       'https://www.primor.eu/agrado/73688-champu-profesional-reparacion-brillo-intenso.html' : 'BPTM00006327',
                       'https://www.primor.eu/agrado/73687-champu-profesional-nutricion-cabellos-secos-y-fragiles.html' : 'BPTM00006326',
                       'https://www.primor.eu/agrado/52393-mini-crema-go-rosa-mosqueta.html' : 'BPTM00006248',
                       'https://www.primor.eu/agrado/51813-desodorante-body-spray-sweet-love.html' : 'BPTM00006184',
                       'https://www.primor.eu/agrado/58703-gel-de-bano-y-ducha-mediterraneo.html' : 'BPTM00006177',
                       'https://www.primor.eu/agrado/57805-body-milk-rosa-mosqueta.html' : 'BPTM00005671',
                       'https://www.primor.eu/agrado/44230-gel-de-bano-y-ducha-sales-minerales.html' : 'BPTM00005491',
                       'https://www.primor.eu/agrado/38344-desodorante-roll-on.html' : 'BPTM00005252',
                       'https://www.primor.eu/agrado/76703-desodorante-roll-on-rosa-mosqueta.html' : 'BPTM00005251',
                       'https://www.primor.eu/agrado/33441-keratina-liquida-anti-encrespamiento.html' : 'BPTM00004918',
                       'https://www.primor.eu/agrado/21388-leche-limpiadora-facial.html' : 'BPTM00004903',
                       'https://www.primor.eu/agrado/53842-hidragel-aloe-vera-after-sun.html' : 'BPTM00006079',
                       'https://www.primor.eu/agrado/70041-champu-en-seco.html' : ['BPTM00006559', 'BPTM00006560'],
                       'https://www.primor.eu/agrado/36276-desodorante-body-spray-para-hombre.html' : ['BPTM00005257', 'BPTM00005256', 'BPTM00005258'],
                       'https://www.primor.eu/agrado/36277-enjuague-bucal.html' : ['BPTM00005284', 'BPTM00005283']
                       }
    Claves_producto = {'250 ML': 'BPTM00006030', '400 ML': 'BPTM00006282', 'Floral': 'BPTM00006559', 'Frutal': 'BPTM00006560', 'Fresh Water': 'BPTM00005257', 'Ice Sensation': 'BPTM00005256', 'Wild Chocolate': 'BPTM00005258', 'Dientes Blancos': 'BPTM00005284', 'Menta': 'BPTM00005283'}
    
    def parse(self, response):
        
        Url_img = response.xpath('//span[@class="img-producto"]/img/@data-src').extract_first()
        
        datos = response.xpath('//ul/li/input/@onclick').extract()
        
        for i in range(len(datos)):
            if len(datos) > 1:
                
                
                strdatos = str(datos[i])
           
                datosLimpio = strdatos.replace("\"onProductAttributeClick(", "").replace(")\"", "").replace("'", "")
            
                ##  self.ID_Producto_URL[response.Url] Comprobar si es un array o no 
                # si es un array claves_producto[la propiedad que has leido]
                 
                datosArray = datosLimpio.split(",")
                
                price = datosArray[2].strip()
            
                description = datosArray[1].strip()
            
                size = datosArray[-4].strip()
                print('---------------------')
                print(size)
                print('---------------------')
                if type(self.ID_Producto_URL[response.url]) is list:                                                                                      
                    
                    self.writer.writerow({'Descripcion': description, 'Precio': price, 'Fecha': self.fecha_actual, 'Url': Url_img, 'Unit_size': size.replace("ML", "").replace("ml", ""), 'ID_Producto': self.Claves_producto[size]})
                       
                else:
                    self.writer.writerow({'Descripcion': description, 'Precio': price, 'Fecha': self.fecha_actual, 'Url': Url_img, 'Unit_size': size, 'ID_Producto': self.ID_Producto_URL[response.url]})
            else:
                strdatos = str(datos[i])
           
                datosLimpio = strdatos.replace("\"onProductAttributeClick(", "").replace(")\"", "").replace("'", "")
            
            
                datosArray = datosLimpio.split(",")
                
            
                price = datosArray[2].strip()
            
                description = datosArray[1].strip()
                
                size = datosArray[-4].replace("ML", "").replace("ml", "").strip().split(" ")
                
                sizeInLiters = int(size[-1]) / 1000
                
                self.writer.writerow({'Descripcion': description, 'Precio': price, 'Fecha': self.fecha_actual, 'Url': Url_img, 'Unit_size': sizeInLiters, 'ID_Producto': self.ID_Producto_URL[response.url]})
                
                