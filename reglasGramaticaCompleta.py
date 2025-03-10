

class R1():
    def __init__(self): 
        self.id = ''
        self.TIP = '<programa>'
        self.P_Definiciones = ''
    
    def imprimir(self):
        print(self.TIP) 
        self.P_Definiciones.imprimir()
    

class R2():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Definiciones>'
        self.e = '/e'

    def imprimir(self):
        print(self.TIP) 
        print(self.e)

class R3():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Definiciones>'
        self.P_Definicion = ''
        self.P_Definiciones = ''

    def imprimir(self):
        print(self.TIP) 
        self.P_Definicion.imprimir()
        self.P_Definiciones.imprimir()
        
        
class R4():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Definicion>'
        self.P_DefVar = ''
    
    def imprimir(self):
        print(self.TIP) 
        self.P_DefVar.imprimir()
        
class R5():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Definicion>'
        self.P_DefFunc = ''

    def imprimir(self):
        print(self.TIP) 
        self.P_DefFunc.imprimir()
        
class R6():
    def __init__(self): 
        self.id = ''
        self.TIP = '<DefVar>'
        self.tipo = ''
        self.identificador = ''
        self.P_ListaVar = ''
        self.puntoYComa = ''
    
    def imprimir(self):
        print(self.TIP) 
        print(self.tipo)
        print(self.identificador)
        self.P_ListaVar.imprimir()
        print(self.puntoYComa)
        
class R7():
    def __init__(self): 
        self.id = ''
        self.TIP = '<ListaVar>'
        self.e = '/e'

    def imprimir(self):
        print(self.TIP) 
        print(self.e)


class R8():
    def __init__(self): 
        self.id = ''
        self.TIP = '<ListaVar>'
        self.coma = ''
        self.identificador = ''
        self.P_ListaVar = ''
    
    def imprimir(self):
        print(self.TIP)
        print(self.coma)
        print(self.identificador)
        self.P_ListaVar.imprimir()

class R9():
    def __init__(self): 
        self.id = ''
        self.TIP = '<DefFunc>'
        self.tipo = ''
        self.identificador = ''
        self.ParentApertura = ''
        self.P_Parametros = ''
        self.ParentCierre = ''
        self.P_BloqFunc = ''

    def imprimir(self):
        print(self.TIP)
        print(self.tipo)
        print(self.identificador)
        print(self.ParentApertura)
        self.P_Parametros.imprimir()
        print(self.ParentCierre)
        print(self.P_BloqFunc)

class R10():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Parametros>'
        self.e = '/e'

    def imprimir(self):
        print(self.TIP) 
        print(self.e)

class R11():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Parametros>'
        self.tipo = ''
        self.identificador = ''
        self.P_ListaParam = ''
    
    def imprimir(self):
        print(self.TIP) 
        print(self.tipo)
        print(self.identificador)
        self.P_ListaParam.imprimir()

class R12():
    def __init__(self): 
        self.id = ''
        self.TIP = '<ListaParam>'
        self.e = '/e'

    def imprimir(self):
        print(self.TIP) 
        print(self.e)

class R13():
    def __init__(self): 
        self.id = ''
        self.TIP = '<ListaParam>'
        self.coma = ''
        self.tipo = ''
        self.identificador = ''
        self.P_ListaParam = ''
    
    def imprimir(self):
        print(self.TIP) 
        print(self.coma)
        print(self.tipo)
        print(self.identificador)
        self.P_ListaParam.imprimir()

class R14():
    def __init__(self): 
        self.id = ''
        self.TIP = '<BloqFunc>'
        self.LlaveApertura = ''
        self.P_DefLocales = ''
        self.LlaveCierre = ''

    def imprimir(self):
        print(self.TIP)
        print(self.LlaveApertura)
        self.P_DefLocales.imprimir()
        print(self.LlaveCierre)

class R15():
    def __init__(self): 
        self.id = ''
        self.TIP = '<DefLocales>'
        self.e = '/e'

    def imprimir(self):
        print(self.TIP) 
        print(self.e)

class R16():
    def __init__(self): 
        self.id = ''
        self.TIP = '<DefLocales>'
        self.P_DefLocal = ''
        self.P_DefLocales = ''

    def imprimir(self):
        print(self.TIP) 
        self.P_DefLocal.imprimir()
        self.P_DefLocales.imprimir()

