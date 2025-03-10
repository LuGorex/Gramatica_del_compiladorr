from ast import NodeVisitor
from tkinter import font
from token import NUMBER
from turtle import width
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from ui_mainwindow import Ui_MainWindow
import numpy as np
#from tabulate import tabulate
from colorama import init, Fore, Back, Style
import networkx as nx  
import matplotlib.pyplot as plt  
import reglasGramaticaCompleta


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        header = self.ui.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.ui.pushButton.clicked.connect(self.Automata)
        

    @Slot()
    def Automata(self): 
        #Pila de strings
        pila2 = []
        pila2.append('$')
        pila2.append('0')
        entrada2 = []
        #print(pila2, entrada2)
        
        #Pila de enteros
        pila = []
        pila.append('23')
        pila.append('0')
        entrada = []
        
        matrizLR = [['','','','','d5','','','','','','','','','','','','','','','','','','','r2','1','2','3','4','','6','','','','','','','','','','','','','','','',''], #0
                    ['','','','','','','','','','','','','','','','','','','','','','','','r0','','','','','','','','','','','','','','','','','','','','','',''], #1
                    ['','','','','','','','','','','','','','','','','','','','','','','','r1','','','','','','','','','','','','','','','','','','','','','',''], #2
                    ['','','','','d5','','','','','','','','','','','','','','','','','','','r2','','7','3','4','','6','','','','','','','','','','','','','','','',''], #3
                    ['','','','','r4','','','','','','','','','','','','','','','','','','','r4','','','','','','','','','','','','','','','','','','','','','',''], #4
                    ['d8','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #5
                    ['','','','','r5','','','','','','','','','','','','','','','','','','','r5','','','','','','','','','','','','','','','','','','','','','',''], #6
                    ['','','','','','','','','','','','','','','','','','','','','','','','r3','','','','','','','','','','','','','','','','','','','','','',''], #7
                    ['','','','','','','','','','','','','r7','d10','d11','','','','','','','','','','','','','','9','','','','','','','','','','','','','','','','',''], #8
                    ['','','','','','','','','','','','','d12','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #9
                    ['d13','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #10
                    ['','','','','d15','','','','','','','','','','','r10','','','','','','','','','','','','','','','14','','','','','','','','','','','','','','',''], #11
                    ['r6','','','','r6','','','','','','','','','','','','','r6','','r6','r6','r6','','r6','','','','','','','','','','','','','','','','','','','','','',''], #12
                    ['','','','','','','','','','','','','r7','d10','','','','','','','','','','','','','','','16','','','','','','','','','','','','','','','','',''], #13
                    ['','','','','','','','','','','','','','','','d17','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #14
                    ['d18','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #15
                    ['','','','','','','','','','','','','r8','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #16
                    ['','','','','','','','','','','','','','','','','d20','','','','','','','','','','','','','','','','19','','','','','','','','','','','','',''], #17
                    ['','','','','','','','','','','','','','d22','','r12','','','','','','','','','','','','','','','','21','','','','','','','','','','','','','',''], #18
                    ['','','','','r9','','','','','','','','','','','','','','','','','','','r9','','','','','','','','','','','','','','','','','','','','','',''], #19
                    ['d27','','','','d5','','','','','','','','','','','','','r15','','d28','d29','d30','','','','','','25','','','','','','23','24','','26','','','','','','','31','',''], #20
                    ['','','','','','','','','','','','','','','','r11','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #21
                    ['','','','','d32','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #22
                    ['','','','','','','','','','','','','r8','','','','','d33','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #23
                    ['d27','','','','d5','','','','','','','','','','','','','r15','','d28','d29','d30','','','','','','25','','','','','','34','24','','26','','','','','','','31','',''], #24
                    ['r17','','','','r17','','','','','','','','','','','','','r17','','r17','r17','r17','','','','','','','','','','','','','','','','','','','','','','','',''], #25
                    ['r18','','','','r18','','','','','','','','','','','','','r18','','r18','r18','r18','','','','','','','','','','','','','','','','','','','','','','','',''], #26
                    ['','','','','','','','','','','','','','','d36','','','','d35','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #27
                    ['','','','','','','','','','','','','','','d37','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #28
                    ['','','','','','','','','','','','','','','d38','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #29
                    ['d46','d47','d48','d49','','d42','','','','','d43','','r29','','d41','','','','','','','','','','','','','','','','','','','','','','','','','39','','','44','45','','40'], #30
                    ['','','','','','','','','','','','','d50','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #31
                    ['d51','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #32
                    ['','','','','r14','','','','','','','','','','','','','','','','','','','r14','','','','','','','','','','','','','','','','','','','','','',''], #33
                    ['','','','','','','','','','','','','','','','','','r16','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #34
                    ['d46','d47','d48','d49','','d42','','','','','d43','','','','d41','','','','','','','','','','','','','','','','','','','','','','','','','','','','44','45','','52'], #35
                    ['d46','d47','d48','d49','','d42','','','','','d43','','r29','','d41','r31','','','','','','','','','','','','','','','','','','','','','','','','','53','','44','45','','54'], #36
                    ['d46','d47','d48','d49','','d42','','','','','d43','','r29','','d41','','','','','','','','','','','','','','','','','','','','','','','','','','','','44','45','','55'], #37
                    ['d46','d47','d48','d49','','d42','','','','','d43','','r29','','d41','','','','','','','','','','','','','','','','','','','','','','','','','','','','44','45','','56'], #38
                    ['','','','','','','','','','','','','d57','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #39
                    ['','','','','','d59','d58','d60','d63','d62','','d61','r30','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #40
                    ['d46','d47','d48','d49','','d42','','','','','d43','','','','d41','','','','','','','','','','','','','','','','','','','','','','','','','','','','44','45','','64'], #41
                    ['d46','d47','d48','d49','','d42','','','','','d43','','','','d41','','','','','','','','','','','','','','','','','','','','','','','','','','','','44','45','','65'], #42
                    ['d46','d47','d48','d49','','d42','','','','','d43','','','','d41','','','','','','','','','','','','','','','','','','','','','','','','','','','','44','45','','66'], #43
                    ['','','','','','r52','r52','r52','r52','r52','','r52','r52','r52','','r52','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #44
                    ['','','','','','r35','r35','r35','r35','r35','','r35','r35','r35','','r35','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #45
                    ['','','','','','r36','r36','r36','r36','r36','','r36','r36','r36','d36','r36','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #46
                    ['','','','','','r37','r37','r37','r37','r37','','r37','r37','r37','','r37','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #47
                    ['','','','','','r38','r38','r38','r38','r38','','r38','r38','r38','','r38','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #48
                    ['','','','','','r39','r39','r39','r39','r39','','r39','r39','r39','','r39','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #49
                    ['r25','','','','r25','','','','','','','','','','','','','r25','','r25','r25','r25','r25','','','','','','','','','','','','','','','','','','','','','','',''], #50
                    ['','','','','','','','','','','','','','d22','','r12','','','','','','','','','','','','','','','','67','','','','','','','','','','','','','',''], #51
                    ['','','','','','d59','d58','d60','d63','d62','','d61','d68','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #52
                    ['','','','','','','','','','','','','','','','d69','','','','','','','','','','','','','','','','67','','','','','','','','','','','','','',''], #53
                    ['','','','','','d59','d58','d60','d63','d62','','d61','','d71','','r33','','','','','','','','','','','','','','','','','','','','','','','','','','70','','','',''], #54
                    ['','','','','','d59','d58','d60','d63','d62','','d61','','','','d72','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #55
                    ['','','','','','d59','d58','d60','d63','d62','','d61','','','','d73','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #56
                    ['r24','','','','r24','','','','','','','','','','','','','r24','','r24','r24','r24','r24','','','','','','','','','','','','','','','','','','','','','','',''], #57
                    ['d46','d47','d48','d49','','d42','','','','','d43','','','','d41','','','','','','','','','','','','','','','','','','','','','','','','','','','','44','45','','74'], #58
                    ['d46','d47','d48','d49','','d42','','','','','d43','','','','d41','','','','','','','','','','','','','','','','','','','','','','','','','','','','44','45','','75'], #59
                    ['d46','d47','d48','d49','','d42','','','','','d43','','','','d41','','','','','','','','','','','','','','','','','','','','','','','','','','','','44','45','','76'], #60
                    ['d46','d47','d48','d49','','d42','','','','','d43','','','','d41','','','','','','','','','','','','','','','','','','','','','','','','','','','','44','45','','77'], #61
                    ['d46','d47','d48','d49','','d42','','','','','d43','','','','d41','','','','','','','','','','','','','','','','','','','','','','','','','','','','44','45','','78'], #62
                    ['d46','d47','d48','d49','','d42','','','','','d43','','','','d41','','','','','','','','','','','','','','','','','','','','','','','','','','','','44','45','','79'], #63
                    ['','','','','','d59','d58','d60','d63','d62','','d61','','','','d80','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #64
                    ['','','','','','r44','r44','r44','r44','r44','','r44','r44','r44','','r44','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #65
                    ['','','','','','r45','r45','r45','r45','r45','','r45','r45','r45','','r45','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #66
                    ['','','','','','','','','','','','','','','','r13','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #67
                    ['r21','','','','r21','','','','','','','','','','','','','r21','','r21','r21','r21','r21','','','','','','','','','','','','','','','','','','','','','','',''], #68
                    ['','','','','','r40','r40','r40','r40','40','','r40','r40','r40','','r40','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #69
                    ['','','','','','','','','','','','','','','','r32','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #70
                    ['d46','d47','d48','d49','','d42','','','','','d43','','','','d41','','','','','','','','','','','','','','','','','','','','','','','','','','','','44','45','','81'], #71
                    ['d27','','','','','','','','','','','','','','','','d85','','','d28','d29','d30','','','','','','','','','','','','','','','83','','84','','','','','31','82',''], #72
                    ['','','','','','','','','','','','','','','','','d85','','','','','','','','','','','','','','','','','','','','','','86','','','','','','',''], #73
                    ['','','','','','r46','r46','r46','r46','r46','','r46','r46','r46','','r46','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #74
                    ['','','','','','r47','d58','r47','r47','r47','','r47','r47','r47','','r47','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #75
                    ['','','','','','d59','d58','r48','r48','r48','','r48','r48','r48','','r48','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #76
                    ['','','','','','d59','d58','d60','r49','r49','','r49','r49','r49','','r49','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #77
                    ['','','','','','d59','d58','d60','r50','r50','','d61','r50','r50','','r50','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #78
                    ['','','','','','d59','d58','d60','r51','d62','','d61','r51','r51','','r51','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #79
                    ['','','','','','r43','r43','r43','r43','r43','','r43','r43','r43','','r43','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #80
                    ['','','','','','d59','d58','d60','d63','d62','','d61','','d71','','r33','','','','','','','','','','','','','','','','','','','','','','','','','','87','','','',''], #81
                    ['r26','','','','r26','','','','','','','','','','','','','r26','','r26','r26','r26','r89','','','','','','','','','','','','','','','88','','','','','','','',''], #82
                    ['r41','','','','r41','','','','','','','','','','','','','r41','','r41','r41','r41','r41','','','','','','','','','','','','','','','88','','','','','','','',''], #83
                    ['r42','','','','r42','','','','','','','','','','','','','r42','','r42','r42','r42','r42','','','','','','','','','','','','','','','88','','','','','','','',''], #84
                    ['d27','','','','','','','','','','','','','','','','','r19','','d28','d29','d30','','','','','','','','','','','','','','90','91','','','','','','','31','',''], #85
                    ['r23','','','','r23','','','','','','','','','','','','','r23','','r23','r23','r23','r23','','','','','','','','','','','','','','','88','','','','','','','',''], #86
                    ['','','','','','','','','','','','','','','','r34','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #87
                    ['r22','','','','r22','','','','','','','','','','','','','r22','','r22','r22','r22','r22','','','','','','','','','','','','','','','','','','','','','','',''], #88
                    ['d27','','','','','','','','','','','','','','','','d85','','','d28','d29','d30','','','','','','','','','','','','','','','83','','84','','','','','31','92',''], #89
                    ['','','','','','','','','','','','','','','','','','d93','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #90
                    ['d27','','','','','','','','','','','','','','','','','r19','','d28','d29','d30','','','','','','','','','','','','','','94','91','','','','','','','31','',''], #91
                    ['r27','','','','r27','','','','','','','','','','','','','r27','','r27','r27','r27','','','','','','','','','','','','','','','','','','','','','','','',''], #92
                    ['r28','','','','r28','','','','','','','','','','','','','r28','','r28','r28','r28','r28','','','','','','','','','','','','','','','','','','','','','','',''], #93
                    ['','','','','','','','','','','','','','','','','','r20','','','','','','','','','','','','','','','','','','','','','','','','','','','',''], #94
                    ]        
     

        #Variables iniciales
        elementos=[]
        estado = 0
        indice = 0
        cadena = self.ui.textEdit.toPlainText().strip() + '$'
        while(indice<=(len(cadena)-1)  and estado==0):  
                #Se inicializan las siguientes variables
                lexema=''
                token='error'
                num=-1
                #Mientras el indice sea menor a la longitud de la cadena y NO se encuentre en el estado 20
                while(indice<=(len(cadena)-1) and estado!=20):
                    if estado==0:#Si está en el estado inicial
                        #Si en la posición cadena[indice] hay espacio en blanco
                        if(cadena[indice].isspace()):
                            estado=0 #El estado se establece como el inicial
                        #Si en la posición cadena[indice] hay una letra o un guión bajo
                        elif cadena[indice].isalpha() or cadena[indice]=='_':

                            esTipoDeDato = False
                            intV = cadena[indice:indice+3]        
                            floatV = cadena[indice:indice+5]
                            voidV = cadena[indice:indice+4]
                            stringV = cadena[indice:indice+6]

                            ifV = cadena[indice:indice+2]
                            elseV = cadena[indice:indice+4]
                            whileV = cadena[indice:indice+5]
                            returnV = cadena[indice:indice+6]
                            
                            if(intV == "int"):#append
                                entrada.append('4')
                                entrada2.append('int')
                                esTipoDeDato=True
                                #Reuniendo los datos correspondientes y agregandolos a lista de elementos
                                lexema='int'
                                token='tipo de dato'
                                num=4
                                elementos.append({'token':token,'num':num,'lexema':lexema})
                            elif(floatV == "float"):
                                entrada.append('4')
                                entrada2.append('float')
                                esTipoDeDato=True
                                intV=cadena[indice:indice+5]
                                lexema='float'
                                token='tipo de dato'
                                num=4
                                elementos.append({'token':token,'num':num,'lexema':lexema})
                            elif(voidV == "void"):
                                entrada.append('4')
                                entrada2.append('void')
                                esTipoDeDato=True 
                                intV=cadena[indice:indice+4]
                                lexema='void'
                                token='tipo de dato'
                                num=4
                                elementos.append({'token':token,'num':num,'lexema':lexema})
                            elif(stringV == "string"):
                                entrada.append('4')
                                entrada2.append('string')
                                esTipoDeDato=True 
                                intV=cadena[indice:indice+6]
                                lexema='string'
                                token='tipo de dato'
                                num=4
                                elementos.append({'token':token,'num':num,'lexema':lexema})
                            elif(ifV == "if"):
                                entrada.append('19')
                                entrada2.append('if')
                                esTipoDeDato=True 
                                intV=cadena[indice:indice+2]
                                lexema='if'
                                token='if'
                                num=19
                                elementos.append({'token':token,'num':num,'lexema':lexema})
                            elif(elseV == "else"):
                                entrada.append('22')
                                entrada2.append('else')
                                esTipoDeDato=True 
                                intV=cadena[indice:indice+4]  
                                lexema='else'
                                token='else'
                                num=22
                                elementos.append({'token':token,'num':num,'lexema':lexema})
                            elif(whileV == "while"):
                                entrada.append('20')
                                entrada2.append('while')
                                esTipoDeDato=True
                                intV=cadena[indice:indice+5] 
                                lexema='while'
                                token='while'
                                num=20
                                elementos.append({'token':token,'num':num,'lexema':lexema})
                            elif(returnV == "return"):
                                entrada.append('21')
                                entrada2.append('return')
                                esTipoDeDato=True  
                                intV=cadena[indice:indice+6]
                                lexema='return'
                                token='return'
                                num=21
                                elementos.append({'token':token,'num':num,'lexema':lexema})         
                            else:
                                estado=4 #La variable estado se establece con el número 4
                                lexema+=cadena[indice] #Al lexema se le agrega el contenido de cadena[indice]
                                token='identificador' #El token se define como un identificador
                                num=0 #La variable num se establece con el número 0
                                entrada.append(num)
                     
                            if(esTipoDeDato==True):
                                indice += len(intV)          
                                lexema = cadena[indice]
                                #print("Lexema: ", lexema)
                            
                            #entrada2.append(lexema)
                        #Si en la posición cadena[indice] hay un $ (fin de cadena)
                        elif cadena[indice]=='$':
                            estado=20 #Se establece el estado como el final
                            lexema+=cadena[indice] #Al lexema se le agrega el contenido de cadena[indice]
                            token='$'  #El token se define como un signo de pesos o final de cadena
                            num=23       #2
                            entrada.append(num)
                            #entrada2.append(lexema)
                        elif cadena[indice].isdigit():
                            lexema+=cadena[indice]
                            token='entero'
                            estado=6 
                            num=1
                            #entrada.append(num)
                        elif cadena[indice]=='"':
                            lexema=cadena[indice]
                            estado=11
                            indice+=1
                        elif cadena[indice]=='=':
                            lexema+=cadena[indice]
                            token='='
                            estado=5  
                            num=18  
                        elif cadena[indice]=='+' or cadena[indice]=='-':
                            lexema+=cadena[indice]
                            token='opSuma'
                            estado=20
                            num=5 
                            entrada.append(num)
                            #entrada2.append(lexema)
                        elif cadena[indice]=='*' or cadena[indice]=='/':
                            lexema+=cadena[indice]
                            token='opMul'
                            estado=20 
                            num=6
                            entrada.append(num)
                        elif cadena[indice]=='<' or cadena[indice]=='<=' or cadena[indice]=='>' or cadena[indice]=='>=':
                            lexema+=cadena[indice]
                            token='opRelac'
                            estado=20 
                            num=7 
                            entrada.append(num)
                        elif cadena[indice]=='||':
                            lexema+=cadena[indice]
                            token='opOr'
                            estado=20 
                            num=8
                            entrada.append(num)  
                        elif cadena[indice]=='&&':
                            lexema+=cadena[indice]
                            token='opAnd'
                            estado=20 
                            num=9
                            entrada.append(num)
                        elif cadena[indice]=='!':
                            lexema+=cadena[indice]
                            token='opNot'
                            estado=10 
                            num=10   
                            entrada.append(num)
                        elif cadena[indice]==';':
                            lexema+=cadena[indice]
                            token=';'
                            estado=20 
                            num=12 
                            entrada.append(num)
                        elif cadena[indice]==',':
                            lexema+=cadena[indice]
                            token=','
                            estado=20 
                            num=13 
                            entrada.append(num)
                        elif cadena[indice]=='(':
                            lexema+=cadena[indice]
                            token='('
                            estado=20 
                            num=14
                            entrada.append(num) 
                        elif cadena[indice]==')':
                            lexema+=cadena[indice]
                            token=')'
                            estado=20 
                            num=15
                            entrada.append(num)
                        elif cadena[indice]=='{':
                            lexema+=cadena[indice]
                            token='{'
                            estado=20 
                            num=16
                            entrada.append(num) 
                        elif cadena[indice]=='}':
                            lexema+=cadena[indice]
                            token='}'
                            estado=20 
                            num=17
                            entrada.append(num)
                        #Si NO hay un espacio en blanco o alguno de los tokens válidos       
                        else:
                            estado=20 #Se establece el estado como el final
                            token='error' #El token se define como un error
                            lexema=cadena[indice] #Al lexema se le agrega el contenido de cadena[indice]
                            num=-1 #La variable num se establece con el número -1
                        indice+=1 #Se le suma 1 a la variable indice (se pasa a la siguiente posición)
                    elif estado==4:
                        #Si en la posición cadena[indice] hay un digito, una letra o un guión bajo
                        if cadena[indice].isdigit() or cadena[indice].isalpha() or cadena[indice]=='_':
                            estado=4 #Se establece el estado como el 4
                            lexema+=cadena[indice] #Al lexema se le agrega el contenido de cadena[indice]
                            token='identificador' #El token se define como un identificador
                            indice+=1 #Se le suma 1 a la variable indice (se pasa a la siguiente posición)
                            num=0 #La variable num se establece con el número 1
                            #entrada.append(num)
                            #entrada2.append(lexema)
                        #Si en la posición cadena[indice] NO hay un digito, una letra o un guión bajo
                        else:
                            estado=20 #Se establece el estado como el final
                    elif estado==5:
                        #Si en la posición cadena[indice] NO hay un "="
                        if cadena[indice]!='=':
                            estado=20 #Se establece el estado como el final
                            entrada.append(num)
                        #Si en la posición cadena[indice] NO hay un "="
                        else:
                            estado=20 #Se establece el estado como el final
                            lexema+=cadena[indice] #Al lexema se le agrega el contenido de cadena[indice]
                            token='opIgualdad' #El token se define como un operador de igualdad
                            indice+=1 #Se le suma 1 a la variable indice (se pasa a la siguiente posición)
                            num=11 #La variable num se establece con el número 11
                            entrada.append(num)
                    elif estado==6:
                        if cadena[indice].isdigit():
                            estado=7 
                            lexema+=cadena[indice] 
                            token='entero' 
                            indice+=1 
                            num=1         
                        if cadena[indice]=='.':
                            estado=7
                            lexema+=cadena[indice]
                            indice+=1
                        else:
                            estado=20  
                            entrada.append(num)
                    elif estado==7:
                        if cadena[indice].isdigit():
                            estado=8
                            lexema+=cadena[indice]
                            token='real'
                            indice+=1
                            num=2
                            entrada.append(num)
                        if cadena[indice]=='.':
                            estado=8
                            lexema+=cadena[indice]
                            indice+=1
                        else:
                            estado=20
                    elif estado==8:
                        if cadena[indice].isdigit():
                            estado=9
                            lexema+=cadena[indice]
                            token='real'
                            indice+=1
                            num=2
                            entrada.append(num)
                        else:
                            estado=20
                    elif estado==9:
                        if cadena[indice].isdigit():
                            estado=20
                            lexema+=cadena[indice]
                            token='real'
                            indice+=1
                            num=2
                            entrada.append(num)
                        else:
                            estado=20
                    elif estado==10:
                        if cadena[indice]!='=':
                            estado=20
                        else:
                            estado=20
                            lexema+=cadena[indice]
                            token='opIgualdad'
                            indice+=1
                            num=11
                            entrada.append(num)
                    elif estado==11:
                        indice=indice-1
                        if cadena[indice]=='"':  #cadena = ""
                            estado=20
                            lexema+=cadena[indice]
                            token='cadena'
                            num=3
                            entrada.append(num)
                        else:
                            while(indice<=(len(cadena)-1) and cadena[indice]!='"'): 
                                lexema+=cadena[indice]
                                token='cadena'                                
                                indice+=1
                            lexema+=cadena[indice]
                            num=3
                            indice+=1
                            entrada.append(num)
                            estado=20 
                            #lexema=""
                        
                estado = 0
                elementos.append({'token':token,'num':num,'lexema':lexema})
                #print(lexema)
                entrada2.append(lexema)
        
        init(autoreset=True)
        
        #Análisis LR con pila de enteros
        print('\n')      
        print("{:^100}".format(Fore.YELLOW+'Análisis LR(1) con Pila de Enteros'))
        print('{:<40}{:<20}{:>50}'.format(Fore.CYAN+'Pila',Fore.CYAN+'Entrada',Fore.CYAN+'Salida')) 
        
        #Análisis LR con pila de strings
        # print('\n')      
        # print("{:^130}".format(Fore.YELLOW+'Análisis LR(1) con Pila de strings'))
        # print('{:^50}{:^40}{:^18}'.format(Fore.CYAN+'Pila',Fore.CYAN+'Entrada',Fore.CYAN+'Salida'))
        
        while(True):
            #Pila de enteros
            #print("Entrada: ",entrada)
            x = int(entrada[0]) 
            #print("x: ",x)           
            #print("Pila: ",pila)
            y = int(pila[len(pila)-1])
            #print("Y: ",y)

            salida = matrizLR[y][x]
            #print("Salida: ",salida)
            
            #Pila de strings
            x2 = entrada2[0]
           
            #Análisis LR con pila de enteros
            print('{:<40}{:<20}{:<6}'.format(Fore.YELLOW+str(pila),Fore.GREEN+str(entrada),Fore.MAGENTA+salida))
            
            #Análisis LR con pila de strings
            
            #print('{:^50}{:^40}{:>15}'.format(Fore.YELLOW+str(pila2),Fore.GREEN+str(entrada2),Fore.MAGENTA+salida))
            
            validar  = salida[1:len(salida)]
            #print("validar: ",validar)

            if(salida == ''):
                print('ERROR!')
                QMessageBox.information(self,'Mensaje','Cadena rechazada!')
                break
            if(salida == 'r0'):
                QMessageBox.information(self,'Mensaje','Cadena aceptada!')
                break
            
            if(salida[0] == 'd'):
                
                #Pila de enteros
                pila.append(x)
                #print("Salida: ",salida)
                aux =  salida[1:len(salida)]      #let numE = coordenada.substring(1,coordenada.length)
                pila.append(aux)    
                #print("Aux",aux,"\n\n")

                #Pila de strings
                pila2.append(x2)
                pila2.append(salida[1:len(salida)])  

                entrada.pop(0)  
                entrada2.pop(0)
                                
            elif(salida[0] == 'r'):
                if(validar == '1'):
                    objR1 = reglasGramaticaCompleta.R1()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][24])
                    
                    pila.append('24')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()

                    pila2.append('24')
                    pila2.append(aux)

                elif(validar == '2'):
                    objR2 = reglasGramaticaCompleta.R2()
                    #Aqui no se hace ningun pop por el unico token que hay es "vacío"
                    #Pila de enteros
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][25])

                    pila.append('25')
                    pila.append(aux)

                    #Pila de strings
                    pila2.append('25')
                    pila2.append(aux)

                elif(validar == '3'):
                    objR3 = reglasGramaticaCompleta.R3()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][25])

                    pila.append('25')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('25')
                    pila2.append(aux)

                elif(validar == '4'):
                    objR4 = reglasGramaticaCompleta.R4()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][26])

                    pila.append('26')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()

                    pila2.append('26')
                    pila2.append(aux)

                elif(validar == '5'):
                    objR5 = reglasGramaticaCompleta.R5()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][26])

                    pila.append('26')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()

                    pila2.append('26')
                    pila2.append(aux)

                elif(validar == '6'):
                    objR6 = reglasGramaticaCompleta.R6()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][27])

                    pila.append('27')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('27')
                    pila2.append(aux)

                elif(validar == '7'):
                    objR7 = reglasGramaticaCompleta.R7()
                    #Aqui no se hace ningun pop por el unico token que hay es "vacío"
                    #Pila de enteros
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][28])

                    pila.append('28')
                    pila.append(aux)

                    #Pila de strings 
                    pila2.append('28')
                    pila2.append(aux)

                elif(validar == '8'):
                    objR8 = reglasGramaticaCompleta.R8()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][28])

                    pila.append('28')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('28')
                    pila2.append(aux)

                elif(validar == '9'):
                    objR9 = reglasGramaticaCompleta.R9()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][29])

                    pila.append('29')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('29')
                    pila2.append(aux)

                elif(validar == "10"):       #salida[1:len(salida)-1]=='10'   
                    objR10 = reglasGramaticaCompleta.R10()
                    #Aqui no se hace ningun pop por el unico token que hay es "vacío"
                    #Pila de enteros
                    #print("dimecion de pila: ",len(pila))
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][30])

                    pila.append('30')
                    pila.append(aux)

                    #Pila de strings
                    pila2.append('30')
                    pila2.append(aux)

                elif(validar == "11"):
                    objR11 = reglasGramaticaCompleta.R11()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][30])

                    pila.append('30')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('30')
                    pila2.append(aux)

                elif(validar == "12"):
                    objR12 = reglasGramaticaCompleta.R12()
                    #Aqui no se hace ningun pop por el unico token que hay es "vacío"
                    #Pila de enteros 
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][31])

                    pila.append('31')
                    pila.append(aux)

                    #Pila de strings
                    pila2.append('31')
                    pila2.append(aux)

                elif(validar == "13"):
                    objR13 = reglasGramaticaCompleta.R13()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][31])

                    pila.append('31')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('31')
                    pila2.append(aux)

                elif(validar == "14"):
                    objR14 = reglasGramaticaCompleta.R14()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][32])

                    pila.append('32')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('32')
                    pila2.append(aux)

                elif(validar == "15"):
                    objR15 = reglasGramaticaCompleta.R15()
                    #Aqui no se hace ningun pop por el unico token que hay es "vacío"
                    #Pila de enteros
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][33])

                    pila.append('33')
                    pila.append(aux)

                    #Pila de strings
                    pila2.append('33')
                    pila2.append(aux)

                elif(validar == "16"):
                    objR16 = reglasGramaticaCompleta.R16()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][33])

                    pila.append('33')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('33')
                    pila2.append(aux)
                    
                elif(validar == "17"):
                    objR17 = reglasGramaticaCompleta.R17()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][34])

                    pila.append('34')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()

                    pila2.append('34')
                    pila2.append(aux)
                    
                elif(validar == "18"):
                    objR18 = reglasGramaticaCompleta.R18()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][34])

                    pila.append('34')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()

                    pila2.append('34')
                    pila2.append(aux)
    
                elif(validar == "19"):
                    objR19 = reglasGramaticaCompleta.R19()
                    #Aqui no se hace ningun pop por el unico token que hay es "vacío"
                    #Pila de eneteros 
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][35])

                    pila.append('35')
                    pila.append(aux)

                    #Pila de strings
                    pila2.append('35')
                    pila2.append(aux)

                elif(validar == "20"):
                    objR20 = reglasGramaticaCompleta.R20()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][35])

                    pila.append('35')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('35')
                    pila2.append(aux)
                    
                elif(validar == "21"):
                    objR21 = reglasGramaticaCompleta.R21()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][36])

                    pila.append('36')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('36')
                    pila2.append(aux)

                elif(validar == "22"):
                    objR22 = reglasGramaticaCompleta.R22()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][36])

                    pila.append('36')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('36')
                    pila2.append(aux)

                elif(validar == "23"):
                    objR23 = reglasGramaticaCompleta.R23()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][36])

                    pila.append('36')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('36')
                    pila2.append(aux)
                    
                elif(validar == "24"):
                    objR24 = reglasGramaticaCompleta.R24()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][36])

                    pila.append('36')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('36')
                    pila2.append(aux)

                elif(validar == "25"):
                    objR25 = reglasGramaticaCompleta.R25()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][36])

                    pila.append('36')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('36')
                    pila2.append(aux)
                    
                elif(validar == "26"):
                    objR26 = reglasGramaticaCompleta.R26()
                    #Aqui no se hace ningun pop por el unico token que hay es "vacío"
                    #Pila de enteros
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][37])

                    pila.append('37')
                    pila.append(aux)

                    #Pila de strings
                    pila2.append('37')
                    pila2.append(aux)

                elif(validar == "27"):
                    objR27 = reglasGramaticaCompleta.R27()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][37])

                    pila.append('37')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('37')
                    pila2.append(aux)

                elif(validar == "28"):
                    objR28 = reglasGramaticaCompleta.R28()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][38])

                    pila.append('38')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('38')
                    pila2.append(aux)

                elif(validar == "29"):
                    objR29 = reglasGramaticaCompleta.R29()
                    #Aqui no se hace ningun pop por el unico token que hay es "vacío"
                    #Pila de enteros
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][39])

                    pila.append('39')
                    pila.append(aux)

                    #Pila de strings
                    pila2.append('39')
                    pila2.append(aux)

                elif(validar == "30"):
                    objR30 = reglasGramaticaCompleta.R30()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()

                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][39])

                    pila.append('39')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()

                    pila2.append('39')
                    pila2.append(aux)

                elif(validar == "31"):
                    objR31 = reglasGramaticaCompleta.R31()
                    #Aqui no se hace ningun pop por el unico token que hay es "vacío"
                    #Pila de enteros
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][40])

                    pila.append('40')
                    pila.append(aux)

                    #Pila de strings
                    pila2.append('40')
                    pila2.append(aux)

                elif(validar == "32"):
                    objR32 = reglasGramaticaCompleta.R32()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][40])

                    pila.append('40')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('40')
                    pila2.append(aux)

                elif(validar == "33"):
                    objR33 = reglasGramaticaCompleta.R33()
                    #Aqui no se hace ningun pop por el unico token que hay es "vacío"
                    #Pila de enteros
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][41])

                    pila.append('41')
                    pila.append(aux)

                    #Pila de strings
                    pila2.append('41')
                    pila2.append(aux)

                elif(validar == "34"):
                    objR34 = reglasGramaticaCompleta.R34()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][41])

                    pila.append('41')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('41')
                    pila2.append(aux)

                elif(validar == "35"):
                    objR35 = reglasGramaticaCompleta.R35()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][42])

                    pila.append('42')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()

                    pila2.append('42')
                    pila2.append(aux)

                elif(validar == "36"):
                    objR36 = reglasGramaticaCompleta.R36()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][42])

                    pila.append('42')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()

                    pila2.append('42')
                    pila2.append(aux)

                elif(validar == "37"):
                    objR37 = reglasGramaticaCompleta.R37()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][42])

                    pila.append('42')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()

                    pila2.append('42')
                    pila2.append(aux)

                elif(validar == "38"):
                    objR38 = reglasGramaticaCompleta.R38()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][42])

                    pila.append('42')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()

                    pila2.append('42')
                    pila2.append(aux)

                elif(validar == "39"):
                    objR39 = reglasGramaticaCompleta.R39()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][42])

                    pila.append('42')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()

                    pila2.append('42')
                    pila2.append(aux)

                elif(validar == "40"):
                    objR40 = reglasGramaticaCompleta.R40()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][43])

                    pila.append('43')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('43')
                    pila2.append(aux)
                    
                elif(validar == "41"):
                    objR41 = reglasGramaticaCompleta.R41()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][44])

                    pila.append('44')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()

                    pila2.append('44')
                    pila2.append(aux)

                elif(validar == "42"):
                    objR42 = reglasGramaticaCompleta.R42()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][44])

                    pila.append('44')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()

                    pila2.append('44')
                    pila2.append(aux)

                elif(validar == "43"):
                    objR43 = reglasGramaticaCompleta.R43()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][45])

                    pila.append('45')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('45')
                    pila2.append(aux)

                elif(validar == "44"):
                    objR44 = reglasGramaticaCompleta.R44()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][45])

                    pila.append('45')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('45')
                    pila2.append(aux)
                
                elif(validar == "45"):
                    objR45 = reglasGramaticaCompleta.R45()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][45])

                    pila.append('45')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('45')
                    pila2.append(aux)
                    
                elif(validar == "46"):
                    objR46 = reglasGramaticaCompleta.R46()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][45])

                    pila.append('45')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('45')
                    pila2.append(aux)

                elif(validar == "47"):
                    objR47 = reglasGramaticaCompleta.R47()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][45])

                    pila.append('45')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('45')
                    pila2.append(aux)

                elif(validar == "48"):
                    objR48 = reglasGramaticaCompleta.R48()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][45])

                    pila.append('45')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('45')
                    pila2.append(aux)

                elif(validar == "49"):
                    objR49 = reglasGramaticaCompleta.R49()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][45])

                    pila.append('45')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('45')
                    pila2.append(aux)

                elif(validar == "50"):
                    objR50 = reglasGramaticaCompleta.R50()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][45])

                    pila.append('45')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('45')
                    pila2.append(aux)

                elif(validar == "51"):
                    objR51 = reglasGramaticaCompleta.R51()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][45])

                    pila.append('45')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()
                    pila2.pop()

                    pila2.append('45')
                    pila2.append(aux)

                elif(validar == "52"):
                    objR52 = reglasGramaticaCompleta.R52()
                    #Pila de enteros 
                    pila.pop()
                    pila.pop()
                    
                    pos = int(pila[len(pila)-1])
                    aux = int(matrizLR[pos][45])

                    pila.append('45')
                    pila.append(aux)

                    #Pila de strings
                    pila2.pop()
                    pila2.pop()
                    
                    pila2.append('45')
                    pila2.append(aux)

                    
        self.ui.tableWidget.clearContents()

        row = 0
        self.ui.tableWidget.setRowCount(len(elementos))

        for elemento in elementos:
            if elemento['lexema']=="if":
                elemento['token']="if"
                elemento['num'] = 19
            elif elemento['lexema']=="else":
                elemento['token']="else"
                elemento['num'] = 22
            elif elemento['lexema']=="while":
                elemento['token']="while"
                elemento['num']=20
            elif elemento['lexema']=="return":
                elemento['token']="return"
                elemento['num']=21
            elif elemento['lexema']=="int":
                elemento['token']="tipo de dato"
                elemento['num']=4
            elif elemento['lexema']=="float":
                elemento['token']="tipo de dato"
                elemento['num']=4
            elif elemento['lexema']=="void":
                elemento['token']="tipo de dato"
                elemento['num']=4
            
            self.ui.tableWidget.setItem(row,0,QTableWidgetItem(elemento['token']))
            self.ui.tableWidget.setItem(row,1,QTableWidgetItem(str(elemento['num'])))
            self.ui.tableWidget.setItem(row,2,QTableWidgetItem(elemento['lexema']))
            row +=1  