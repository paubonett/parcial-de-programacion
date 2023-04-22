admin=['adminsap','admin123']
cajeros=[['cajeand','sharon123', 'Sharon Andreina', '1092387960'],['cajeang','angel123', 'Angel Daniel', '1093293435'], ['cajealj', 'paula123', 'Paula', '1090371768']]
usu=[]


def imprimir_menu_comidas(menu_comidas):
    for submenu in menu_comidas:
        for texto in submenu:
            print(texto)
        print()

def imprimir_menu_cocteles(menu_cocteles):
    for submenu in menu_cocteles:
        for texto in submenu:
            print(texto)
        print()

Carnes_Angus_Beef = [['TOMAHWK BEEF', ['-Corte de 1000 gr -Guarnición papa -Yuca al vapor -Cascos de papa -Papas a la francesa -Ensalada pico e’ gallo'], ['Precio $299000']] , ['RIBEYE BEEF', ['-Corte de 400 gr -Papa al vapor -Yuca al vapor -Ensalada pico e’ gallo'], ['Precio $139000']] , ['PICANHA ANGUS BEEF', ['-Corte de 400 gr -Guarnición papa -Yuca al vapor -Cascos de papa -Papas a la francesa -Ensalada pico e’ gallo'], ['Precio $119000']] , ['NEW YORK STEAK BEEF', ['-Lomo Ancho de 400 gr -Guarnición papa -Yuca al vapor -Cascos de papa -Ensalada pico e’ gallo'], ['Precio $129000']], ['ASADO DE TIRA BEEF', ['-Corte de 400 gr'], ['Precio $119000']], ['BIFE DE VACIO BEEF', ['-Pieza de 400 gr'], ['Precio $139000']]]                                                                      
Entradas = [['NACHOS DAKOTA' ,['-Nachos crocantes -Carne al estilo tex-mex -Queso cheddar americano -Guacamole -Pico e ‘gallo -Frijol refrito'], ['Precio $29000']], ['SAUSAGE OLD WEST ', ['-4 chorizos de ternera -Salsa de whisky Jack Daniel’s -Papas a la francesa'], ['Precio $29000']] , [ 'PAPAS WEST SIDE', ['-Papas a la francesa -Queso cheddar -Chorizo de ternera -Tocineta crunchy'], ['Precio $30000']] , [ 'MAZORQUITAS' ,['-3 Mazorquitas al grill -Cubierta de queso paisa'], ['Precio $21000']] ,  [ 'CAMARONES FORT HAYS',  ['-14 camarones apanados -Guacamole -Dip de tártara -Pimentón rostizado'], ['Precio $32000']] , [ 'MAICITOS' , ['-Maíz dulce -Pollo al grill -Tocineta -Gratinado en queso doble crema y parmesano'], ['Precio $34000']], [ 'ALITAS RANGER', ['-12 piezas de alas -Salsa bbq -Miel -Mostaza -Picantes con papas a la francesa'], ['Precio $34000']]]
Carnes_Uruguayas_Argentinas = [['TOMAHAWK URUGUAYO' , ['-Corte de 1000 gr -Guarnición de papa -Yuca al vapor -Ensalada pico e’ gallo'], ['Precio $ 190000']] , ['CHULETON ARGENTINO', ['-Ojo de bife con hueso de 800 gr -Guarnición de papa -Yuca al vapor -Ensalada pico e’ gallo'], ['Precio $ 170000']] , ['PORTER HOUSE ARGENTINO', ['-Corte de 800 gr -Guarnición de papa -Yuca al vapor -Ensalada pico e’ gallo'], ['Precio $160000']] , ['BEEF CHORIZO ARGENTINO', ['-Bife angosto de 600 gr -Guarnición de papa -Yuca al vapor -Ensalada pico e’ gallo'], ['Precio $130000']]]
Carnes_Nacionales=[['PICANHA BACON RANCH', ['-Res al grill de 400 gr -Salsa Jack Daniel’s -Guarnición de papa -Yuca al vapor -Ensalada pico e’ gallo'], ['Precio $64000']], ['PICANHA', ['-Res al grill de 400 gr -Guarnición de papa -Yuca al vapor -Ensalada pico e’ gallo'], ['Precio $62000']], ['CHURRASCO',['-Lomo ancho en corte mariposa de 400 gr -Guarnición papa -Yuca al vapor -Ensalada pico e gallo'], ['Precio $56000' ]], ['BABY BEEF CORN', ['-Lomo Fino de 330 gr -Salsa De Tocineta -Maíz Dulce -Queso Parmesano -Guarnición De Pure De Papa -Mix De Lechugas'], ['Precio $49000']], ['BABY BEEF WESTERN', ['-Lomo Fino de 330 gr -Salsa de champiñones -Guarnición de pure de papa -Mix de lechugas'], ['Precio $46000']], ['BABY BEEF REEWARD', ['-Lomo Fino de 330 gr -Guarnición de papa -Yuca al vapor -Mix de lechugas'], ['Precio $46000']]]
Cerdo=[['CHICARRON', ['-400 gr de Chicharrón Crocante -Guarnición papa -Yuca al vapor -Chimichurri -Rodajas de limón'], ['Precio $46000']], ['RIBS JACK DANIEL’S', ['-400 gr de costillas de cerdo -Salsa de bbq -Salsa Jack Daniel’s -Guarnición de papas a la francesa -Mix de lechugas'], ['Precio $52000']], ['COSTILLITAS', ['-400 gr de costillitas de cerdo -Salsa bbq -Miel mostaza guarnición -Papas a la francesa -Mix de lechugas'], ['Precio $49000']], ['LOMO DE CERDO', ['Lomo de Cerdo de 330 gr -Salsa bbq -Guarnición de papas a la francesa -Mix de lechugas'], ['Precio $44000']]]
Hamburguesas=[['ANGUS BURGUER', ['-Carne Angus de 300 gr -Pan brioche -Queso americano -Tocineta -Vegetales en finas hiervas -Cebolla caramelizada -Pepinillos'], ['Precio $49000']], ['JACK DANIELS', ['-Pan brioche -150 gr de carne de res -Salsa Jack Daniels -Chorizo de ternera -Queso cheddar -70gr tocineta ahumada -Tomate horneado -Cebolla caramelizada en vino tinto -Lechuga fresca'], ['Precio $28000']], ['SHERIFF', ['-150 gr de carne de res -120 gr de pullet pork -Pan baguette semi dulce -Salsa showyn -Colslaw -Queso Colby Jack'], ['Precio $28000']], ['LAS VEGAS', ['-150 gr de carne de res -80 gr de brisket ahumado -Pan artesanal -Macarrón cheese -Vegetales frescos'], ['Precio $28000']], ['EL PRIMO CARIM MUSTAFÁ', ['-300 gr de carne de res doble -Pan brioche -Tocineta -Queso monster -Vegetales frescos -Pepinillos -Salsa de tomate heinz -Mayonesa kraft -Mostaza heinz'], ['Precio $33000']], ['HARLEY DAVIDSON', ['-300 gr carne de res triple -Pan brioche -Vegetales frescos -Tocineta -Pepinillo -Queso cheddar -Salsa tártara y showy'], ['Precio $30000']], ['TÍO SAM', ['-100 gr de lomo de cerdo -100 gr de pechuga -150 gr de carne de res -Pan brioche -Tocineta ahumada -Queso cheddar -Vegetales frescos'], ['Precio $32000']], ['LA ROCKERA', ['-150 gr de carne de res -80 gr de brisket ahumado -Pan brioche -Queso pepperjack -Lechuga Batavia -Cebolla morada -Pepinillos'], ['Precio $29000']], ['CLUB HOUSE', ['-160 gr de dip de pollo -150 gr de tocineta -2 huevos -Queso doble crema -Queso chédar americano'], ['Precio $35000']]]
Brochetas=[['BROCHETA BUFFALO BILL', ['-2 brochetas de lomo de res con 200 gr c/u -Guarnición de papas a la francesa'], ['Precio $49000']], ['BROCHETA APACHE', ['-2 brochetas de 200 gr c/u de pechuga al grill -Guarnición de papas a la francesa'], ['Precio $42000']], ['BROCHETA LEGENS', ['-Brocheta de lomo de res de 200 gr -Brocheta de 200 gr de pechuga al grill -Guarnición de papas a la francesa'], ['Precio $49000']]]
Pollos=[['MUSHROOM CHICKEN', ['-330 gr de pechuga al grill -Salsa de champiñones -Guarnición de puré de papa -Mix de lechugas'], ['Precio $39000']], ['CORN GRILLED CHICKEN', ['-330 gr de pechuga al grill -Salsa de maíz -Tocineta -Queso parmesano -Guarnición de puré de papa -Mix de lechugas'], ['Precio $39000']], ['GRILLED CHICKEN', ['-330 gr de pechuga al grill -Guarnición papas a la francesa -Papa al vapor -Yuca al vapor -Mix de lechugas'], ['Precio $37000']]]
Pastas=[['CAMARONERA', ['-250 gr de camarones -Salsa de mostaza dijon -Vino blanco -Pan focaccia -Pasta de fettuccine'], ['Precio $49000']], ['MUSHROOM', ['-200 gr de lomo fino al grill -Fettuccini -Salsa de champiñón -Pan focaccia'], ['Precio $49000']], ['CARBONARA SWEET CORN', ['-230 gr pechuga al grill -Maíz dulce -Tocineta -Pasta fettuccine -Pan focaccia'], ['Precio $47000']]]
Para_Compartir=[['PICADA OLD WEST', ['-450 gr de pechuga al grill -330 gr de lomo de cerdo -200 gr de lomo fino -2 chorizos de ternera -Ensalada pico e’ gallo -Papas a la francesa -Papa al vapor -Cascos de papa -Yuca al vapor -Queso paisa en cubos'], ['Precio $109000']], ['WILD WEST', ['-400 gr de costillitas de cerdo -Salsa bbq -300 gr de chicharrón crujiente -300 gr de brisket de res ahumado -12 alitas -Salsa bbq -3 mazorquitas -Queso paisa -Macarrón cheese -Papa al vapor -Crotones de tocineta -Mix de lechuga'], ['Precio $119000']]]
Ensaladas=[['ENSALADA LUSIANA', ['-350 gr pollo crispy o al grill -50 gr tocineta ahumada -Mix de lechugas tomate Cherry -Queso parmesano -Crotones de pan -Aderezo de la casa -Reducción de vinagre balsámico'], ['Precio $34000']], ['ENSALADA DE CAMARONES', ['-300 gr de camarones al crispy -Mix de lechugas -Tomates Cherry -Crotones de pan -Queso parmesano -Aderezo de la casa -Reducción de vinagre balsámico'], ['Precio $36000']]]
Menu_Infantil_Postres=[['VAQUERITOS BURGUER', ['-Pan brioche -150 gr de carne molida de res -Tocineta -Queso cheddar americano -Papas a la francesa -Juguete infantil'], ['Precio $32000']], ['CHEROKEE CHICKEN', ['-250 gr de pollo apanado -Guarnición de papas a la francesa -Juguete infantil'], ['Precio $32000']], ['TORTA DE CHOCOLATE', ['Precio $12000']], ['LINGOTE DE ORO', ['-Barra de chocolate -Azúcar dorada -Licor dulce -Ganache de frutos secos -Helado artesanal'], ['Precio $19000']]]


