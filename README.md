# ComparadorPrecios
Proyecto para la asigtura SINF de un comparador de precios de las empresas Carrefour y Dia mediante un bot de Telegram

**Introducción.**

En este proyecto se pretende construir una herramienta que ayude al usuario a encontrar el lugar donde su lista de la compra le resulte mas barata, esto se va  realizar mediante web scrapping y un bot de telegram.

**Descripción de la solución planteada.**

Para realizar el proyecto se han realizado dos scripts que se usan para scrapear las webs del Carrefour y del Dia obteniendo fotos de los productos, nombre, precio y precio por kilo o por unidad y los resultados se introducen en una Google sheet que se usa a modo de base de datos online.
Aparte se ha desarrollado un bot de Telegram el que, al recibir una lista de la compra, devolverá aquella donde resulte mas barato comprar todos los productos, si se introduce solamente el nombre de un producto devolverá el producto encontrado en ambas tiendas.

**Metodología.**

Para el desarrollo de este proyecto se ha usado la metodología de la *school of data*, marcando hitos a cumplir dentro de un plan de trabajo. El lenguaje de desarrollo escogido ha sido *Python3* por su versatilidad.

**Resultados.**

Los resultados del proyecto son los scripts desarrollados así como dos *spreadsheets* con todos los productos de la sección de supermercado de las empresas mencionadas.

**Guía de uso.**

Debemos tener instalados en el ordenador a ejecutar los programas tanto Python 3.0 en adelante como las dependencias necesarias.

Para el scrapeo de las webs se necesita conectar dichos scripts con una cuenta de google docs done se haya habilitado el uso de la api *gspread* así como ubicarlos en una carpeta con el fichero *client_secret.json* correspondiente, los campos a modificar en el script se encuentran indicados en este. Una vez configurados se pueden ejecutar sin argumentos con el comando **python *nombre_del sript* **

Para el bot de Telegram, la variable *update* de la función *main()* debe asignarse al codigo que al registrar el bot con el chat de BotFather de telegram este nos indicará. También deben configurarse las credenciales de acceso a las *spreadsheets* como se indica en el script. Mencionar que se debe ubicar el script del bot en el mismo lugar donde se encuentre el archivo *client_secret.json* de la api *gspread*


El contenido de este repositorio está sujeto a la licencia GNU General Public License v3.0 :computer:
