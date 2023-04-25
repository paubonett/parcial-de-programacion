admin=['adminsap','admin123']
cajeros=[['cajeand','sharon123', 'Sharon Andreina', '1092387960'],['cajeang','angel123', 'Angel Daniel', '1093293435'], ['cajealj', 'paula123', 'Paula', '1090371768']]

##########################################################################################


def buscar_user_pass(matriz, usuario, contraseña):
    for uWu in matriz:
        if uWu[0] == usuario and uWu[1] == contraseña:
            return True
    return False

usuarios=[['user1', 'pass1', 'Alicia', '12345678', '0000000000', 'País de las maravillas'], ['user2', 'pass2', 'Naruto', '87654321' '1111111111', 'Aldea Oculta de la Hoja']]

##########################################################################################

def imprimir_menu_comidas(menu_comidas):
    for submenu in menu_comidas:
        for texto in submenu:
            print(texto)
        print()

##########################################################################################
def imprimir_menu_cocteles(menu_cocteles):
    for submenu in menu_cocteles:
        for texto in submenu:
            print(texto)
        print()



Carnes_Angus_Beef = [['TOMAHWK BEEF', ['-Corte de 1000 gr -Guarnición papa -Yuca al vapor -Cascos de papa -Papas a la francesa -Ensalada pico e’ gallo'], ['Precio $299000'], "1101"] , ['RIBEYE BEEF', ['-Corte de 400 gr -Papa al vapor -Yuca al vapor -Ensalada pico e’ gallo'], ['Precio $139000'],  "1102"] , ['PICANHA ANGUS BEEF', ['-Corte de 400 gr -Guarnición papa -Yuca al vapor -Cascos de papa -Papas a la francesa -Ensalada pico e’ gallo'], ['Precio $119000'], "1103"] , ['NEW YORK STEAK BEEF', ['-Lomo Ancho de 400 gr -Guarnición papa -Yuca al vapor -Cascos de papa -Ensalada pico e’ gallo'], ['Precio $129000'], "1104"], ['ASADO DE TIRA BEEF', ['-Corte de 400 gr'], ['Precio $119000'], "1105"], ['BIFE DE VACIO BEEF', ['-Pieza de 400 gr'], ['Precio $139000'], "1106"]]                                                                      
Entradas = [['NACHOS DAKOTA' ,['-Nachos crocantes -Carne al estilo tex-mex -Queso cheddar americano -Guacamole -Pico e ‘gallo -Frijol refrito'], ['Precio $29000'], "1107"], ['SAUSAGE OLD WEST ', ['-4 chorizos de ternera -Salsa de whisky Jack Daniel’s -Papas a la francesa'], ['Precio $29000'], "1108"] , [ 'PAPAS WEST SIDE', ['-Papas a la francesa -Queso cheddar -Chorizo de ternera -Tocineta crunchy'], ['Precio $30000'], "1109"] , [ 'MAZORQUITAS' ,['-3 Mazorquitas al grill -Cubierta de queso paisa'], ['Precio $21000'], "1110"] ,  [ 'CAMARONES FORT HAYS',  ['-14 camarones apanados -Guacamole -Dip de tártara -Pimentón rostizado'], ['Precio $32000'],  "1111"] , [ 'MAICITOS' , ['-Maíz dulce -Pollo al grill -Tocineta -Gratinado en queso doble crema y parmesano'], ['Precio $34000'],  "1112"], [ 'ALITAS RANGER', ['-12 piezas de alas -Salsa bbq -Miel -Mostaza -Picantes con papas a la francesa'], ['Precio $34000'],  "1113"]]
Carnes_Uruguayas_Argentinas = [['TOMAHAWK URUGUAYO' , ['-Corte de 1000 gr -Guarnición de papa -Yuca al vapor -Ensalada pico e’ gallo'], ['Precio $ 190000'],  "1114"] , ['CHULETON ARGENTINO', ['-Ojo de bife con hueso de 800 gr -Guarnición de papa -Yuca al vapor -Ensalada pico e’ gallo'], ['Precio $ 170000'],  "1115"] , ['PORTER HOUSE ARGENTINO', ['-Corte de 800 gr -Guarnición de papa -Yuca al vapor -Ensalada pico e’ gallo'], ['Precio $160000'],  "1116" ] , ['BEEF CHORIZO ARGENTINO', ['-Bife angosto de 600 gr -Guarnición de papa -Yuca al vapor -Ensalada pico e’ gallo'], ['Precio $130000'],  "1117" ]]
Carnes_Nacionales=[['PICANHA BACON RANCH', ['-Res al grill de 400 gr -Salsa Jack Daniel’s -Guarnición de papa -Yuca al vapor -Ensalada pico e’ gallo'], ['Precio $64000'], "1118"], ['PICANHA', ['-Res al grill de 400 gr -Guarnición de papa -Yuca al vapor -Ensalada pico e’ gallo'], ['Precio $62000'],  "1119"], ['CHURRASCO',['-Lomo ancho en corte mariposa de 400 gr -Guarnición papa -Yuca al vapor -Ensalada pico e gallo'], ['Precio $56000' ],  "1120" ], ['BABY BEEF CORN', ['-Lomo Fino de 330 gr -Salsa De Tocineta -Maíz Dulce -Queso Parmesano -Guarnición De Pure De Papa -Mix De Lechugas'], ['Precio $49000'],  "1121"], ['BABY BEEF WESTERN', ['-Lomo Fino de 330 gr -Salsa de champiñones -Guarnición de pure de papa -Mix de lechugas'], ['Precio $46000'],  "1122"], ['BABY BEEF REEWARD', ['-Lomo Fino de 330 gr -Guarnición de papa -Yuca al vapor -Mix de lechugas'], ['Precio $46000'],  "1123"]]
Cerdo=[['CHICARRON', ['-400 gr de Chicharrón Crocante -Guarnición papa -Yuca al vapor -Chimichurri -Rodajas de limón'], ['Precio $46000'],  "1124"], ['RIBS JACK DANIEL’S', ['-400 gr de costillas de cerdo -Salsa de bbq -Salsa Jack Daniel’s -Guarnición de papas a la francesa -Mix de lechugas'], ['Precio $52000'],  "1125"], ['COSTILLITAS', ['-400 gr de costillitas de cerdo -Salsa bbq -Miel mostaza guarnición -Papas a la francesa -Mix de lechugas'], ['Precio $49000'],  "1126"], ['LOMO DE CERDO', ['Lomo de Cerdo de 330 gr -Salsa bbq -Guarnición de papas a la francesa -Mix de lechugas'], ['Precio $44000'],  "1127"]]
Hamburguesas=[['ANGUS BURGUER', ['-Carne Angus de 300 gr -Pan brioche -Queso americano -Tocineta -Vegetales en finas hiervas -Cebolla caramelizada -Pepinillos'], ['Precio $49000'],  "1128" ], ['JACK DANIELS', ['-Pan brioche -150 gr de carne de res -Salsa Jack Daniels -Chorizo de ternera -Queso cheddar -70gr tocineta ahumada -Tomate horneado -Cebolla caramelizada en vino tinto -Lechuga fresca'], ['Precio $28000'],  "1129"], ['SHERIFF', ['-150 gr de carne de res -120 gr de pullet pork -Pan baguette semi dulce -Salsa showyn -Colslaw -Queso Colby Jack'], ['Precio $28000'],  "1130" ], ['LAS VEGAS', ['-150 gr de carne de res -80 gr de brisket ahumado -Pan artesanal -Macarrón cheese -Vegetales frescos'], ['Precio $28000'],  "1131" ], ['EL PRIMO CARIM MUSTAFÁ', ['-300 gr de carne de res doble -Pan brioche -Tocineta -Queso monster -Vegetales frescos -Pepinillos -Salsa de tomate heinz -Mayonesa kraft -Mostaza heinz'], ['Precio $33000'],  "1132"], ['HARLEY DAVIDSON', ['-300 gr carne de res triple -Pan brioche -Vegetales frescos -Tocineta -Pepinillo -Queso cheddar -Salsa tártara y showy'], ['Precio $30000'],  "1133"], ['TÍO SAM', ['-100 gr de lomo de cerdo -100 gr de pechuga -150 gr de carne de res -Pan brioche -Tocineta ahumada -Queso cheddar -Vegetales frescos'], ['Precio $32000'],  "1134"], ['LA ROCKERA', ['-150 gr de carne de res -80 gr de brisket ahumado -Pan brioche -Queso pepperjack -Lechuga Batavia -Cebolla morada -Pepinillos'], ['Precio $29000'],  "1135"], ['CLUB HOUSE', ['-160 gr de dip de pollo -150 gr de tocineta -2 huevos -Queso doble crema -Queso chédar americano'], ['Precio $35000'],  "1136"]]
Brochetas=[['BROCHETA BUFFALO BILL', ['-2 brochetas de lomo de res con 200 gr c/u -Guarnición de papas a la francesa'], ['Precio $49000'],  "1137"], ['BROCHETA APACHE', ['-2 brochetas de 200 gr c/u de pechuga al grill -Guarnición de papas a la francesa'], ['Precio $42000'],  "1138"], ['BROCHETA LEGENS', ['-Brocheta de lomo de res de 200 gr -Brocheta de 200 gr de pechuga al grill -Guarnición de papas a la francesa'], ['Precio $49000'],  "1139"]]
Pollos=[['MUSHROOM CHICKEN', ['-330 gr de pechuga al grill -Salsa de champiñones -Guarnición de puré de papa -Mix de lechugas'], ['Precio $39000'],  "1140" ], ['CORN GRILLED CHICKEN', ['-330 gr de pechuga al grill -Salsa de maíz -Tocineta -Queso parmesano -Guarnición de puré de papa -Mix de lechugas'], ['Precio $39000'],  "1141"], ['GRILLED CHICKEN', ['-330 gr de pechuga al grill -Guarnición papas a la francesa -Papa al vapor -Yuca al vapor -Mix de lechugas'], ['Precio $37000'],  "1142"]]
Pastas=[['CAMARONERA', ['-250 gr de camarones -Salsa de mostaza dijon -Vino blanco -Pan focaccia -Pasta de fettuccine'], ['Precio $49000'],  "1143"], ['MUSHROOM', ['-200 gr de lomo fino al grill -Fettuccini -Salsa de champiñón -Pan focaccia'], ['Precio $49000'],  "1144"], ['CARBONARA SWEET CORN', ['-230 gr pechuga al grill -Maíz dulce -Tocineta -Pasta fettuccine -Pan focaccia'], ['Precio $47000'],  "1145"]]
Para_Compartir=[['PICADA OLD WEST', ['-450 gr de pechuga al grill -330 gr de lomo de cerdo -200 gr de lomo fino -2 chorizos de ternera -Ensalada pico e’ gallo -Papas a la francesa -Papa al vapor -Cascos de papa -Yuca al vapor -Queso paisa en cubos'], ['Precio $109000'],  "1146"], ['WILD WEST', ['-400 gr de costillitas de cerdo -Salsa bbq -300 gr de chicharrón crujiente -300 gr de brisket de res ahumado -12 alitas -Salsa bbq -3 mazorquitas -Queso paisa -Macarrón cheese -Papa al vapor -Crotones de tocineta -Mix de lechuga'], ['Precio $119000'],  "1147"]]
Ensaladas=[['ENSALADA LUSIANA', ['-350 gr pollo crispy o al grill -50 gr tocineta ahumada -Mix de lechugas tomate Cherry -Queso parmesano -Crotones de pan -Aderezo de la casa -Reducción de vinagre balsámico'], ['Precio $34000'],  "1148"], ['ENSALADA DE CAMARONES', ['-300 gr de camarones al crispy -Mix de lechugas -Tomates Cherry -Crotones de pan -Queso parmesano -Aderezo de la casa -Reducción de vinagre balsámico'], ['Precio $36000'],  "1149"]]
Menu_Infantil_Postres=[['VAQUERITOS BURGUER', ['-Pan brioche -150 gr de carne molida de res -Tocineta -Queso cheddar americano -Papas a la francesa -Juguete infantil'], ['Precio $32000'],  "1150" ], ['CHEROKEE CHICKEN', ['-250 gr de pollo apanado -Guarnición de papas a la francesa -Juguete infantil'], ['Precio $32000'],  "1151" ], ['TORTA DE CHOCOLATE',[""], ['Precio $12000'],  "1152"], ['LINGOTE DE ORO', ['-Barra de chocolate -Azúcar dorada -Licor dulce -Ganache de frutos secos -Helado artesanal'], ['Precio $19000'],  "1153"]]