class R17():
    def __init__(self): 
        self.id = ''
        self.TIP = '<DefLocal>'
        self.P_DefVar = ''
    
    def imprimir(self):
        print(self.TIP) 
        self.P_DefVar.imprimir()
        
class R18():
    def __init__(self): 
        self.id = ''
        self.TIP = '<DefLocal>'
        self.P_Sentencia = ''
    
    def imprimir(self):
        print(self.TIP) 
        self.P_Sentencia.imprimir()
        
class R19():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Sentencias>'
        self.e = '/e'

    def imprimir(self):
        print(self.TIP) 
        print(self.e)
        
class R20():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Sentencias>'
        self.P_Sentencia = ''
        self.P_Sentencias = ''

    def imprimir(self):
        print(self.TIP) 
        self.P_Sentencia.imprimir()
        self.P_Sentencias.imprimir()

class R21():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Sentencia>'
        self.identificador = ''
        self.igual = ''
        self.P_Expresion = ''

    def imprimir(self):
        print(self.TIP) 
        print(self.identificador)
        print(self.igual)
        self.P_Expresion.imprimir()


class R22():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Sentencia>'
        self.si = ''
        self.ParentApertura = ''
        self.P_Expresion = ''
        self.ParentCierre = ''
        self.P_SentenciaBloque = ''
        self.P_Otro = ''
    
    def imprimir(self):
        print(self.TIP) 
        print(self.si)
        print(self.ParentApertura)
        self.P_Expresion.imprimir()
        print(self.ParentCierre)
        self.P_SentenciaBloque.imprimir()
        self.P_Otro.imprimir()

class R23():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Sentencia>'
        self.mientras = ''
        self.ParentApertura = ''
        self.P_Expresion = ''
        self.ParentCierre = ''
        self.P_Bloque = ''
    
    def imprimir(self):
        print(self.TIP) 
        print(self.mientras)
        print(self.ParentApertura)
        self.P_Expresion.imprimir()
        print(self.ParentCierre)
        self.P_Bloque.imprimir()
        
class R24():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Sentencia>'
        self.retornar = ''
        self.P_ValorRegresa = ''
        self.puntoYComa = ''

    def imprimir(self):
        print(self.TIP) 
        print(self.retornar)
        self.P_ValorRegresa.imprimir()
        print(self.puntoYComa)

class R25():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Sentencia>'
        self.P_LlamadFunc = ''
        self.puntoYComa = ''

    def imprimir(self):
        print(self.TIP) 
        self.P_LlamadFunc.imprimir()
        print(self.puntoYComa)
        
class R26():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Otro>'
        self.e = '/e'

    def imprimir(self):
        print(self.TIP) 
        print(self.e)
        
class R27():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Otro>'
        self.sino = ''
        self.P_SentenciaBloque = ''

    def imprimir(self):
        print(self.TIP)
        print(self.sino)  
        self.P_SentenciaBloque.imprimir()    
        

class R28():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Bloque>'
        self.LlaveApertura = ''
        self.P_Sentencias = ''
        self.LlaveCierre = ''

    def imprimir(self):
        print(self.TIP)
        print(self.LlaveApertura)
        self.P_Sentencias.imprimir()
        print(self.LlaveCierre)
        
class R29():
    def __init__(self): 
        self.id = ''
        self.TIP = '<ValorRegresa>'
        self.e = '/e'

    def imprimir(self):
        print(self.TIP) 
        print(self.e)

class R30():
    def __init__(self): 
        self.id = ''
        self.TIP = '<ValorRegresa>'
        self.P_Expresion = ''

    def imprimir(self):
        print(self.TIP) 
        self.P_Expresion.imprimir()

        
class R31():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Argumentos>'
        self.e = '/e'

    def imprimir(self):
        print(self.TIP) 
        print(self.e)
        
class R32():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Argumentos>'
        self.P_Expresion = ''
        self.P_ListaArgumentos = ''

    def imprimir(self):
        print(self.TIP) 
        self.P_Expresion.imprimir()
        self.P_ListaArgumentos.imprimir()

class R33():
    def __init__(self): 
        self.id = ''
        self.TIP = '<ListaArgumentos>'
        self.e = '/e'

    def imprimir(self):
        print(self.TIP) 
        print(self.e)
        