Cocteles_de_Autor=[['TORO SENTADO', ['-Whisky Red label -Licor de café -Vino embajador -Cerveza club negral -Piña -Naranja'], ['Precio $28000']], ['BILLY THE KID', ['-Jack Daniels Honey  -Jaguermeister -Crema de coco'], ['Precio $32000']], ['CALIBRE 38', ['-Whisky Jack Daniel No 7 -Limon -Syrop de frutos rojos -Syrop simple -Ginger'], ['Precio $32000']], ['BONNIE & CLYDE', ['-Ron de coco -Jägermeister -Syrop frutos amarillos -Shrup de piña -Jarabe de genjibre -Limón'], ['Precio $32000']], ['JHON WESLY', ['-Tequila Reposado -Ron coco -Syrop de maracuya -Shrup de piña -Ginger'], ['Precio $30000']], ['JESSE JAMES', ['-Ron blanco -Curacao azul -Syrop de piña -Syrop de maracuya -Ginger'], ['Precio $30000']], ['SE BUSCA', ['-Vodka -Limón -Syrop de lychhe -Vino Rosado lambrusco -Syrop de frutos rojos'], ['Precio $32000']], ['INMORTAL JACK', ['-Jack Daniel No 7 Botellita -Licor de melon -Jarabe de jengibre -Zumo de  limon -Licor de durazno -Jägermeister'], ['Precio $34000']], ['GIN CAKTUS', ['-Ginebra -Infusión de pepino -Tonica nacional'], ['Precio $30000']]]
Bebidas_Especiales=[['SODAS', ['-Frutos amarillos -Frutos rojos'], ['Precio $10000']], ['SODAS 2', ['-Frutos Azules'], ['Precio $12000']], ['LIMONADAS', ['-Limonada Cerezada -Coco Limonada -Limonada Hierba Buena'], ['Precio $11000']], ['LIMONADA DE ROSAS', ['Precio $24000']], ['FRAPPES', ['-Naranja -Maracuyá -Limón'], ['Precio $9000']]]
Bebidas=[['AGUA', ['Precio $5000']], ['COCA-COLA PET 400ML', ['Precio $6000']], ['COCA-COLA ZERO PET 400ML', ['Precio $6000']], ['GASEOSAS QUATRO - KOLA ROMAN', ['Precio $5000']], ['GINGER - SODA', ['Precio $6000']], ['REDBULL', ['Precio $10000']]]
Cervezas_Importadas=[['ERDINGER WEISSBIER', ['Precio $32000']], ['ERDINGER DUNKEL', ['Precio $32000']], ['ERDINGER PIKANTUS', ['Precio $38000']], ['TROOPER BEER IRON MAIDEN', ['Precio $32000']], ['CERVEZA ACDC', ['Precio $32000']], ['BUDWEISER 250ML', ['Precio $8000']], ['HEINEKEN', ['Precio $10000']], ['CORONA', ['Precio $12000']], ['SMIRNOFF ICE 275ML', ['Precio $15000']], ['SMIRNOFF ICE 275ML APPLE', ['Precio $15000']]]
Cervezas=[['CERVEZA ARTESANAL OLDWEST', ['Precio $10000']], ['CERVEZA AGUILA', ['Precio $7000']], ['CERVEZA AGUILA LIGHT', ['Precio $7000']], ['CERVEZA POKER', ['Precio $7000']], ['CERVEZA CLUB COLOMBIA', ['-Roja -Negra -Dorada -Doble Malta'], ['Precio $8000']]]
Sangrias=[['JARRA ROSADA', ['-Fresas -Hierba Buena -Cereza -Uvas Isabelina'], ['Precio $110000']], ['JARRA AZUL', ['-Fresas -Arandanos -Uva Isabelina -Lycehes'], ['Precio $110000']], ['JARRA TINTO', ['-Fresas -Uvas -Naranja -Cereza -Uva Isabelina'], ['Precio $110000']], ['COPA DE SANGRÍA', ['Precio $30000']]]
Whisky=[['CREMA DE WHISKY - BAILEYS 375 ML', ['Precio $80000']], ['CREMA DE WHISKY - BAILEYS 700 ML', ['Precio $130000']], ['BLACK Y WHITE', ['Precio $120000']], ['BUCHANANS 12 AÑOS 375 ML', ['Precio $175000']], ['BUCHANANS 12 AÑOS 750 ML DELUXE', ['Precio $250000']], ['BUCHANANS 18 AÑOS 750 ML', ['Precio $470000']], ['BUCHANNAS MASTER 750 ML', ['Precio $320000']], ['MINI JACK DANIELS 50 ML', ['Precio $25000']], ['JACK DANIELS 375ML', ['Precio $160000']], ['JACK DANIEL’S TENNESSE 750 ML', ['Precio $280000']], ['JACK DANIEL’S HONEY 750 ML', ['Precio $280000']], ['JACK DANIEL’S TENNESSE FIRE 750 ML', ['Precio $280000']], ['JHONNIE WALKER RED LABEL 750 ML', ['Precio $150000']], ['JHONNIE WALKER BLACK LABEL 750 ML', ['Precio $240000']], ['MACALLAN 12 DOUBLE CASK 700 ML', ['Precio $600000']], ['OLD PARR 12 AÑOS 500 ML', ['Precio $180000']], ['OLD PARR 12 AÑOS 750 ML', ['Precio $220000']]]
Champagne=[['JP ROSE ICE CHENET 750 ML', ['Precio $110000']], ['JP CHENET ICE EDTION 750 ML', ['Precio $110000']]]
Vino=[['COPA DE VINO', ['Precio 15000']], ['VINO TARAPACA 750 ML', ['Precio 70000']], ['VINO SANTA CAROLINA 750 ML', ['Precio 70000']], ['VINO LAMBRUSCO ROSATO 750 ML', ['Precio $80000']], ['VINO LAMBRUSCO BLANCO 750 ML', ['Precio $80000']]]
Ginebra=[['GINEBRA GORDONS PREMIUM PINK', ['Precio $140000']], ['GINEBRA TANQUERAY 750 ML', ['Precio $190000']], ['GINEBRA BOMBAY 750 ML', ['Precio $220000']], ['GINEBRA TANQUERAY RANGPUR 750 ML', ['Precio $260000']], ['GINEBRA MON 750 ML', ['Precio $320000']], ['GIN MARE 750 ML', ['Precio $390000']], ['FIFTY POUNDS 750ML', ['Precio $360000']], ['BOSQUE DE INDIAS 700ML', ['Precio $160000']], ['BEEFEATER 750ML', ['Precio $220000']]] 
Vodka=[['MINI VODKA ABSOLUT 50 ML', ['Precio $21000']], ['VODKA ABSOLUT 375 ML', ['Precio $99000']], ['VODKA ABSOLUT 750ML', ['Precio $180000']], ['VODKA SMIRNOFF 750 ML', ['Precio $160000']]]
Tequila=[['JOSE CUERVO REPOSADO 375 ML', ['Precio $90000']], ['JOSE CUERVO REPOSADO 750ML', ['Precio $180000']], ['JOSE CUERVO SILVER 750ML', ['Precio $170000']], ['DON JULIO BLANCO 700 ML', ['Precio $350000']], ['DON JULIO REPOSADO 700 ML', ['Precio $420000']], ['DON JULIO AÑEJO 750 ML', ['Precio $450000']], ['TEQUILA PATRON SILVER 750 ML', ['Precio $410000']], ['TEQUILA PATRON REPOSADO 750 ML', ['Precio $420000']]]
Ron=[['RON VIEJO DE CALDAS 375 ML', ['Precio $60000']], ['RON VIEJO DE CALDAS 750 ML', ['Precio $110000']], ['RON BACARDI AÑEJO 750 ML', ['Precio $130000']], ['RON ZACAPA 23 750 ML', ['Precio $420000']]]
Aguardiente=[['AGUARDIENTE ANTIOQUEÑO 375 ML', ['Precio $60000']], ['AGUARDIENTE ANTIOQUEÑO TAPA AZUL', ['Precio $110000']]]