Cocteles_de_Autor=[['TORO SENTADO', ['-Whisky Red label -Licor de café -Vino embajador -Cerveza club negral -Piña -Naranja'], ['Precio $28000'],  "2101" ], ['BILLY THE KID', ['-Jack Daniels Honey  -Jaguermeister -Crema de coco'], ['Precio $32000'],  "2102" ], ['CALIBRE 38', ['-Whisky Jack Daniel No 7 -Limon -Syrop de frutos rojos -Syrop simple -Ginger'], ['Precio $32000'],  "2103"], ['BONNIE & CLYDE', ['-Ron de coco -Jägermeister -Syrop frutos amarillos -Shrup de piña -Jarabe de genjibre -Limón'], ['Precio $32000'],  "2104"], ['JHON WESLY', ['-Tequila Reposado -Ron coco -Syrop de maracuya -Shrup de piña -Ginger'], ['Precio $30000'],  "2105"], ['JESSE JAMES', ['-Ron blanco -Curacao azul -Syrop de piña -Syrop de maracuya -Ginger'], ['Precio $30000'],  "2106"], ['SE BUSCA', ['-Vodka -Limón -Syrop de lychhe -Vino Rosado lambrusco -Syrop de frutos rojos'], ['Precio $32000'],  "2107"], ['INMORTAL JACK', ['-Jack Daniel No 7 Botellita -Licor de melon -Jarabe de jengibre -Zumo de  limon -Licor de durazno -Jägermeister'], ['Precio $34000'],  "2108"], ['GIN CAKTUS', ['-Ginebra -Infusión de pepino -Tonica nacional'], ['Precio $30000'],  "2109"]]
Bebidas_Especiales=[['SODAS', ['-Frutos amarillos -Frutos rojos'], ['Precio $10000'], "2110" ], ['SODAS 2', ['-Frutos Azules'], ['Precio $12000'], "2111"], ['LIMONADAS', ['-Limonada Cerezada -Coco Limonada -Limonada Hierba Buena'], ['Precio $11000'], "2112"], ['LIMONADA DE ROSAS', ["-Limonada de rosas"], ['Precio $24000'], "2113"], ['FRAPPES', ['-Naranja -Maracuyá -Limón'], ['Precio $9000'], "2114"]]
Bebidas=[['AGUA', [""], ['Precio $5000'], "2115"], ['COCA-COLA PET 400ML',[""],  ['Precio $6000'], "2116"], ['COCA-COLA ZERO PET 400ML', [""], ['Precio $6000'], "2117" ], ['GASEOSAS QUATRO - KOLA ROMAN', [""], ['Precio $5000'], "2118"], ['GINGER - SODA',[""], ['Precio $6000'], "2119"], ['REDBULL', [""], ['Precio $10000'], "2120" ]]
Cervezas_Importadas=[['ERDINGER WEISSBIER', [""], ['Precio $32000'], "2121" ], ['ERDINGER DUNKEL',[""], ['Precio $32000'], "2122"], ['ERDINGER PIKANTUS', [""], ['Precio $38000'], "2123"], ['TROOPER BEER IRON MAIDEN', [""], ['Precio $32000'], "2124"], ['CERVEZA ACDC', [""], ['Precio $32000'], "2125"], ['BUDWEISER 250ML',[""], ['Precio $8000'] , "2126"], ['HEINEKEN', [""], ['Precio $10000'], "2127"], ['CORONA', [""], ['Precio $12000'], "2128"], ['SMIRNOFF ICE 275ML', [""], ['Precio $15000'], "2129"], ['SMIRNOFF ICE 275ML APPLE', [""], ['Precio $15000'], "2130" ]]
Cervezas=[['CERVEZA ARTESANAL OLDWEST', [""], ['Precio $10000'], "2131"], ['CERVEZA AGUILA', [""], ['Precio $7000'] , "2132"], ['CERVEZA AGUILA LIGHT', [""], ['Precio $7000'], "2133"], ['CERVEZA POKER', [""], ['Precio $7000'], "2134"], ['CERVEZA CLUB COLOMBIA', ['-Roja -Negra -Dorada -Doble Malta'], ['Precio $8000'] , "2135"]]
Sangrias=[['JARRA ROSADA', ['-Fresas -Hierba Buena -Cereza -Uvas Isabelina'], ['Precio $110000'] , "2136"], ['JARRA AZUL', ['-Fresas -Arandanos -Uva Isabelina -Lycehes'], ['Precio $110000'], "2137"], ['JARRA TINTO', ['-Fresas -Uvas -Naranja -Cereza -Uva Isabelina'], ['Precio $110000'], "2138"], ['COPA DE SANGRÍA', [""], ['Precio $30000'], "2139"]]
Whisky=[['CREMA DE WHISKY - BAILEYS 375 ML',[""], ['Precio $80000'], "2140"], ['CREMA DE WHISKY - BAILEYS 700 ML', [""], ['Precio $130000'], "2141"], ['BLACK Y WHITE', [""], ['Precio $120000'], "2142" ], ['BUCHANANS 12 AÑOS 375 ML', [" "], ['Precio $175000'], "2143"], ['BUCHANANS 12 AÑOS 750 ML DELUXE', [""], ['Precio $250000'], "2144"], ['BUCHANANS 18 AÑOS 750 ML',[""], ['Precio $470000'], "2145"], ['BUCHANNAS MASTER 750 ML', [""], ['Precio $320000'], "2146"], ['MINI JACK DANIELS 50 ML', [""], ['Precio $25000'] , "2147"], ['JACK DANIELS 375ML', [""], ['Precio $160000'], "2148"], ['JACK DANIEL’S TENNESSE 750 ML', [""], ['Precio $280000'], "2149"], ['JACK DANIEL’S HONEY 750 ML', [""], ['Precio $280000'], "2150" ], ['JACK DANIEL’S TENNESSE FIRE 750 ML', [""], ['Precio $280000'], "2151"], ['JHONNIE WALKER RED LABEL 750 ML', [""], ['Precio $150000'] , "2152"], ['JHONNIE WALKER BLACK LABEL 750 ML', [""], ['Precio $240000'], "2153"], ['MACALLAN 12 DOUBLE CASK 700 ML', [""], ['Precio $600000'] , "2154"], ['OLD PARR 12 AÑOS 500 ML', [""], ['Precio $180000'], "2155"], ['OLD PARR 12 AÑOS 750 ML', [""], ['Precio $220000'], "2156"]]
Champagne=[['JP ROSE ICE CHENET 750 ML', [""], ['Precio $110000'], "2157"], ['JP CHENET ICE EDTION 750 ML', [""], ['Precio $110000'], "2158"]]
Vino=[['COPA DE VINO', [""], ['Precio 15000'], "2159"], ['VINO TARAPACA 750 ML', [""], ['Precio 70000'], "2160" ], ['VINO SANTA CAROLINA 750 ML', [""], ['Precio 70000'], "2161"], ['VINO LAMBRUSCO ROSATO 750 ML',[""], ['Precio $80000'], "2162"], ['VINO LAMBRUSCO BLANCO 750 ML', [""], ['Precio $80000'], "2163"]]
Ginebra=[['GINEBRA GORDONS PREMIUM PINK', [""], ['Precio $140000'], "2164"], ['GINEBRA TANQUERAY 750 ML', [""], ['Precio $190000'], "2165"], ['GINEBRA BOMBAY 750 ML', [""], ['Precio $220000'], "2166"], ['GINEBRA TANQUERAY RANGPUR 750 ML', [" "], ['Precio $260000'], "2167"], ['GINEBRA MON 750 ML', [""], ['Precio $320000'], "2168"], ['GIN MARE 750 ML', [""], ['Precio $390000'], "2169"], ['FIFTY POUNDS 750ML',[""], ['Precio $360000'], "2170" ], ['BOSQUE DE INDIAS 700ML',[""], ['Precio $160000'], "2171"], ['BEEFEATER 750ML', [""], ['Precio $220000'], "2172"]] 
Vodka=[['MINI VODKA ABSOLUT 50 ML', [""], ['Precio $21000'], "2173"], ['VODKA ABSOLUT 375 ML', [""], ['Precio $99000'], "2174"], ['VODKA ABSOLUT 750ML', [""], ['Precio $180000'], "2175"], ['VODKA SMIRNOFF 750 ML', [""], ['Precio $160000'], "2176"]]
Tequila=[['JOSE CUERVO REPOSADO 375 ML',[""], ['Precio $90000'], "2177"], ['JOSE CUERVO REPOSADO 750ML', [""], ['Precio $180000'], "2178"], ['JOSE CUERVO SILVER 750ML', [""], ['Precio $170000'], "2179"], ['DON JULIO BLANCO 700 ML', [""], ['Precio $350000'], "2180" ], ['DON JULIO REPOSADO 700 ML', [""], ['Precio $420000'], "2181"], ['DON JULIO AÑEJO 750 ML', [""], ['Precio $450000'], "2182"], ['TEQUILA PATRON SILVER 750 ML', [""], ['Precio $410000'], "2183"], ['TEQUILA PATRON REPOSADO 750 ML', [""], ['Precio $420000'], "2184"]]
Ron=[['RON VIEJO DE CALDAS 375 ML', [""] , ['Precio $60000'], "2185"], ['RON VIEJO DE CALDAS 750 ML', [""], ['Precio $110000'], "2186"], ['RON BACARDI AÑEJO 750 ML',[""], ['Precio $130000'], "2187"], ['RON ZACAPA 23 750 ML', [""], ['Precio $420000'], "2188"]]
Aguardiente=[['AGUARDIENTE ANTIOQUEÑO 375 ML', [""], ['Precio $60000'], "2189"], ['AGUARDIENTE ANTIOQUEÑO TAPA AZUL', [""], ['Precio $110000'], "2190"]]



