import sys
import PyQt5.QtWidgets as PyQT
from PyQt5 import  uic
import login

class Principal(PyQT.QMainWindow):
    def __init__(self): 
        super().__init__()
        self.initGui()
    
    def initGui(self):
        uic.loadUi("PrimerEjercicio.ui",self)
        self.show()

        self.boton.clicked.connect(self.cambio)

    def calcular(self):
        texto1=float(self.num1.text())
        texto2=float(self.num2.text())
        if self.suma.isChecked()==True:
          self.resultado.setText(str(texto1+texto2))    
        elif self.resta.isChecked()==True:
            self.resultado.setText(str(texto1-texto2)) 
        elif self.multiplicacion.isChecked()==True:
            self.resultado.setText(str(texto1*texto2)) 
        else:
            self.resultado.setText(str(texto1/texto2)) 

    def cambio(self):
        login.Principal()

def main():
    app=PyQT.QApplication([])
    window= Principal()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