menu_comidas = [['Carnes Angus Beef', Carnes_Angus_Beef], ['Entradas', Entradas], ['Carnes Uruguayas y Argentinas', Carnes_Uruguayas_Argentinas], ['Carnes Nacionales', Carnes_Nacionales], ['Cerdo', Cerdo], ['Burgers', Hamburguesas], ['Brochetas', Brochetas], ['Pollos', Pollos], ['Pastas', Pastas], ['Para Compartir', Para_Compartir], ['Ensaladas', Ensaladas], ['Menu Infantil Postres', Menu_Infantil_Postres]]
menu_cocteles=[['Cocteles de Autor', Cocteles_de_Autor], ['Bebidas Especiales', Bebidas_Especiales], ['Bebidas', Bebidas], ['Cervezas Importadas', Cervezas_Importadas], ['Cervezas', Cervezas], ['Sangrias', Sangrias], ['Whisky', Whisky], ['Champagne', Champagne], ['Vino', Vino], ['Ginebra', Ginebra], ['Vodka', Vodka], ['Tequila', Tequila], ['Ron', Ron], ['Aguardiente', Aguardiente]]


contador2=3


def autousercajero(nombre, documento):
    usu= "cajero" + str(contador2)
    cont = "Ab" + str(documento)
    list_1=[usu, cont, nombre, documento]
    cajeros.append(list_1)
    return usu, cont

