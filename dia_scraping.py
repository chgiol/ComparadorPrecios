from lxml import html
import requests
import time
from random import randint
################CREDS Y OPEN DE LA SHEET#################
import gspread
from oauth2client.service_account import ServiceAccountCredentials
 
 
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
 
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Dia_database").sheet1 #Cambiar el nombre al de la sheet correspondiente

#################################
num_prods=0
for i in range(1):#Insertar el numero de paginas de productos maximo que se encuentran a partir del link inferior
	page = requests.get('https://www.dia.es/compra-online/productos/frescos/c/WEB.001.000.00000?q=%3Arelevance&page='+str(i))
	tree = html.fromstring(page.content)
	#print(page.content)

	productos = tree.xpath('//span[@class="details"]/text()')
	#precios sin descuentos
	#precios= tree.xpath('//p[@class="price"]/text()')
	#precioskilo=tree.xpath('//p[@class="pricePerKilogram"]/text()')
	precios= tree.xpath('//p[@class="price"]/s/text()')
	precioskilo=tree.xpath('//p[@class="pricePerKilogram"]/s/text()')
	

#usar .items() para saber los items del objeto y .get() para obtenerlos
	links=tree.xpath('//span[@class = "thumb"]/img')
	lins=[l.get('data-original') for l in links]
	links=lins
	x=[p[-6:].rstrip() for p in precios]
	precios=x
	x=[p.rstrip() for p in precioskilo]
	precioskilo=x
	x=[p[6:].rstrip() for p in productos]
	productos=x

	cosas=zip(productos,precios,precioskilo,links)

	num_prods+=len(productos)
	for prod,prec,pkil,img in cosas:
		print(prod,prec,pkil,img)
		sheet.append_row([prod,prec,pkil,img])
	time.sleep(5)
print()
print('TOTAL DE PRODUCTOS LISTADOS: '+str(num_prods))