menu_comidas = [['Carnes Angus Beef', Carnes_Angus_Beef], ['Entradas', Entradas], ['Carnes Uruguayas y Argentinas', Carnes_Uruguayas_Argentinas], ['Carnes Nacionales', Carnes_Nacionales], ['Cerdo', Cerdo], ['Burgers', Hamburguesas], ['Brochetas', Brochetas], ['Pollos', Pollos], ['Pastas', Pastas], ['Para Compartir', Para_Compartir], ['Ensaladas', Ensaladas], ['Menu Infantil Postres', Menu_Infantil_Postres]]
menu_cocteles=[['Cocteles de Autor', Cocteles_de_Autor], ['Bebidas Especiales', Bebidas_Especiales], ['Bebidas', Bebidas], ['Cervezas Importadas', Cervezas_Importadas], ['Cervezas', Cervezas], ['Sangrias', Sangrias], ['Whisky', Whisky], ['Champagne', Champagne], ['Vino', Vino], ['Ginebra', Ginebra], ['Vodka', Vodka], ['Tequila', Tequila], ['Ron', Ron], ['Aguardiente', Aguardiente]]

##########################################################################################

contador2=3
contadorAzul=2

PedidosPendientes = []
contadorPedidos = len(PedidosPendientes)

##########################################################################################

