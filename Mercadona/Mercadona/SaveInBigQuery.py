
from google.cloud import bigquery

import pandas as pd

class Csv2BQ:

    producto = []
    
    
    def read_csv(self, filename):
        
        self.producto = pd.read_csv(filename, delimiter='#').to_dict()
        
        
    def SaveOnBQ(self, Distributor):
        
        rows_to_insert = []
        print(self.producto.get('Unit_size'))
        for i in range(0,len(self.producto.get('Descripcion'))):
            print('------------------------')
            print(self.producto.get('Unit_size')[i])
            print('-----------------------')
            if  str(self.producto.get('Unit_size')[i]) != "nan":
                print("Por aquí")
                row_to_insert = {"Distributor": Distributor, "ImageURL": self.producto.get('Url')[i], "Description": self.producto.get('Descripcion')[i], "Price": self.producto.get('Precio')[i], "Volume": self.producto.get('Unit_size')[i], "Date": self.producto.get('Fecha')[i], "Price_volume": self.producto.get('Precio')[i]/self.producto.get('Unit_size')[i], "ID_PRODUCT": self.producto.get('ID_Producto')[i]}
            else:
                print("Por allá")
                row_to_insert = {"Distributor": Distributor, "ImageURL": self.producto.get('Url')[i], "Description": self.producto.get('Descripcion')[i], "Price": self.producto.get('Precio')[i], "Date": self.producto.get('Fecha')[i], "ID_PRODUCT": self.producto.get('ID_Producto')[i]}
            rows_to_insert.append(row_to_insert)

        client = bigquery.Client()

        Table_ID = "pricingproofofconcept.PricingDate.PRICES"

        errors = client.insert_rows_json(Table_ID, rows_to_insert)  
        

        if errors == []:
            print(f"New rows has been added.{i}")
        else:
            print("enconter errors []",format(errors))


    

        
    