def verifidocum():    
    while 1:
        try:
            documento = int(input ("Ingrese documento o ingrese (7) para salir: "))
            if documento == 7:
                break
            elif len(str(documento)) >= 8 and len(str(documento)) <= 10:
                break
            else:
                print("Ingrese correctamente el documento.")
        except ValueError:
            print("Error, Ingrese números")
    return documento

def verifinombre (nombre):
    contadorveri = 0
    while 1:
        if contadorveri != 0 :
            nombre=input('Ingrese correctamente o  1. Salir: ')
        if nombre == "1":
            return nombre
            break
        elif nombre.replace(" ", "") != "":
            return nombre
            break
        contadorveri += 1
  

def verifiprice():
    while True:
        try:
            precio = int(input("Por favor, Ingrese el precio del producto: "))  
            if len(str(precio)) >= 4:
                precio = '{:,}'.format(int(precio)).replace(',', '.')
                print(precio)
                break
            elif precio > 0 and precio < 1000 :
                print(precio)
                break
        except ValueError:
            print('Ingrese precio valido.')
    return precio

def mostrarMenuCocteles():
    contadorcuen=0
    print('MENÚ DE COCTELES :P')
    for coctel in menu_cocteles:
        contadorcuen+=1
        print(contadorcuen, '->', coctel[0])