PedidosPendientes = []
contadorPedidos = len(PedidosPendientes)



def autousercajero(nombre, documento):
    usu= "cajero" + str(contador2)
    cont = "Ab" + str(documento)
    list_1=[usu, cont, nombre, documento]
    cajeros.append(list_1)
    return usu, cont


def autouser_user(nombre, documento, telefono, direccion):
    usu= "user" + str(contadorAzul)
    cont = "pass" + str(contadorAzul)
    list_1=[usu, cont, nombre, documento, telefono, direccion]
    usuarios.append(list_1)
    print('Su usuario es: ', '(', usu, ')', 'y su contraseña es: ', '(', cont, ')')


def comprarComida ():
    productos = []
    while 1 :
        mostrarMenuComida()
        bandera7 , numberproduct = verificatecomidas()
        if bandera7 == True:
            contador = mostarSubmenuProductoComida(numberproduct)
            bandera9 = True
            while bandera9==True:
                try :
                    producto = int(input("Ingrese un número para ver la descripción del producto o "+ str(contador + 5)+ ". Ver submenú, " + str(contador + 6)+ ". Salir  "))
                    if producto <= contador and producto >0 :
                        nombre = str(menu_comidas[numberproduct-1][1][producto-1][0])
                        print(nombre)      
                        print( ','.join(menu_comidas[numberproduct-1][1][producto-1][1]))
                        print(','.join(menu_comidas[numberproduct-1][1][producto-1][2]))
                        number = str(menu_comidas[numberproduct-1][1][producto-1][3])
                        while 1 :
                            aña = input("(si) Añadir producto, (no) Salir   ")
                            if aña.lower() == "si":
                                if int(number) >= 1128 and int(number) <= 1136:
                                    while 1 :
                                        papas = input("¿En combo con papa a la francesa? $3.000  (si) - (no)")
                                        if papas.lower() == "si":
                                            nombre  = nombre + " combo"
                                            break
                                        elif papas.lower() == "no":
                                            break
                                productos.append(nombre)
                                bandera9 = False
                                break
                            elif aña.lower() == "no":
                                bandera9 = False
                                break
                    elif contador+5 == producto:
                        bandera9 = False
                    elif contador+6 == producto:
                        bandera7 = False
                        bandera9 = False
                except ValueError:
                    print("Ingrese un número")  
        if bandera7 == False:
            break
    if productos == []:
        print("No se guardo nada de comida en el pedido ")
    elif productos != []: 
        return productos

def verifidocum():    
    while 1:
        try:
            documento = int(input ("Ingrese documento o ingrese (7) para salir: "))
            if documento == 7:
                bandera=False
                break
            elif len(str(documento)) >= 8 and len(str(documento)) <= 10:
                bandera=True
                break
            else:
                print("Ingrese correctamente el documento.")
        except ValueError:
            print("Error, Ingrese números")
    return documento,bandera

def verifinombre(nombre):
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
        
def verifitelefono():
    while 1:
        try:
            telefono = int(input("Ingrese su número de telefono o ingrese (3) salir: "))
            if telefono == 3:
                break
            elif len(str(telefono)) == 10:
                break
            else:
                print("Ingrese su número de telefono correctamente.")
        except ValueError:
            print("Error, Ingrese números.")
    return telefono


def contodo ():
    while 1:
        all = input("¿Con todo? (si) - (no) ")
        if all.lower() == "si":
            break
        elif all.lower() == "no":
            cambio = input("Desea añadirle o quitarle algo a la comida?  ")
            return cambio

def verificarString(nombre):
    conu=nombre.replace(" ","")
    if(conu.isalpha()):
        return True
    else:
        print("no ingrese numeros y/o caracteres especiales")

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
            numberproduct= int(input('Ingrese número de la categoría o ' + str(len(menu_cocteles)+5) + " para salir:  "  ))
            if numberproduct <= len(menu_cocteles) and numberproduct >= 1:
                bandera7 = True
                return bandera7, numberproduct 
                break
            elif len(menu_cocteles)+5 == numberproduct:
                bandera7 = False
                return bandera7,""
                break  
        except ValueError:
            print("Ingrese el número de la categoria")

def verificatecomidas (): 
    while 1:
        try :
            numberproduct= int(input('Ingrese número o ' + str(len(menu_comidas)+5) + " para salir:  "  ))
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

def verificateProductoCocteles(numberproduct):
    while 1:
        try :
            categoria=menu_cocteles[int(numberproduct)-1]
            nuevo=categoria[1]
            numero_producto= int(input('Ingrese número o ' + str(len(nuevo)+5) + " para salir:  "  ))
            if numero_producto <= len(nuevo) and numero_producto >= 1:
                bandera7 = True
                return bandera7, numero_producto 
                break
            elif len(nuevo)+5 == numero_producto:
                bandera7 = False
                return bandera7, numero_producto
                break
        except ValueError:
            print("Ingrese el número del producto")

def verificateProductoComidas(numberproduct):
    while 1:
        try :
            categoria=menu_comidas[int(numberproduct)-1]
            nuevo=categoria[1]
            numero_producto= int(input('Ingrese número o ' + str(len(nuevo)+5) + " para salir:  "  ))
            if numero_producto <= len(nuevo) and numero_producto >= 1:
                bandera7 = True
                return bandera7, numero_producto 
                break
            elif len(nuevo)+5 == numero_producto:
                bandera7 = False
                return bandera7, numero_producto
                break   
        except ValueError:
            print("Ingrese el número del producto")



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
        print(contador, '->',mostrar[0],'- ', mostrar[3])
    return contador

def mostarSubmenuProductoCocteles(numberproduct):
    categoria=menu_cocteles[int(numberproduct)-1]
    nuevo=categoria[1]
    contador = 0
    for mostrar in nuevo:
        contador+=1
        print(contador, '->',mostrar[0],'- ' , mostrar[3])
    return contador

def comprarCocteles ():
    productos = []
    while 1 :
        mostrarMenuCocteles()
        bandera7 , numberproduct = verificatecocteles()
        if bandera7 == True:
            contador = mostarSubmenuProductoCocteles(numberproduct)
            bandera9 = True
            while bandera9==True:
                try :
                    producto = int(input("Ingrese un número para ver la descripción del producto o " + str(contador + 5) + ". Ver submenú, " + str(contador + 6) + ". Salir  "))
                    if producto <= contador and producto > 0 :
                        nombre = str(menu_cocteles[numberproduct-1][1][producto-1][0])
                        print(nombre)      
                        print( ','.join(menu_cocteles[numberproduct-1][1][producto-1][1]))
                        print(','.join(menu_cocteles[numberproduct-1][1][producto-1][2]))
                        number = int(menu_cocteles[numberproduct-1][1][producto-1][3])
                        while 1 :
                            aña = input("(si) Añadir producto, (no) Salir  ")
                            if aña.lower() == "si":
                                nombre = opcio (number, nombre)                                    
                                productos.append(nombre)
                                bandera9 = False
                                break
                            elif aña.lower() == "no":
                                bandera9 = False
                                break
                    elif contador+5 == producto:
                        bandera9 = False
                    elif contador+6 == producto:
                        bandera7 = False
                        bandera9 = False
                except ValueError:
                    print("Ingrese un número  ")  
        if bandera7 == False:
            break
    if productos == []:
        print("No se guardo ninguna bebida en el pedido ")
    elif productos != []: 
        return productos

def comprarCocteles ():
    productos = []
    while 1 :
        mostrarMenuCocteles()
        bandera7 , numberproduct = verificatecocteles()
        if bandera7 == True:
            contador = mostarSubmenuProductoCocteles(numberproduct)
            bandera9 = True
            while bandera9==True:
                try :
                    producto = int(input("Ingrese un número para ver la descripción del producto o " + str(contador + 5) + ". Ver submenú, " + str(contador + 6) + ". Salir  "))
                    if producto <= contador and producto > 0 :
                        nombre = str(menu_cocteles[numberproduct-1][1][producto-1][0])
                        print(nombre)      
                        print( ','.join(menu_cocteles[numberproduct-1][1][producto-1][1]))
                        print(','.join(menu_cocteles[numberproduct-1][1][producto-1][2]))
                        number = int(menu_cocteles[numberproduct-1][1][producto-1][3])
                        while 1 :
                            aña = input("(si) Añadir producto, (no) Salir  ")
                            if aña.lower() == "si":
                                nombre = opcio (number, nombre)                                    
                                productos.append(nombre)
                                bandera9 = False
                                break
                            elif aña.lower() == "no":
                                bandera9 = False
                                break
                    elif contador+5 == producto:
                        bandera9 = False
                    elif contador+6 == producto:
                        bandera7 = False
                        bandera9 = False
                except ValueError:
                    print("Ingrese un número  ")  
        if bandera7 == False:
            break
    if productos == []:
        print("No se guardo ninguna bebida en el pedido ")
    elif productos != []: 
        return productos
    
def opcio (number, nombre):    
    while 1:
        if number == 2112 :
            try:
                sabor = int(input("¿Qué sabor desea?: 1. Limonada Cerezada, 2. Coco Limonada, 3. Limonada Hierba Buena    "))
                if int(sabor) == 1:
                    nombre = nombre + " -limonada cerezada"
                    break
                elif int(sabor) == 2:
                    nombre = nombre + " -coco limonada"
                    break
                elif int(sabor) == 3:
                    nombre = nombre + " -hierva buena"
                    break
            except ValueError:
                print("Ingrese un número")
        elif number == 2114:
            try :
                sabor = int(input("¿Qué sabor desea?: 1. Naranja, 2. Maracuyá, 3. Limón"))
                if sabor == 1:
                    nombre = nombre + " -naranja"
                    break
                elif sabor == 2:
                    nombre = nombre + " -maracuyá" 
                    break
                elif sabor == 3:
                    nombre = nombre + " -limón"
                    break
            except ValueError:
                print("Ingrese un número")
        elif number == 2118:
            try:
                sabor = int(input("¿Qué sabor desea?: 1. GASEOSAS QUATRO, 2. KOLA ROMAN "))
                if sabor == 1:
                    nombre = nombre + " -gaseosas quatro"
                    break
                elif sabor == 2:
                    nombre = nombre + " -kola roman"
                    break
            except ValueError:
                print("Ingrese un número")
        elif number == 2119:
            try:
                sabor = int(input("¿Qué sabor desea?: 1. GINGER, 2. SODA "))
                if sabor == 1:
                    nombre = nombre + " -ginger" 
                    break
                if sabor == 2:
                    nombre = nombre + " -soda"
                    break
            except ValueError:
                print("Ingrese un número")
        elif number == 2135:
            try:
                sabor = int(input("¿Qué sabor desea?: 1. Roja, 2. Negra, 3. Dorada, 4. Doble Malta"))
                if sabor == 1:
                    nombre = nombre + " -roja"
                    break
                elif sabor == 2:
                    nombre = nombre + " -negra"
                    break
                elif sabor == 3:
                    nombre = nombre + " -dorada"
                    break
                elif sabor == 4:
                    nombre = nombre + " -doble malta"
                    break
            except ValueError:
                print("Ingrese un número")
    return nombre

####################################################################################################

def eliminarModificarProducto(cualpro):        
    if cualpro == '1':
        mostrarMenuComida()
        bandera7 , numberproduct = verificatecomidas()
        if bandera7 == True:
            bane=True
            mostarSubmenuProductoComida(numberproduct)
            bandera8 , numeropro = verificateProductoComidas(numberproduct)
            caten=int(numberproduct)-1
            elimino=menu_comidas[caten]
            if bandera8 == True:
                num=int(numeropro)-1
                nup=elimino[1]
                bane=True
                return bane,nup,elimino,caten,num
            elif bandera8==False:
                bane=False
                return bane,0,0,0,0
        elif bandera7==False:
            bane=False
            return bane,0,0,0,0
            
    elif cualpro == '2':
        mostrarMenuCocteles()
        bandera7 , numberproduct = verificatecocteles()
        if bandera7==True:
            mostarSubmenuProductoCocteles(numberproduct)
            bandera8 , numeropro = verificateProductoCocteles(numberproduct)
            caten=int(numberproduct)-1
            elimino=menu_cocteles[caten]     
            if bandera8==True:
                num=int(numeropro)-1
                nup=elimino[1]
                return nup,elimino,caten,
            elif bandera8==False:
                bane=False
                return bane,0,0,0,0
        elif bandera7==False:
            bane=False
            return bane,0,0,0,0
            
def mostarInfoCajero():
    for caje in cajeros:
        print(caje[0],"=>",caje[3])

def modificarProductoCoctelComida(cualpron):
    if cualpron=='1':
        bani,nupi,elimino,caten,nume=eliminarModificarProducto('1')
        if bani==True:
            producto_a_modificar=nupi[nume]
            cambiose=[]
            while 1:
                nameproduct=input('¿Desea cambiar nombre del producto? si/no  :  ')
                nameproduct=nameproduct.strip()
                if nameproduct=='si':
                    namenewpro=input('Ingrese nuevo nombre del producto :  ')
                    if verificarString(namenewpro)==True:
                        cambiose.append(namenewpro.upper())
                        break
                elif nameproduct=='no':
                    cambiose.append(producto_a_modificar[0])
                    break
            while 1:
                descripcionproduct=input('¿Desea cambiar descripcion del producto? si/no  :  ')
                descripcionproduct=descripcionproduct.strip()
                if descripcionproduct=='si':
                    descripnewpro=input('Ingrese nueva descripcion del producto :   ')
                    cambiose.append(descripnewpro)
                    break
                elif descripcionproduct=='no':
                    descripnewpro=producto_a_modificar[1]
                    cambiose.append(descripnewpro)
                    break
            while 1:
                priceproduct=input('¿Desea cambiar precio del producto? si/no  :  ')
                priceproduct=priceproduct.strip()
                if priceproduct=='si':
                    precio1=verifiprice()
                    precioe=descripnewpro, 'Precio: $'+str(precio1)
                    precioewpro=list(precioe)
                    cambiose.append(precioewpro)
                    break
                elif descripcionproduct=='no':
                    precioe=producto_a_modificar[2]
                    cambiose.append(precioe)
                    break
                    break
            cambiose.append(producto_a_modificar[3])
            nupi[nume]=cambiose
            elimino[1]=nupi
            menu_comidas[caten]=elimino
            print(menu_comidas[caten])
    elif cualpron=='2':
        banin,nupi,elimino,caten,nume=eliminarModificarProducto('2')
        if banin==True:        
            producto_a_modificar=nupi[nume]
            cambiose=[]
            while 1:
                nameproduct=input('¿Desea cambiar nombre del producto? si/no  :  ')
                nameproduct=nameproduct.strip()
                if nameproduct=='si':
                    namenewpro=input('Ingrese nuevo nombre del producto :  ')
                    if verificarString(namenewpro)==True:
                        cambiose.append(namenewpro.upper())
                        break
                elif nameproduct=='no':
                    cambiose.append(producto_a_modificar[0])
                    break
            while 1:
                descripcionproduct=input('¿Desea cambiar descripcion del producto? si/no  :  ')
                descripcionproduct=descripcionproduct.strip()
                if descripcionproduct=='si':
                    descripnewpro=input('Ingrese nueva descripcion del producto :   ')
                    cambiose.append(descripnewpro)
                    break
                elif descripcionproduct=='no':
                    descripnewpro=producto_a_modificar[1]
                    cambiose.append(descripnewpro)
                    break
            while 1:
                priceproduct=input('¿Desea cambiar precio del producto? si/no  :  ')
                priceproduct=priceproduct.strip()
                if priceproduct=='si':
                    precio1=verifiprice()
                    precioe= 'Precio: $'+str(precio1)
                    precioe=list(precioe)
                    cambiose.append(precioe)
                    break
                elif descripcionproduct=='no':
                    precioe=producto_a_modificar[2]
                    cambiose.append(precioe)
                    break
            cambiose.append(producto_a_modificar[3])
            nupi[nume]=cambiose
            elimino[1]=nupi
            menu_cocteles[caten]=elimino
            print(menu_cocteles[caten])


def opcio (number, nombre):    
    while 1:
        if number == 2112 :
            try:
                sabor = int(input("¿Qué sabor desea?: 1. Limonada Cerezada, 2. Coco Limonada, 3. Limonada Hierba Buena    "))
                if int(sabor) == 1:
                    nombre = nombre + " -limonada cerezada"
                    break
                elif int(sabor) == 2:
                    nombre = nombre + " -coco limonada"
                    break
                elif int(sabor) == 3:
                    nombre = nombre + " -hierva buena"
                    break
            except ValueError:
                print("Ingrese un número")
        elif number == 2114:
            try :
                sabor = int(input("¿Qué sabor desea?: 1. Naranja, 2. Maracuyá, 3. Limón"))
                if sabor == 1:
                    nombre = nombre + " -naranja"
                    break
                elif sabor == 2:
                    nombre = nombre + " -maracuyá" 
                    break
                elif sabor == 3:
                    nombre = nombre + " -limón"
                    break
            except ValueError:
                print("Ingrese un número")
        elif number == 2118:
            try:
                sabor = int(input("¿Qué sabor desea?: 1. GASEOSAS QUATRO, 2. KOLA ROMAN "))
                if sabor == 1:
                    nombre = nombre + " -gaseosas quatro"
                    break
                elif sabor == 2:
                    nombre = nombre + " -kola roman"
                    break
            except ValueError:
                print("Ingrese un número")
        elif number == 2119:
            try:
                sabor = int(input("¿Qué sabor desea?: 1. GINGER, 2. SODA "))
                if sabor == 1:
                    nombre = nombre + " -ginger" 
                    break
                if sabor == 2:
                    nombre = nombre + " -soda"
                    break
            except ValueError:
                print("Ingrese un número")
        elif number == 2135:
            try:
                sabor = int(input("¿Qué sabor desea?: 1. Roja, 2. Negra, 3. Dorada, 4. Doble Malta"))
                if sabor == 1:
                    nombre = nombre + " -roja"
                    break
                elif sabor == 2:
                    nombre = nombre + " -negra"
                    break
                elif sabor == 3:
                    nombre = nombre + " -dorada"
                    break
                elif sabor == 4:
                    nombre = nombre + " -doble malta"
                    break
            except ValueError:
                print("Ingrese un número")
        else:
            break
    return nombre



####################################################################################################

while 1:
    print("¡¡¡ Bienvenid@s a OLD WEST !!! (づ ｡◕‿‿◕｡) づ  ")
    queso=input("(Ingrese un número): 1. Administrador, 2. Cajero, 3. Usuario:     "  )
    if queso=='1':
        bandera5 = True
        while bandera5 == True :
            bandera1=False
            usuarioAdm=input("Ingrese usuario: ")
            contraseñaAdm=input("Ingrese contraseña: ")
            if usuarioAdm==admin[0] and contraseñaAdm==admin[1]:
                print("Bienvenid@ Administrador :D ")
                bandera1=True
            else:
                while 1:
                    arrepentimiento=input("Usuario o contraseña incorrecta 1.Ingresar nuevamente, 2. salir")
                    if arrepentimiento =='1':
                        bandera5 = True
                        break
                    elif arrepentimiento=='2':
                        bandera5 = False
                        break
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
                                bindo=True
                                while bindo==True:
                                    eliminoCajero=input('¿Qué cajero desea eliminar?: 1. Ingrese el documento del cajero, 2. Salir: ')
                                    if eliminoCajero=='1':
                                        bindo=False
                                        mostarInfoCajero()
                                        doc,banh=verifidocum()
                                        if banh==True:
                                            contador=-1
                                            for caje in cajeros:
                                                contador+=1
                                                if str(doc)==caje[3]:
                                                    del cajeros[contador]
                                                    bandera2=True
                                            if bandera2 == False :
                                                print("Cajero no encontrado.")
                                            print(cajeros)
                                            bindo=False
                                    elif eliminoCajero=='2':
                                        bindo=False
                                        bandera2=True
                            elif cajerosOpc=='3':
                                contador2+=1                    
                                nombre=input('Ingrese su nombre o 1. Salir:  ')
                                nombre = verifinombre(nombre)
                                if nombre != "1" :
                                    documento = verifidocum()
                                    if len(str(documento)) >= 8 and len(str(documento)) <= 10 :
                                        print(autousercajero(nombre,documento))
                                        print(cajeros)
                            elif cajerosOpc=="4":
                                banderarrr=True
                                while banderarrr==True:
                                    user_modificar=input("¿Qué cajero desea modificar?: 1. Ingrese el documento del cajero, 2. Salir:")
                                    if user_modificar=='1':
                                        banderarrr=False
                                        banderamal=False
                                        mostarInfoCajero()
                                        doce,bancre=verifidocum()
                                        if bancre==True:
                                            contadormodi=-1
                                            for caji in cajeros:
                                                contadormodi+=1
                                                if str(doce)==caji[3]:       
                                                    while 1:
                                                        usuariomod=input('¿Va a modificar usuario? si/no :   ')
                                                        cambios=[]
                                                        usuariomod=usuariomod.strip()
                                                        if usuariomod =="si":
                                                            usuariocam=input('Ingrese nuevo usuario: ')
                                                            cambios.append(usuariocam)
                                                            break
                                                        elif usuariomod =="no":
                                                            cambios.append(caji[0])
                                                            break
                                                    while 1:
                                                        contraseñamod=input('¿Va a modificar contraseña? si/no :   ')
                                                        contraseñamod=contraseñamod.strip()
                                                        if contraseñamod =="si":
                                                            contraseñacam=input('Ingrese nueva contraseña: ')
                                                            cambios.append(contraseñacam)
                                                            break                                            
                                                        elif contraseñamod =="no":
                                                            cambios.append(caji[1])
                                                            break
                                                    while 1:
                                                        nombremod=input('¿Va a modificar nombre? : si/no: ')
                                                        nombremod=nombremod.strip()
                                                        if nombremod =="si":
                                                            nombrecam=input('Ingrese nuevo nombre: ')
                                                            cambios.append(nombrecam)
                                                            cambios.append(caji[3])
                                                            break
                                                        elif nombremod =="no":
                                                            cambios.append(caji[2])
                                                            cambios.append(caji[3])
                                                            break
                                                    banderamal=True
                                                    cajeros[contadormodi]=cambios
                                            if banderamal == False :
                                                print("Cajero no encontrado.")
                                    elif user_modificar=='2':
                                        banderarrr=False
                                        bandera2=True
                            elif cajerosOpc=="5":
                                bandera3 =True
                                break

                    elif hacerAdm == "2":
                        bandera4 = True

                        while bandera4 == True:
                            producOpc = input("Ingrese un número: 1. Ver productos, 2. Nuevo producto o Categoría, 3. Eliminar Producto o Categoría, 4. Modificar producto o Categoria, 5. Salir  :   ")
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
                                                bomi=True
                                                while bomi==True:
                                                    nombrecatego=input('ingrese nombre de la nueva categoria o 1. Salir   ')
                                                    if nombrecatego != "1":
                                                        conta=0
                                                        contam=0
                                                        for coma in menu_comidas:
                                                            boman=False
                                                            nombrecatego=nombrecatego.strip()
                                                            coma[0]=coma[0].strip()
                                                            if nombrecatego.lower()==coma[0].lower():
                                                                conta+=1
                                                                bomi=True
                                                                boman=True
                                                                print("categoria ya existente")
                                                            elif nombrecatego!=coma[0]:
                                                                contam+=1
                                                                if contam==len(menu_comidas):
                                                                    bomi=False
                                                                    contam=0
                                                                    conta=0
                                                                    categorianueva=[nombrecatego,[]]
                                                                    menu_comidas.append(categorianueva)
                                                                    nombrecatego=''
                                                                    while 1 :
                                                                        productopregun=input('desea ingresar productos "si" o "no"  ' )
                                                                        if productopregun=="si":
                                                                            num=str(len(menu_comidas))
                                                                            nuevoProductoComida(num)
                                                                            print('Categoría agregada con los nuevos productos')
                                                                            break
                                                                        elif productopregun=="no":
                                                                            print('Categoría agregada')
                                                                            break
                                                                elif boman==True:
                                                                    print("categoria ya existente")
                                                    elif nombrecatego == "1":
                                                        print("Categoría no agregada ")
                                                        bomi=False
                                            elif tipocatego =='2':
                                                bofi=True
                                                while bofi==True:
                                                    nombrecatego2=input('ingrese nombre de la nueva categoria o 1. Salir   ')
                                                    if nombrecatego2 != "1":
                                                        conta2=0
                                                        contam2=0
                                                        for coma in menu_cocteles:
                                                            boman2=False
                                                            nombrecatego=nombrecatego.strip()
                                                            coma[0]=coma[0].strip()
                                                            if nombrecatego2.lower()==coma[0].lower():
                                                                conta2+=1
                                                                bofi=True
                                                                boman2=True
                                                                print("categoria ya existente")
                                                            elif nombrecatego2!=coma[0]:
                                                                contam2+=1
                                                                if contam2==len(menu_cocteles):
                                                                    bofi=False
                                                                    contam2=0
                                                                    conta2=0
                                                                    categorianueva=[nombrecatego,[]]
                                                                    menu_cocteles.append(categorianueva)
                                                                    nombrecatego2=''
                                                                    while 1 :
                                                                        productopregun=input('desea ingresar productos "si" o "no"  ' )
                                                                        if productopregun=="si":
                                                                            num=str(len(menu_cocteles))
                                                                            nuevoProductoCocteles(num)
                                                                            print('Categoría agregada con los nuevos productos')
                                                                            break
                                                                        elif productopregun=="no":
                                                                            print('Categoría agregada')
                                                                            break
                                                                elif boman2==True:
                                                                    print("categoria ya existente")
                                                    elif nombrecatego2 == "1":
                                                        print("Categoría no agregada ")
                                                        bofi=False
                                            elif tipocatego=='3':
                                                break
                                    elif add == "3":
                                        break

                            elif producOpc == "3" :
                                banderaeliminar=True
                                while banderaeliminar==True: 
                                    produocate=input('¿Que desea eliminar? 1. Producto, 2. Categoría, 3.salir :   ') 
                                    if produocate=='1':
                                        banderaeliminarprod=True
                                        while banderaeliminarprod==True:
                                            cualpro=input('Ingrese un número: 1. Menú Comidas, 2. Menú Cocteles, 3. Salir : ')
                                            if cualpro == '1':
                                                bane,nup,elimino,caten,num=eliminarModificarProducto('1')
                                                if bane==True:
                                                    productoeliminado=[]
                                                    productoeliminado.append(nup.pop(num))
                                                    elimino[1]=nup
                                                    menu_comidas[caten]=elimino
                                                    banderaeliminarprod=False
                                                    print( menu_comidas[caten])
                                                elif bane==False:
                                                    banderaeliminarprod=False
                                            elif cualpro == '2':
                                                banip,nup,elimino,caten,num=eliminarModificarProducto('2')
                                                if banip==True:
                                                    productoeliminado=[]
                                                    productoeliminado.append(nup.pop(num))
                                                    elimino[1]=nup
                                                    menu_comidas[caten]=elimino
                                                    banderaeliminarprod=False
                                                    print( menu_comidas[caten])
                                                elif bane==False:
                                                    banderaeliminarprod=False
                                            elif cualpro=='3':
                                                banderaeliminarprod=False

                                    elif produocate=='2':
                                        banderaeliminarcate=True
                                        while banderaeliminarcate==True:
                                            cualcatego=input('Ingrese un número: 1. Menú Comidas, 2. Menú Cocteles, 3. Salir: ')
                                            productoeliminado=[]
                                            if cualcatego == '1':
                                                mostrarMenuComida()
                                                bandera7 , numberproduct = verificatecomidas()
                                                if bandera7==True:
                                                    productoeliminado=menu_comidas.pop(int(numberproduct)-1)
                                                    mostrarMenuComida()
                                                    banderaeliminarcate=False
                                            elif cualcatego == '2':
                                                mostrarMenuCocteles()
                                                bandera7 , numberproduct = verificatecocteles()
                                                if bandera7==True:
                                                    productoeliminado=menu_cocteles.pop(int(numberproduct)-1)
                                                    mostrarMenuCocteles()
                                                    banderaeliminarcate=False
                                            elif cualcatego=='3':
                                                 banderaeliminar=False
                                    elif produocate=='3':
                                        banderaeliminar=False
                                    
                            elif producOpc == "4" :
                                banderaeditar=True
                                while banderaeditar==True:
                                    edit=input('Editar o Modificar : 1. Producto, 2. Categoría, 3. Salir :')
                                    if edit=='1':
                                        bandenose=True
                                        while bandenose==True:
                                            cualpro=input('Ingrese un número: 1. Menú Comidas, 2. Menú Cocteles, 3. Salir : ')
                                            if cualpro=='1':
                                                modificarProductoCoctelComida('1')
                                                bandenose=False
                                            elif cualpro=='2':
                                                modificarProductoCoctelComida('2')
                                                bandenose=False
                                            elif cualpro=='3':
                                                bandenose=False

                                    elif edit=='2':
                                        banderamodificandoando=True
                                        while banderamodificandoando==True:
                                            cualcatego=input('Ingrese un número: 1. Menú Comidas, 2. Menú Cocteles, 3. Salir: ')
                                            
                                            if cualcatego == '1':
                                                mostrarMenuComida()
                                                bandera7 , numberproduct = verificatecomidas()
                                                if bandera7==True:
                                                    categoriaedicion=menu_comidas[int(numberproduct)-1]
                                                    nuevocambiose=categoriaedicion[0]
                                                    
                                                    bomi=True
                                                    while bomi==True:
                                                        edicionnombre=input('Ingrese nombre de la categoria  o 1.salir:   ')
                                                        if edicionnombre != "1":
                                                            conta=0
                                                            contam=0
                                                            for coma in menu_comidas:
                                                                bonan=False
                                                                edicionnombre=edicionnombre.strip()
                                                                coma[0]=coma[0].strip()
                                                                if edicionnombre.lower()== coma[0].lower():
                                                                    boni=False
                                                                    bonan=True
                                                                    print("categoria ya existente")
                                                                elif edicionnombre!=coma[0]:
                                                                    contam+=1
                                                                    if contam==len(menu_comidas):
                                                                        bomi=False
                                                                        contam=0
                                                                        conta=0
                                                                        edicionnombre=''
                                                                        categoriaedicion[0]=edicionnombre
                                                                        menu_comidas[int(numberproduct)-1]=categoriaedicion
                                                                        pre=input('Desea modificar productos de esa categoria :  ')
                                                                        pre.strip()
                                                                        if pre=='si':
                                                                            modificarProductoCoctelComida('1')
                                                                        elif pre=='no':
                                                                            print('ok')
                                                                        mostrarMenuComida()
                                                                        banderamodificandoando=False
                                                                    elif bonan==True:
                                                                        print("categoria ya existente")
                                                        elif edicionnombre == "1":
                                                            print("Categoría no agregada ")
                                                            bomi=False

                                            elif cualcatego == '2':
                                                mostrarMenuCocteles()
                                                bandera7 , numberproduct = verificatecocteles()
                                                if bandera7==True:
                                                    categoriaedicion=menu_cocteles[int(numberproduct)-1]
                                                    nuevocambiose=categoriaedicion[0]
                                                    bomi=True
                                                    while bomi==True:
                                                        edicionnombre=input('Ingrese nombre de la categoria  o 1.salir:   ')
                                                        if edicionnombre != "1":
                                                            conta=0
                                                            contam=0
                                                            for coma in menu_cocteles:
                                                                bonan=False
                                                                edicionnombre=edicionnombre.strip()
                                                                coma[0]=coma[0].strip()
                                                                if edicionnombre.lower()== coma[0].lower():
                                                                    boni=False
                                                                    bonan=True
                                                                    print("categoria ya existente")
                                                                elif edicionnombre!=coma[0]:
                                                                    contam+=1
                                                                    if contam==len(menu_cocteles):
                                                                        bomi=False
                                                                        contam=0
                                                                        conta=0
                                                                        edicionnombre=''
                                                                        categoriaedicion[0]=edicionnombre
                                                                        menu_cocteles[int(numberproduct)-1]=categoriaedicion
                                                                        pre=input('Desea modificar productos de esa categoria :  ')
                                                                        pre.strip()
                                                                        if pre=='si':
                                                                            modificarProductoCoctelComida('2')
                                                                        elif pre=='no':
                                                                            print('ok')
                                                                        mostrarMenuCocteles()
                                                                        banderamodificandoando=False
                                                                    elif bonan==True:
                                                                        print("categoria ya existente")
                                                        elif edicionnombre == "1":
                                                            print("Categoría no agregada ")
                                                            bomi=False


                                            elif cualcatego=='3':
                                                 banderamodificandoando=False
                                    elif edit=='3':
                                        banderaeditar=False

                            elif producOpc == "5" :
                                bandera3 = True
                                break       
                            
                    elif hacerAdm == "4":
                        bandera3 = True
                        bandera1 = False  
                        bandera5 = False


####################################################################################################          

    elif queso=='2':
        bandera6 = True
        while bandera6 == True:
            usuarioCaj=input("Ingrese usuario: ")
            contraseñaCaj=input("Ingrese contraseña: ")
            bandera8 = False
            for cajero in cajeros:    
                if usuarioCaj==cajero[0] and contraseñaCaj==cajero[1]:
                    print("Bienvenid@ Cajero ;3")
                    bandera8=True
            if bandera8 == False:
                print("Usuario o contraseña incorrecta")
            while bandera8==True:

                hacerCaj = input("(Ingrese un número) 1. Pedido, 2. Pedido Nuevo, 3. Pendientes, 4. Volver al menú: ")
                bandera9 =False
                while bandera9==False:
                    if hacerCaj=='1':
                        print("Hola")
                        print(PedidosPendientes)
                        break
                    elif hacerCaj == "2":
                        while 1: 
                            pedido = []
                            quemenu = input("¿Como desea hacer el pedido? 1. Ver menú, 2.Ingresar código, 3. Salir  ")
                            if quemenu == "1":
                                while 1 :
                                    cualmenu3 = input("1. Menú comidas, 2. Menú cocteles, 3. Confirmar pedido, 4. Salir  ") 
                                    bandera9 = True
                                    if cualmenu3 == "1":
                                        productos = comprarComida()
                                        if productos != None:
                                            productos = str(productos).replace("]", "")
                                            productos = str(productos).replace("[", "")
                                            productos = str(productos).replace("'", "")
                                            pedido.append(productos)
                                            
                                    elif cualmenu3 == "2":
                                        productos = comprarCocteles()
                                        if productos != None:
                                            productos = str(productos).replace("]", "")
                                            productos = str(productos).replace("[", "")
                                            productos = str(productos).replace("'", "")
                                            pedido.append(productos)
                                    elif cualmenu3 == "3":
                                        cambio = contodo ()
                                        pedido.append(cambio)
                                        pedido.insert(0,contadorPedidos+1)
                                        print(pedido)
                                        PedidosPendientes.append(pedido)
                                        print(PedidosPendientes)
                                        print("Pedido #" + str(contadorPedidos+1) + " guardado")
                                        break
                                    elif cualmenu3 == "4":
                                        break


                            elif quemenu == "3":
                                bandera9 = True
                                break            
                    elif hacerCaj == "4":
                        print("salir")
                        bandera8 = False
                        bandera9 = True
                        bandera6 = False
                        break 
    
####################################################################################################   

    elif queso=='3':
        bandera30=True
        while bandera30 == True:
            bandera31=False
            azul=input("(Ingrese un número) 1. Iniciar sesión, 2. Registrarse, 3. Volver al menú: ")
            if azul=='1':
                bandera31=False
                usuarioUsu=input("Ingrese usuario: ")
                contraseñaUsu=input("Ingrese contraseña: ")
                if buscar_user_pass(usuarios, usuarioUsu, contraseñaUsu):
                    print("Bienvenid@ usuario <3")
                    bandera31=True
                while bandera31==True:
                    hacerUser = input("(Ingrese un número) 1. Modificar Datos, 2. Pedido Nuevo, 3. Pedido Vigente, 4. Factura, 5. Salir: ")
                    bandera32=False
                    while bandera32==False:

                        if hacerUser=='1':
                            usuario_azulmodi = input("Confirme usuario a modificar: ")
                            fila_azulmodi = None
                            for i, fila in enumerate(usuarios):
                                if fila[0] == usuario_azulmodi:
                                    fila_azulmodi = i
                                    break
                            if fila_azulmodi is None:
                                print("El usuario ingresado no existe.")
                            else:
                                while 1:
                                    modificar_nombre = input("Desea modificar el nombre? si/no: ")
                                    if modificar_nombre.lower() == "si":
                                        nuevo_nombre = input("Ingrese el nuevo nombre: ")
                                        nuevo_nombre=verifinombre(nuevo_nombre)
                                        usuarios[fila_azulmodi][2] = nuevo_nombre
                                        break
                                    elif modificar_nombre.lower() == "no":
                                        break

                                while 1:
                                    modificar_telefono = input("Desea modificar el teléfono? si/no: ")
                                    if modificar_telefono.lower() == "si":
                                        nuevo_telefono = verifitelefono()
                                        usuarios[fila_azulmodi][4] = nuevo_telefono
                                        break
                                    elif modificar_telefono.lower() == "no":
                                        break
                                
                                while 1:
                                    modificar_direccion = input("Desea modificar la dirección? si/no: ")
                                    if modificar_direccion.lower() == "si":
                                        nueva_direccion = input("Ingrese la nueva dirección: ")
                                        usuarios[fila_azulmodi][5] = nueva_direccion
                                        break
                                    elif modificar_direccion.lower() == "no":
                                        break
                                print('Sus datos con las modificaciones: ', usuarios[fila_azulmodi])

                        elif hacerUser=='2':
                            print('hola')

            ####################################################################  

            elif azul=='2':
                contadorAzul+=1
                nombre=input('Ingrese su nombre o 1. Salir: ')
                nombre = verifinombre(nombre)
                if nombre != '1':
                    documento = verifidocum()
                    telefono = verifitelefono()
                    direccion=input('Ingrese su dirección: ')
                    print(autouser_user(nombre, documento, telefono, direccion))
    
            #################################################################### 
            elif azul =='3':
                break

            