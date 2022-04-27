from DIACSV2BQ import Csv2BQ 

file_name = 'E:\\zzretail\\Scrapy\\ficheros\\Dia\\2022-03-10.csv'


csv2BQ = Csv2BQ()

Csv2BQ.read_csv(csv2BQ, file_name)

Csv2BQ.SaveOnBQ(csv2BQ)