def mostrarMenuComida():
    print("MENÚ DE COMIDAS :P")
    contadorcuen=0
    for comida in menu_comidas:
        contadorcuen+=1
        print (contadorcuen, '->', comida[0])

def verificatecocteles (): 
    while 1:
        try :
            numberproduct= int(input('Ingrese número de la categoría en la que desea hacer un cambio o ' + str(len(menu_cocteles)+5) + " para salir:  "  ))
            if numberproduct <= len(menu_cocteles) and numberproduct >= 1:
                bandera7 = True
                return bandera7, numberproduct 
                break
            elif len(menu_cocteles)+5 == numberproduct:
                bandera7 = False
                return bandera7, numberproduct
                break  
        except ValueError:
            print("Ingrese el número de la categoria")

def verificatecomidas (): 
    while 1:
        try :
            numberproduct= int(input('Ingrese número de la categoría en la que desea hacer un cambio o ' + str(len(menu_comidas)+5) + " para salir:  "  ))
            if numberproduct <= len(menu_comidas) and numberproduct >= 1:
                bandera7 = True
                return bandera7, numberproduct 
                break
            elif len(menu_comidas)+5 == numberproduct:
                bandera7 = False
                return bandera7, numberproduct
                break  
        except ValueError:
            print("Ingrese el número de la categoria")


