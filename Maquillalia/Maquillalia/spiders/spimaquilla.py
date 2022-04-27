import scrapy
import csv
from datetime import date
import json
import re

class SpimaquillaSpider(scrapy.Spider):
    
    fecha_actual = date.today()
    
    file_name = open('E:\\zzretail\\Scrapy\\ficheros\\Maquillalia\\' + str(fecha_actual) + '.csv', 'w', newline='', encoding='utf-8')
    
    field_names = ['Descripcion', 'Precio', 'Fecha', 'Url', 'Unit_size', 'ID_Producto']
    
    writer = csv.DictWriter(file_name, fieldnames=field_names,delimiter='#')
    
    writer.writeheader()
    
    name = 'spimaquilla'
    allowed_domains = ['maquillalia.com']
    start_urls = ['https://www.maquillalia.com/agrado-champu-uso-frecuente-para-cabellos-grasos-750ml-p-63143.html',
                  'https://www.maquillalia.com/agrado-mascarilla-capilar-reparadora-brillo-intenso-p-63079.html',
                  'https://www.maquillalia.com/agrado-keratina-mascarilla-capilar-p-63060.html',
                  'https://www.maquillalia.com/agrado-keratina-crema-suavizante-acondicionadora-p-63065.html',
                  'https://www.maquillalia.com/agrado-champu-uso-frecuente-para-cabellos-finos-750ml-p-63142.html',
                  'https://www.maquillalia.com/agrado-colonia-fresca-gotas-de-agrado-p-62767.html',
                  'https://www.maquillalia.com/agrado-acondicionador-bifasico-p-63053.html',
                  'https://www.maquillalia.com/agrado-kids-locion-solar-spf50-p-62732.html',
                  'https://www.maquillalia.com/agrado-agua-micelar-desmaquillante-400-ml-p-62753.html',
                  'https://www.maquillalia.com/agrado-kids-bruma-seca-solar-spf50-p-62733.html',
                  'https://www.maquillalia.com/agrado-geles-del-mundo-gel-de-bano-ducha-tropical-p-63327.html',
                  'https://www.maquillalia.com/agrado-after-sun-hidrocalmante-p-62752.html',
                  'https://www.maquillalia.com/agrado-spray-texturizador-ondas-surferas-p-62770.html',
                  'https://www.maquillalia.com/agrado-jabon-intimo-p-63239.html',
                  'https://www.maquillalia.com/agrado-enjuague-bucal-menta-p-62758.html',
                  'https://www.maquillalia.com/agrado-enjuague-bucal-dientes-blancos-p-62757.html',
                  'https://www.maquillalia.com/agrado-tonico-facial-p-62755.html',
                  'https://www.maquillalia.com/agrado-crema-suavizante-acondicionadora-cabellos-fragiles-sensibles-p-63055.html',
                  'https://www.maquillalia.com/agrado-crema-suavizante-acondicionadora-cabellos-normales-grasos-p-63058.html',
                  'https://www.maquillalia.com/agrado-champu-profesional-reparador-nutritivo-750ml-p-63147.html',
                  'https://www.maquillalia.com/agrado-quitaesmalte-hidratante-p-62764.html',
                  'https://www.maquillalia.com/agrado-keratina-champu-profesional-750ml-p-63081.html',
                  'https://www.maquillalia.com/agrado-crema-solar-spf50-p-62666.html',
                  'https://www.maquillalia.com/agrado-champu-profesional-brillo-intenso-900ml-p-63144.html',
                  'https://www.maquillalia.com/agrado-champu-profesional-nutricion-cabellos-secos-900ml-p-63212.html',
                  'https://www.maquillalia.com/agrado-crema-hidratante-mini-go-rosa-mosqueta-p-63321.html',
                  'https://www.maquillalia.com/agrado-aceite-acelerador-del-bronceado-spf20-p-62717.html',
                  'https://www.maquillalia.com/agrado-geles-del-mundo-gel-de-bano-ducha-mediterraneo-p-63326.html',
                  'https://www.maquillalia.com/agrado-bruma-seca-solar-spf30-p-62730.html',
                  'https://www.maquillalia.com/agrado-kids-bruma-seca-solar-spf50-p-62733.html',
                  'https://www.maquillalia.com/agrado-trendy-bubbles-gel-de-bano-ducha-aqua-blue-p-63344.html',
                  'https://www.maquillalia.com/agrado-agua-micelar-desmaquillante-250-ml-p-62754.html',
                  'https://www.maquillalia.com/agrado-agua-de-colonia-fresca-p-62765.html',
                  'https://www.maquillalia.com/agrado-jabon-de-manos-dermo-papaya-p-63243.html',
                  'https://www.maquillalia.com/agrado-jabon-de-manos-dermo-coco-p-63278.html',
                  'https://www.maquillalia.com/agrado-leche-corporal-rosa-mosqueta-p-63234.html',
                  #'https://www.maquillalia.com/search.php?buscar=Agrado+-+Desodorante+roll-on+Aloe+Vera',
                  'https://www.maquillalia.com/agrado-aceite-corporal-coco-p-63233.html',
                  'https://www.maquillalia.com/agrado-leche-limpiadora-p-62756.html',
                  'https://www.maquillalia.com/agrado-colorterapia-champu-profesional-p-63082.html',
                  'https://www.maquillalia.com/agrado-colorterapia-crema-suavizante-acondicionadora-profesional-p-63076.html',
                  'https://www.maquillalia.com/agrado-acondicionador-profesional-reparador-brillo-intenso-p-63078.html',
                  'https://www.maquillalia.com/agrado-crema-solar-spf30-p-62657.html',
                  'https://www.maquillalia.com/agrado-trendy-bubbles-jabon-de-manos-melon-fresco-p-63283.html',
                  'https://www.maquillalia.com/agrado-leche-corporal-coco-p-63238.html',
                  'https://www.maquillalia.com/agrado-after-sun-aloe-vera-p-62751.html',
                  'https://www.maquillalia.com/agrado-aceite-acelerador-del-bronceado-spf8-p-62669.html',
                  'https://www.maquillalia.com/agrado-trendy-bubbles-gel-de-bano-ducha-coco-loco-p-63342.html',
                  'https://www.maquillalia.com/agrado-gel-de-bano-ducha-sales-marinas-p-63351.html',
                  'https://www.maquillalia.com/agrado-gel-champu-uso-frecuente-familiar-1250ml-p-62652.html',
                  'https://www.maquillalia.com/agrado-champu-profesional-brillo-intenso-750ml-p-63146.html',
                  'https://www.maquillalia.com/agrado-crema-solar-spf50-p-62666.html'
                  ]
    
    ID_Producto_URL = {'https://www.maquillalia.com/agrado-champu-uso-frecuente-para-cabellos-grasos-750ml-p-63143.html' : 'BPTM00005972',
                       'https://www.maquillalia.com/agrado-mascarilla-capilar-reparadora-brillo-intenso-p-63079.html' : 'BPTM00005506',
                       'https://www.maquillalia.com/agrado-keratina-mascarilla-capilar-p-63060.html' : 'BPTM00005504',
                       'https://www.maquillalia.com/agrado-keratina-crema-suavizante-acondicionadora-p-63065.html' : 'BPTM00004907',
                       'https://www.maquillalia.com/agrado-champu-uso-frecuente-para-cabellos-finos-750ml-p-63142.html' : 'BPTM00005971',
                       'https://www.maquillalia.com/agrado-colonia-fresca-gotas-de-agrado-p-62767.html' : 'BPTM00004896',
                       'https://www.maquillalia.com/agrado-acondicionador-bifasico-p-63053.html' : 'BPTM00004826',
                       'https://www.maquillalia.com/agrado-kids-locion-solar-spf50-p-62732.html' : 'BPTM00007312',
                       'https://www.maquillalia.com/agrado-agua-micelar-desmaquillante-400-ml-p-62753.html' : 'BPTM00006282',
                       'https://www.maquillalia.com/agrado-kids-bruma-seca-solar-spf50-p-62733.html' : 'BPTM00006223',
                       'https://www.maquillalia.com/agrado-geles-del-mundo-gel-de-bano-ducha-tropical-p-63327.html' : 'BPTM00006180',
                       'https://www.maquillalia.com/agrado-after-sun-hidrocalmante-p-62752.html' : 'BPTM00006079',
                       'https://www.maquillalia.com/agrado-spray-texturizador-ondas-surferas-p-62770.html' : 'BPTM00005997',
                       'https://www.maquillalia.com/agrado-jabon-intimo-p-63239.html' : 'BPTM00005769',
                       'https://www.maquillalia.com/agrado-enjuague-bucal-menta-p-62758.html' : 'BPTM00005284',
                       'https://www.maquillalia.com/agrado-enjuague-bucal-dientes-blancos-p-62757.html' : 'BPTM00005283',
                       'https://www.maquillalia.com/agrado-tonico-facial-p-62755.html' : 'BPTM00004904',
                       'https://www.maquillalia.com/agrado-crema-suavizante-acondicionadora-cabellos-fragiles-sensibles-p-63055.html' : 'BPTM00004887',
                       'https://www.maquillalia.com/agrado-crema-suavizante-acondicionadora-cabellos-normales-grasos-p-63058.html' : 'BPTM00004886',
                       'https://www.maquillalia.com/agrado-champu-profesional-reparador-nutritivo-750ml-p-63147.html' : 'BPTM00004882',
                       'https://www.maquillalia.com/agrado-quitaesmalte-hidratante-p-62764.html' : 'BPTM00004878',
                       'https://www.maquillalia.com/agrado-keratina-champu-profesional-750ml-p-63081.html' : 'BPTM00004828',
                       'https://www.maquillalia.com/agrado-crema-solar-spf50-p-62666.html' : 'BPTM00007312',
                       'https://www.maquillalia.com/agrado-champu-profesional-brillo-intenso-900ml-p-63144.html' : 'BPTM00006327',
                       'https://www.maquillalia.com/agrado-champu-profesional-nutricion-cabellos-secos-900ml-p-63212.html' : 'BPTM00006326',
                       'https://www.maquillalia.com/agrado-crema-hidratante-mini-go-rosa-mosqueta-p-63321.html' : 'BPTM00006248',
                       'https://www.maquillalia.com/agrado-aceite-acelerador-del-bronceado-spf20-p-62717.html' : 'BPTM00006220',
                       'https://www.maquillalia.com/agrado-geles-del-mundo-gel-de-bano-ducha-mediterraneo-p-63326.html' : 'BPTM00006177',
                       'https://www.maquillalia.com/agrado-bruma-seca-solar-spf30-p-62730.html' : 'BPTM00006077',
                       'https://www.maquillalia.com/agrado-kids-bruma-seca-solar-spf50-p-62733.html' : 'BPTM00006223',
                       'https://www.maquillalia.com/agrado-trendy-bubbles-gel-de-bano-ducha-aqua-blue-p-63344.html' : 'BPTM00006050',
                       'https://www.maquillalia.com/agrado-agua-micelar-desmaquillante-250-ml-p-62754.html' : 'BPTM00006030',
                       'https://www.maquillalia.com/agrado-agua-de-colonia-fresca-p-62765.html' : 'BPTM00005973',
                       'https://www.maquillalia.com/agrado-jabon-de-manos-dermo-papaya-p-63243.html' : 'BPTM00005785',
                       'https://www.maquillalia.com/agrado-jabon-de-manos-dermo-coco-p-63278.html' : 'BPTM00005779',
                       'https://www.maquillalia.com/agrado-leche-corporal-rosa-mosqueta-p-63234.html' : 'BPTM00005671',
                       #'https://www.maquillalia.com/search.php?buscar=Agrado+-+Desodorante+roll-on+Aloe+Vera',
                       'https://www.maquillalia.com/agrado-aceite-corporal-coco-p-63233.html' : 'BPTM00008451',
                       'https://www.maquillalia.com/agrado-leche-limpiadora-p-62756.html' : 'BPTM00004903',
                       'https://www.maquillalia.com/agrado-colorterapia-champu-profesional-p-63082.html' : 'BPTM00008262',
                       'https://www.maquillalia.com/agrado-colorterapia-crema-suavizante-acondicionadora-profesional-p-63076.html' : 'BPTM00008261',
                       'https://www.maquillalia.com/agrado-acondicionador-profesional-reparador-brillo-intenso-p-63078.html' : 'BPTM00006726',
                       'https://www.maquillalia.com/agrado-crema-solar-spf30-p-62657.html' : 'BPTM00006556',
                       'https://www.maquillalia.com/agrado-trendy-bubbles-jabon-de-manos-melon-fresco-p-63283.html' : 'BPTM00006280',
                       'https://www.maquillalia.com/agrado-leche-corporal-coco-p-63238.html' : 'BPTM00006225',
                       'https://www.maquillalia.com/agrado-after-sun-aloe-vera-p-62751.html' : 'BPTM00006224',
                       'https://www.maquillalia.com/agrado-aceite-acelerador-del-bronceado-spf8-p-62669.html' : 'BPTM00006222',
                       'https://www.maquillalia.com/agrado-trendy-bubbles-gel-de-bano-ducha-coco-loco-p-63342.html' : 'BPTM00006105',
                       'https://www.maquillalia.com/agrado-gel-de-bano-ducha-sales-marinas-p-63351.html' : 'BPTM00004901',
                       'https://www.maquillalia.com/agrado-gel-champu-uso-frecuente-familiar-1250ml-p-62652.html' : 'BPTM00004890',
                       'https://www.maquillalia.com/agrado-champu-profesional-brillo-intenso-750ml-p-63146.html' : 'BPTM00004883',
                       'https://www.maquillalia.com/agrado-crema-solar-spf50-p-62666.html' : 'BPTM00007312'
                       }
    
    
    def parse(self, response):
        
        for sel in response.xpath('//script[@type="application/ld+json"]'):
            script = sel.xpath('text()').get(default='not-found')
            print('-------------------')
            if script.find("\"offers\": [") == -1:
                print('not-found')
            else:
                print('yes-found')
                json_datos = json.loads(re.sub('\'','\"',script))
                print(json_datos)
                offerString = re.sub('\'','\"',str(json_datos["offers"][0]))
                print(offerString)
                offers = json.loads(offerString)
                size = (response.xpath('//span[@class="prdct-unit"]/text()').extract_first()).replace("Contenido:", "").replace("ml", "").replace(" ", "")
                sizeINlitters = float(size) / 1000
                self.writer.writerow({'Descripcion': json_datos['name'][0], 'Precio': offers['price'], 'Fecha': self.fecha_actual, 'Url': json_datos['image'][0], 'Unit_size': sizeINlitters, 'ID_Producto': self.ID_Producto_URL[response.url]})
       
