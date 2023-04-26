admin=['adminsap','admin123']
cajeros=[['cajeand','sharon123', 'Sharon Andreina', '1092387960'],['cajeang','angel123', 'Angel Daniel', '1093293435'], ['cajealj', 'paula123', 'Paula', '1090371768']]

usuarios=[['user1', 'pass1', 'Alicia', '12345678', '0000000000', 'País de las maravillas', '0'], ['user2', 'pass2', 'Naruto', '87654321', '1111111111', 'Aldea Oculta de la Hoja','0']]

def validacion(usu,contra):
    bandera=False
    if admin[0]==usu and admin[1]==contra:  
        bandera=True
        return bandera
    elif admin[0]!=usu and admin[1]!=contra:
        bandera=False
        return bandera
        
def validacion1(usu,contra):
    contadorUser=0
    coma=0
    bandera=False
    for usi in usuarios:
        if usi[0]==usu and usi[1]==contra: 
            contadorUser+=1 
            bandera=True
            return bandera
        elif usi[0]!=usu and usi[1]!=contra:
            coma+=1
            bandera=False
            if coma==len(usuarios):
                return bandera
        
def validacion2(usu,contra):
    contadorCajeros=0
    coma=0
    bandera=False
    for us in cajeros:
        if us[0]==usu and us[1]==contra:  
            contadorCajeros+=1
            bandera=True
            return bandera
        elif us[0]!=usu and us[1]!=contra:
            coma+=1
            bandera=False
            if coma==len(cajeros):
                return bandera

usuario=input('Ingrese usuario :   ')
contraseña=input('Ingrese contraseña :    ')
bandiri=validacion(usuario,contraseña)
bandere=validacion1(usuario,contraseña)
bandara=validacion2(usuario,contraseña)

if bandiri==True:
    print('administrador')
elif bandere==True:
    print('usuario')
elif bandara==True:
    print('cajero')