def nuevoProductoCocteles(numberproduct):
    nuevo=menu_cocteles[int(numberproduct)-1]
    nombre_producto = input('Ingrese el nombre del nuevo producto o 1. Salir: ')
    nombre_producto = verifinombre (nombre_producto)
    descripcion=input('Ingrese la descripción del nuevo producto: ')
    descripcion = verifinombre (descripcion)
    if nombre_producto != "1" and descripcion != "1":
        precio=verifiprice()
        nuevo[1].append([nombre_producto.upper(), descripcion, 'Precio: $' + str(precio)])
        menu_cocteles[int(numberproduct)-1]=nuevo
        print(menu_cocteles[int(numberproduct)-1])
    else:
        print("No se guardo el producto")

def nuevoProductoComida(numberproduct):
    nuevo=menu_comidas[int(numberproduct)-1]
    nombre_producto=input('Ingrese el nombre del nuevo producto o 1. Salir: ')
    nombre_producto = verifinombre (nombre_producto)
    descripcion = input('Ingrese la descripción del nuevo producto o 1. Salir: ')
    descripcion = verifinombre(descripcion)
    if nombre_producto != "1" and descripcion != "1":
        precio=verifiprice()
        nuevo[1].append([nombre_producto.upper(), descripcion, 'Precio: $' + str(precio)])
        menu_comidas[int(numberproduct)-1]=nuevo
        print(menu_comidas[int(numberproduct)-1])
    else:
        print("No se guardo el producto")


def mostarSubmenuProductoComida(numberproduct):
    categoria=menu_comidas[int(numberproduct)-1]
    nuevo=categoria[1]
    contador = 0
    for mostrar in nuevo:
        contador+=1
        print(contador, '->',mostrar[0])

def mostarSubmenuProductoCocteles(numberproduct):
    categoria=menu_cocteles[int(numberproduct)-1]
    nuevo=categoria[1]
    contador = 0
    for mostrar in nuevo:
        contador+=1
        print(contador, '->',mostrar[0])


