#Gerenciador de Janela
import sys
from PyQt5.QtWidgets import *
from materiais import *
from sistemaBinario import *

class SisBin(QWidget):
    def __init__(self):
        super().__init__()
        #Material 1
        self.nome1 = QLineEdit()        
        self.p1 = QLineEdit()
        self.beta1 = QLineEdit()        
        self.diametro1 = QLineEdit()
        #Material 2
        self.nome2 = QLineEdit()        
        self.p2 = QLineEdit()
        self.beta2 = QLineEdit()        
        self.diametro2 = QLineEdit()
        #Outras ações
        self.ger_graf = QPushButton("Gerar gráfico")       
        self.ger_graf.setEnabled(False)        #desabilita o botão adicionar a principio
        self.comp_max = QLineEdit()
        self.y1_max = QLineEdit()
        self.y2_max = QLineEdit()
        self.ind_compac = QLineEdit()
        self.compa_real = QPushButton("Calcular compacidade real")       
        self.compa_real.setEnabled(False)
        self.comp_real = QLineEdit()
        self.limpar = QPushButton("Limpar espaços")         
        self.sair = QPushButton("Sair")         #cria um botao para sair
        #Elementos gráficos
            #Esquerda
        self.left = QVBoxLayout()      #cria uma caixa vertical (na esquerda)
        self.left.addWidget(QLabel("Material 1"))
        self.left.addWidget(self.nome1)
        self.left.addWidget(QLabel("Massa específica (kg/m³)"))
        self.left.addWidget(self.p1)
        self.left.addWidget(QLabel("Compacidade"))
        self.left.addWidget(self.beta1)
        self.left.addWidget(QLabel("Diâmetro máximo (mm)"))
        self.left.addWidget(self.diametro1)
        self.left.addStretch()
            #Central
        self.central = QVBoxLayout() 
        self.central.addWidget(QLabel("Material 2"))
        self.central.addWidget(self.nome2)
        self.central.addWidget(QLabel("Massa específica (kg/m³)"))
        self.central.addWidget(self.p2)
        self.central.addWidget(QLabel("Compacidade"))
        self.central.addWidget(self.beta2)
        self.central.addWidget(QLabel("Diâmetro máximo (mm)"))
        self.central.addWidget(self.diametro2)
        self.central.addStretch()
            #Direita
        self.right=QVBoxLayout()
        self.right.addWidget(self.ger_graf)
        self.right.addWidget(QLabel("Compacidade máxima"))
        self.right.addWidget(self.comp_max)
        self.right.addWidget(QLabel("Percentual volumétrico do Material 1 (%)"))
        self.right.addWidget(self.y1_max)
        self.right.addWidget(QLabel("Percentual volumétrico do Material 2 (%)"))
        self.right.addWidget(self.y2_max)
        self.right.addWidget(QLabel("Índice de compactação"))
        self.right.addWidget(self.ind_compac)
        self.right.addWidget(self.compa_real)
        self.right.addWidget(QLabel("Compacidade real"))
        self.right.addWidget(self.comp_real)
        self.right.addWidget(self.limpar)
        self.right.addStretch()     #cria uma caixa de rabisco vazia entre elementos
        self.right.addWidget(self.sair)
            #Implementação
        self.layout = QHBoxLayout()         
        self.layout.addLayout(self.left)   #Um VBox é um layout
        self.layout.addLayout(self.central)
        self.layout.addLayout(self.right)
        self.setLayout(self.layout)         

        #Sinais     (Conectam um elemento grafico a um metodo)
        self.beta1.textChanged[str].connect(self.check_disable)
        self.diametro1.textChanged[str].connect(self.check_disable)
        self.beta2.textChanged[str].connect(self.check_disable)
        self.diametro2.textChanged[str].connect(self.check_disable)
        self.ger_graf.clicked.connect(self.calcular)
        
        self.comp_max.textChanged[str].connect(self.check_real)
        self.ind_compac.textChanged[str].connect(self.check_real)
        self.compa_real.clicked.connect(self.calcular_real)
        
        self.limpar.clicked.connect(self.limpar_itens)
        self.sair.clicked.connect(self.quit_application)

    #Eventos
    def check_disable(self, s):         #verifica se pode acionar o botão
        if not self.beta1.text() or not self.diametro1.text() or not self.beta2.text() or not self.diametro2.text():
            self.ger_graf.setEnabled(False)
        else:
            self.ger_graf.setEnabled(True)

    def check_real(self, s):         #verifica se pode acionar o botão
        if not self.comp_max.text() or not self.ind_compac.text():
            self.compa_real.setEnabled(False)
        else:
            self.compa_real.setEnabled(True)

    def calcular(self):
        self.M1=Material()
        self.M2=Material()

        self.M1.nome=self.nome1.text()
        self.pega_ro(self.M1.p, self.p1)
        self.M1.beta=float(self.beta1.text())
        self.M1.d=float(self.diametro1.text())
        self.M1.matriz_material()

        self.M2.nome=self.nome2.text()
        self.pega_ro(self.M2.p, self.p2)
        self.M2.beta=float(self.beta2.text())
        self.M2.d=float(self.diametro2.text())
        self.M2.matriz_material()

        if self.M1.matriz[2]<self.M2.matriz[2]:
            self.erro_diametro()

        ferramenta=Sistema(self.M1, self.M2)
        self.comp_max.setText('')
        self.comp_max.setText(str(round(ferramenta.max_compacidade(), 5)))
        y1=ferramenta.resolver()
        y2=1-y1
        self.y1_max.setText(str(round(100*y1, 3)))
        self.y2_max.setText(str(round(100*y2, 3)))
        ferramenta.plotar()

    def calcular_real(self):    #O ideal seria nao calcular aqui
        K=float(self.ind_compac.text())
        fator=(K+1)/K
        beta_max=float(self.comp_max.text())
        phi=round(beta_max/fator, 3)
        self.comp_real.setText('')
        self.comp_real.setText(str(phi))

    def pega_ro(self, _matriz, _valor):
        if _valor.text()!='':
            _matriz=float(_valor.text())
        else:
            _matriz=0

    def erro_diametro(self):
        info_d=QMessageBox()
        info_d.setWindowTitle("Erro!")
        info_d.setText('Diâmetro 1 necessita ser maior que Diâmetro 2!')
        info_d.exec()

    def limpar_itens(self):
        self.nome1.setText('')
        self.p1.setText('')
        self.beta1.setText('')
        self.diametro1.setText('')
        self.nome2.setText('')
        self.p2.setText('')
        self.beta2.setText('')
        self.diametro2.setText('')
        
    def quit_application(self):
        self.close()

