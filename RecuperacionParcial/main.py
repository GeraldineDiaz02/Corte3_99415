from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("menuresistencias.ui", self)
        self.show()

        self.resisserie.clicked.connect(self.irresisserie)
        self.resisparale.clicked.connect(self.irresisparalelo)
        self.resisparayserie.clicked.connect(self.irresisserieyparalelo)

    def irresisserie(self):
        self.hide()  
        self.resiss = Resistenciasserie()
        self.resiss.show()

    def irresisparalelo(self):
        self.hide()  
        self.resisp = Resistenciasparalelo()
        self.resisp.show()

    def irresisserieyparalelo(self):
        self.hide()  
        self.resissp = Resistenciasserieyparalelo()
        self.resissp.show()

class Resistenciasserie(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("resistenciasenserie.ui", self)
        self.show()

        self.volverrs.clicked.connect(self.serieirprincipal)
        self.calcular1.clicked.connect(self.calcularserie)

    def calcularserie(self):
        resis1s = float(self.r1ps.text())
        resis2s = float(self.r2ps.text())
        resis3s = float(self.r3ps.text())

        self.respuesta1.setText(str(round(resis1s + resis2s + resis3s,2)))

    def serieirprincipal(self):
        self.hide()  
        self.sprincial = Principal()
        self.sprincial.show()

class Resistenciasparalelo(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("resistenciasenparalelo.ui", self)
        self.show()
         
        self.volverrp.clicked.connect(self.paraleloirprincipal)
        self.calcular2.clicked.connect(self.calcularparalelo)

    def calcularparalelo(self):
        resis1p = float(self.r1pp.text())
        resis2p = float(self.r2pp.text())
        resis3p = float(self.r3pp.text())
        resis4p = float(self.r4pp.text())
        p1=((1/resis1p))
        p2=((1/resis2p))
        p3=((1/resis3p))
        p4=((1/resis4p))
        p5=(p1+p2+p3+p4)
        p6=(1/p5)
        self.respuesta2.setText(str(round(p6,2)))

    def paraleloirprincipal(self):
        self.hide()  
        self.pprincial = Principal()
        self.pprincial.show()

class Resistenciasserieyparalelo(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("resistenciasenparaleloyserie.ui", self)
        self.show()

        self.volverrsyp.clicked.connect(self.pysirprincipal)
        self.calular3.clicked.connect(self.calcularserieyparalelo)

    def calcularserieyparalelo(self):
        resis1pys = float(self.r1pys.text())
        resis2pys = float(self.r2pys.text())
        resis3pys = float(self.r3pys.text())
        resis4pys = float(self.r4pys.text())
        resis5pys = float(self.r5pys.text())

        paso_1 = (resis5pys*resis4pys)/(resis5pys+resis4pys)
        paso_2 = (resis2pys+paso_1)
        paso_3 = (1 / ((1/resis1pys)+(1/paso_2)+(1/resis3pys)))


        self.respuesta3.setText(str(round(paso_3,2)))

    def pysirprincipal(self):
        self.hide()  
        self.pysprincial = Principal()
        self.pysprincial.show()


def main():
    app = QApplication(sys.argv)
    window = Principal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()