class R34():
    def __init__(self): 
        self.id = ''
        self.TIP = '<ListaArgumentos>'
        self.coma = ''
        self.P_Expresion = ''
        self.P_ListaArgumentos = ''

    def imprimir(self):
        print(self.TIP) 
        print(self.coma)
        self.P_Expresion.imprimir()
        self.P_ListaArgumentos.imprimir()
        
class R35():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Termino>'
        self.P_LlamadaFunc = ''

    def imprimir(self):
        print(self.TIP) 
        self.P_LlamadaFunc.imprimir()
        
class R36():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Termino>'
        self.identificador = ''

    def imprimir(self):
        print(self.TIP)
        print(self.identificador)
        
class R37():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Termino>'
        self.entero = ''

    def imprimir(self):
        print(self.TIP)
        print(self.entero)
        
class R38():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Termino>'
        self.real = ''

    def imprimir(self):
        print(self.TIP)
        print(self.real)
        
class R39():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Termino>'
        self.cadena = ''

    def imprimir(self):
        print(self.TIP)
        print(self.cadena)
        
class R40():
    def __init__(self): 
        self.id = ''
        self.TIP = '<LlamadaFunc>'
        self.identificador = ''
        self.ParentApertura = ''
        self.P_Argumentos = ''
        self.ParentCierre = ''

    def imprimir(self):
        print(self.TIP)
        print(self.identificador)
        print(self.ParentApertura)
        self.P_Argumentos.imprimir()
        print(self.ParentCierre)
        
class R41():
    def __init__(self): 
        self.id = ''
        self.TIP = '<SentenciaBloque>'
        self.P_Sentencia = ''

    def imprimir(self):
        print(self.TIP) 
        self.P_Sentencia.imprimir()
        
class R42():
    def __init__(self): 
        self.id = ''
        self.TIP = '<SentenciaBloque>'
        self.P_Bloque = ''

    def imprimir(self):
        print(self.TIP) 
        self.P_Bloque.imprimir()
        
class R43():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Expresion>'
        self.ParentApertura = ''
        self.P_Expresion = ''
        self.ParentCierre = ''

    def imprimir(self):
        print(self.TIP)
        print(self.ParentApertura)
        self.P_Expresion.imprimir()
        print(self.ParentCierre)
        
class R44():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Expresion>'
        self.opSuma = ''
        self.P_Expresion = ''

    def imprimir(self):
        print(self.TIP)
        print(self.opSuma)
        self.P_Expresion.imprimir()
        
class R45():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Expresion>'
        self.opNot = ''
        self.P_Expresion = ''

    def imprimir(self):
        print(self.TIP)
        print(self.opNot)
        self.P_Expresion.imprimir()
        
class R46():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Expresion>'
        self.opMul = ''
        self.P_Expresion = ''

    def imprimir(self):
        print(self.TIP)
        self.P_Expresion.imprimir()
        print(self.opMul)
        self.P_Expresion.imprimir()
        
class R47():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Expresion>'
        self.opSuma = ''
        self.P_Expresion = ''

    def imprimir(self):
        print(self.TIP)
        self.P_Expresion.imprimir()
        print(self.opSuma)
        self.P_Expresion.imprimir()
        
class R48():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Expresion>'
        self.opRelac = ''
        self.P_Expresion = ''

    def imprimir(self):
        print(self.TIP)
        self.P_Expresion.imprimir()
        print(self.opRelac)
        self.P_Expresion.imprimir()
        
class R49():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Expresion>'
        self.opIgualdad = ''
        self.P_Expresion = ''

    def imprimir(self):
        print(self.TIP)
        self.P_Expresion.imprimir()
        print(self.opIgualdad)
        self.P_Expresion.imprimir()
        
class R50():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Expresion>'
        self.opAnd = ''
        self.P_Expresion = ''

    def imprimir(self):
        print(self.TIP)
        self.P_Expresion.imprimir()
        print(self.opAnd)
        self.P_Expresion.imprimir()
        
class R51():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Expresion>'
        self.opOr = ''
        self.P_Expresion = ''

    def imprimir(self):
        print(self.TIP)
        self.P_Expresion.imprimir()
        print(self.opOr)
        self.P_Expresion.imprimir()
        
class R52():
    def __init__(self): 
        self.id = ''
        self.TIP = '<Expresion>'
        self.P_Termino = ''
    
    def imprimir(self):
        print(self.TIP)
        self.P_Termino.imprimir()