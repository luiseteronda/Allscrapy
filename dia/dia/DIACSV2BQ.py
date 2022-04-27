from google.cloud import bigquery

import pandas as pd



class DiaCsv2BQ:

    producto = []


    def read_csv(self, filename):
        self.producto = pd.read_csv(filename, delimiter='#').to_dict()
            
    def SaveOnBQ(self, Distributor):
        
        rows_to_insert = []
        
        for i in range(0,len(self.producto.get('Descripcion'))):
            row_to_insert = {"Distributor": Distributor, "ID_PRODUCT": (i+18), "ImageURL": self.producto.get('Url')[i], "Description": self.producto.get('Descripcion')[i], "Price":self.producto.get('Precio')[i], "Volume": self.producto.get('Unit_size')[i], "Date": self.producto.get('Fecha')[i]}
            
            rows_to_insert.append(row_to_insert)

        client = bigquery.Client()

        Table_ID = "pricingproofofconcept.PricingDate.Pricesdef"

        errors = client.insert_rows_json(Table_ID, rows_to_insert)  

        if errors == []:
            print(f"New rows has been added.{i}")
        else:
            print("enconter errors []",format(errors))