while 1:
    print("¡¡¡ Bienvenid@s a OLD WEST !!! (づ ｡◕‿‿◕｡) づ  ")
    queso=input("(Ingrese un número): 1. Administrador, 2. Cajero, 3. Usuario:     ")
    if queso=='1':
        bandera5 = True
        while bandera5 == True :
            bandera1=False
            usuarioAdm=input("Ingrese usuario: ")
            contraseñaAdm=input("Ingrese contraseña: ")
            if usuarioAdm==admin[0] and contraseñaAdm==admin[1]:
                print("Bienvenid@ Administrador :D ")
                bandera1=True
            while bandera1==True:
                hacerAdm = input("(Ingrese un número) 1. Cajero, 2. Producto, 3. Ventas, 4. Volver al menú: ")
                bandera3 =False
                while bandera3==False:
                    if hacerAdm=='1':
                        bandera2=False
                        while bandera2==False:
                            cajerosOpc=input("(Ingrese un número) 1. Ver cajeros, 2. Eliminar cajero, 3. Nuevo cajero, 4. Modificar datos,  5. volver al menú: ")
                            if cajerosOpc=="1": 
                                print(cajeros)
                            elif cajerosOpc=="2":
                                eliminoCajero=input('¿Qué cajero desea eliminar?: Ingrese el usuario del cajero: ')
                                contador=-1
                                for caje in cajeros:
                                    contador+=1
                                    if eliminoCajero==caje[0]:
                                        del cajeros[contador]
                                        bandera2=True
                                if bandera2 == False :
                                    print("Cajero no encontrado.")
                                print(cajeros)
                            elif cajerosOpc=='3':
                                contador2+=1                    
                                nombre=input('Ingrese su nombre o 1. Salir: ')
                                nombre = verifinombre(nombre)
                                if nombre != "1" :
                                    documento = verifidocum()
                                    if len(str(documento)) >= 8 and len(str(documento)) <= 10 :
                                        print(autousercajero(nombre,documento))
                                        print(cajeros)
                            elif cajerosOpc=="4":
                                user_modificar=input("¿Qué cajero desea modificar?: ")
                                contadormodi=-1
                                for equisde in cajeros:
                                    contadormodi+=1
                                    if user_modificar==equisde[0]:                                        
                                        while 1:
                                            usuariomod=input('¿Va a modificar usuario? si/no :   ')
                                            cambios=[]
                                            if usuariomod =="si":
                                                usuariocam=input('Ingrese nuevo usuario: ')
                                                cambios.append(usuariocam)
                                                break
                                            elif usuariomod =="no":
                                                cambios.append(equisde[0])
                                                break
                                        while 1:
                                            contraseñamod=input('¿Va a modificar contraseña? si/no :   ')
                                            if contraseñamod =="si":
                                                contraseñacam=input('Ingrese nueva contraseña: ')
                                                cambios.append(contraseñacam)
                                                break                                            
                                            elif contraseñamod =="no":
                                                cambios.append(equisde[1])
                                                break
                                        while 1:
                                            nombremod=input('¿Va a modificar nombre? : si/no: ')
                                            if nombremod =="si":
                                                nombrecam=input('Ingrese nuevo nombre: ')
                                                cambios.append(nombrecam)
                                                cambios.append(equisde[3])
                                                break
                                            elif nombremod =="no":
                                                cambios.append(equisde[2])
                                                cambios.append(equisde[3])
                                                break
                                        cajeros[contadormodi]=cambios
                            elif cajerosOpc=="5":
                                bandera3 =True
                                break

                    elif hacerAdm == "2":
                        bandera4 = True
                        print(bandera4 )
                        
                        while bandera4 == True:
                            producOpc = input("Ingrese un número: 1. Ver productos, 2. Nuevo producto o Categoría, 3. Eliminar Producto o Categoría, 4. Salir: ")
                            if producOpc == "1":
                                while 1:
                                    cualmenu = input("Ingrese un número: 1. Menú Comidas, 2. Menú Cocteles, 3. Salir: ")
                                    if cualmenu == "1":
                                        mostrarMenuComida()
                                    elif cualmenu =='2':
                                        mostrarMenuCocteles()
                                    elif cualmenu =='3':
                                        break
                                    

                            elif producOpc =='2':
                                while 1:
                                    add = input('Agregar nuevo:  1. Producto, 2. Categoría, 3. Salir : ')
                                    if add == '1':
                                        while 1 :
                                            cualmenu2 = input('Ingrese un número: 1. Menú Comidas, 2. Menú Cocteles, 3. Salir: ')
                                            if cualmenu2 == '1':
                                                mostrarMenuComida()
                                                bandera7 , numberproduct = verificatecomidas()            
                                                if bandera7 == True:
                                                    nuevoProductoComida(str(numberproduct))
                                                elif bandera7 == False:
                                                    print("No se guardo el producto ")    
                                            elif cualmenu2 == '2':
                                                mostrarMenuCocteles()
                                                bandera7 , numberproduct = verificatecocteles()            
                                                if bandera7 == True:
                                                    nuevoProductoCocteles(numberproduct)
                                                elif bandera7 == False:
                                                    print("No se guardo el producto ")
                                            elif cualmenu2 == '3':
                                                break

                                    elif add =='2':
                                        while 1 :
                                            tipocatego=input('Ingrese un número: 1. Menú Comidas, 2. Menú Cocteles, 3. Salir: ')
                                            
                                            if tipocatego=='1':
                                                nombrecatego=input('ingrese nombre de la nueva categoria o 1. Salir   ')
                                                if nombrecatego != "1":
                                                    categorianueva=[nombrecatego,[]]
                                                    menu_comidas.append(categorianueva)
                                                    while 1 :
                                                        productopregun=input('deasea ingresar productos "si" o "no"  ' )
                                                        if productopregun=="si":
                                                            num=str(len(menu_comidas))
                                                            nuevoProductoComida(num)
                                                            print('Categoría agregada con los nuevos productos')
                                                            break
                                                        elif productopregun=="no":
                                                            print('Categoría agregada')
                                                            break
                                                elif nombrecatego == "1":
                                                    print("Categoría no agregada ")
                                                    break
                                            elif tipocatego =='2':
                                                nombrecatego=input('ingrese nombre de la nueva categoria o 1. Salir   ')
                                                if nombrecatego != "1":
                                                    categorianueva=[nombrecatego,[]]
                                                    menu_cocteles.append(categorianueva)
                                                    while 1:
                                                        productopregun=input('desea ingresar productos')
                                                        if productopregun=="si":
                                                            num=str(len(menu_cocteles))
                                                            nuevoProductoCocteles(num)
                                                            print('categoria agregada con los nuevos productos')
                                                            break
                                                        elif productopregun=="no":
                                                            print('categoria agregada')
                                                            break
                                                elif nombrecatego == "1":
                                                    print("Categoría no agregada ")
                                                    break
                                            elif tipocatego =="3":
                                                break
                                    elif add == "3":
                                        break

                            elif producOpc == "3" :
                                produocate=input('¿Que desea eliminar? 1. Producto, 2. Categoría:   ') 
                                if produocate=='1':
                                    cualpro=input('Ingrese un número: 1. Menú Comidas, 2. Menú Cocteles, 3. Salir: ')
                                    if cualpro == '1':
                                        mostrarMenuComida()
                                        bandera7 , numberproduct = verificatecomidas()
                                        if bandera7 == True:
                                            mostarSubmenuProductoComida(numberproduct)
                                            numberoletr=input('ingrese numero :   ')

                                            caten=int(numberproduct)-1
                                            elimino=menu_comidas[caten]
                                            productoeliminado=[]
                                            if numberoletr.isnumeric():
                                                num=int(numberoletr)-1
                                                nup=elimino[1]
                                                productoeliminado.append(nup.pop(num))
                                                elimino=nup
                                                menu_comidas[caten]=elimino
                                                print( menu_comidas[caten])

                                    elif cualpro == '2':
                                        mostrarMenuCocteles()
                                        numberproduct=input('Ingrese número de la categoría a la que desea eliminarle un producto: ')
                                        if numberproduct.isnumeric():
                                            mostarSubmenuProductoCocteles(numberproduct)
                                            numberoletr=input('ingrese numero :   ')
                                            caten=int(numberproduct)-1
                                            elimino=menu_cocteles[caten]
                                            productoeliminado=[]
                                            if numberoletr.isnumeric():
                                                num=int(numberoletr)-1
                                                nup=elimino[1]
                                                productoeliminado.append(nup.pop(num))
                                                elimino=nup
                                                menu_cocteles[caten]=elimino
                                                print( menu_cocteles[caten])

                                if produocate=='2':
                                    cualpro=input('Ingrese un número: 1. Menú Comidas, 2. Menú Cocteles, 3. Salir: ')
                                    productoeliminado=[]
                                    if cualpro == '1':
                                        mostrarMenuComida()
                                        numberproduct=input('Ingrese número de la categoria que desea eliminar:  ')
                                        productoeliminado=menu_comidas.pop(int(numberproduct)-1)
                                        mostrarMenuComida()
                                    elif cualpro == '2':
                                        mostrarMenuCocteles()
                                        numberproduct=input('Ingrese número de la categoria que desea eliminar:  ')
                                        productoeliminado=menu_cocteles.pop(int(numberproduct)-1)
                                        mostrarMenuCocteles()




                            elif producOpc == "4" :
                                bandera3 = True
                                break       

####################################################################################################3
                            
                    elif hacerAdm == "4":
                        bandera3 = True
                        bandera1 = False  
                        bandera5 = False


                    
    elif queso=='2':
        bandera6 = True
        while bandera6 == True:
            bandera6 = False
            usuarioCaj=input("1.Iniciar sesión : ")
    elif queso=='3':
        dese2=input("1.iniciar sesion o 2.registrarse : ")
        if dese2=='1':
            usuarioUsu=input("Ingrese usuario ")
            contraseñaUsu=input("Ingrese contraseña ")
        elif dese2=='2':
            nombre=input('Ingrese su nombre: ')
            documento=input('Ingrese su documento:')
            direccion=input('Ingrese su direccion: ')
            telefono=input('Ingrese su telefono: ')






