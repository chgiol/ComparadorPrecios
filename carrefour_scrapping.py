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
sheet2 = client.open("Dia_database").get_worksheet(1)#abre la sheet 2 (indices empiezan por 0)

#################################
num_prods=0
for i in range(1):
	page = requests.get('https://www.carrefour.es/supermercado/')
	tree = html.fromstring(page.content)
	links_categorias=tree.xpath('//li[@class="level2-item"]/a')
	links_categorias=[a.get('href') for a in links_categorias]
	print(links_categorias)#añadir davant  https://www.carrefour.es/supermercado/------>/supermercado/perfumeria-e-higiene/cosmetica/N-16keur/c;jsessionid=iAgmIsvqzptvv3d7LvEOlCAY.sf2_5
print('\n\n TENEMOS las categorias \n\n\n')
primera_vez=True
for i in links_categorias[1:2]:
	print()
	print()
	print()
	print(' vamos a  obtener de '+i)
	print()
	print()
	pagina=requests.get('https://www.carrefour.es/supermercado'+i)
	tree=html.fromstring(pagina.content)
	links_subcategorias=tree.xpath('//ul[@class="columns"]/li/a')
	links_subcategorias=[a.get('href') for a in links_subcategorias]
	#print(links_subcategorias)---->/supermercado/el-mercado/verduras-y-hortalizas/patatas-cebollas-y-ajos/N-1cqv2v0/c;jsessionid=dlPydhBsFbS392RUboiehqc5.sf2_5
	if(primera_vez):
		print()
		print('Tiempo de espera de 40 segundos para entrar y darle a cargar siempre automaticante con este session_id')
		print()
		print('https://www.carrefour.es'+links_subcategorias[0])
		time.sleep(40)
		primera_vez=False #queda obtener  imagen precio nombre preukio/preuud