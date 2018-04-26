from telegram.ext import Updater,CommandHandler,ConversationHandler,Filters,MessageHandler
import store_bot
import re
import random
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
sheet = client.open("Dia_database").sheet1

#################################


PELICULA, END,INICIO=range(3)


def buscaprecios(bot,mensaje,el_id):
	print('estamos')
	print(mensaje.message.text)
	productos=mensaje.message.text.split(',')
	print('estamos'+str(productos))
	productos=[x.strip() for x in productos]
	print('estamos2'+str(productos))
	try:
		for p in productos:
			criteria_re = re.compile(".*\\b"+p+"\\b.*",re.IGNORECASE)
			cell_list = sheet.findall(criteria_re)
			print(cell_list)
			if(len(cell_list)==0):
				print('not found')
				bot.sendMessage(chat_id=el_id,text='No se ha encontrado el producto '+p)
				
			else:

				producto_ele=cell_list[random.randint(0,(len(cell_list)-1))]
				print(producto_ele)
				nombre=producto_ele.value
				fila=producto_ele.row
				print(fila)
				datos=sheet.range(int(fila),2,int(fila),4)
				datos=[x.value for x in datos]
				print(datos,el_id)
				bot.sendMessage(chat_id=el_id,text=nombre+'\n'+datos[0]+'\n'+datos[1]+'\n'+datos[2])
				print(datos)
	except Exception as e:
		raise e
	
	return INICIO


def inicio(bot, update):
	if not store_bot.user_exists(update):
		bot.sendMessage(chat_id=update.message.chat.id,text='Hola {}, introduce la lista de la compra, separando los productos por comas'.format(update.message.chat.first_name))
		mensaje_recibido=update.message.text
		print(mensaje_recibido)
		print(update)
		#buscaprecios(mensaje_recibido)
		return PELICULA
	else:
		bot.sendMessage(chat_id=update.message.chat.id,text='Introduce la lista de la compra, separando los productos por comas, o bien un solo producto')
		return END


def pelicula(bot,update):
	buscaprecios(bot,update,update.message.chat.id)
	bot.sendMessage(chat_id=update.message.chat.id,text='Gracias, si necesitas algo mas escribe \n /inicio')
	#print(update.message.text)
	return ConversationHandler.END


def end(bot,update):
	bot.sendMessage(chat_id=update.message.chat.id,text='hasta otra')
	return ConversationHandler.END

def cancel(bot,update):
	bot.sendMessage(chat_id=update.message.chat.id,text='hasta otra')
	return ConversationHandler.END

def main():
	update=Updater()#Poner aqui el codigo:hash del bot
	conversacion=ConversationHandler(entry_points=[CommandHandler('inicio',inicio)],
		states={PELICULA:[MessageHandler(Filters.text, pelicula)], INICIO:[MessageHandler(Filters.text, inicio)],
		END:[MessageHandler(Filters.text, end)] }, 
		fallbacks=[CommandHandler('cancelar',cancel)])
	update.dispatcher.add_handler(conversacion)#CommandHandler('inicio',inicio))
	update.start_polling()
	update.idle()

if __name__ == '__main__':
	main()