'''PyConcreto: Software para a tecnologia de concreto desenvolvido no LAMCO/UFF
Copyright (C) 2020  Eugênio Luiz (eugenioluiz@id.uff.br)
Esse programa é um software gratuito: você pode redistribuir e/ou modificá-lo
sob os termos da GNU General Public License conforme publicados pela Free
Software Foundation, na terceira versão da Licença. Este programa é
distribuído na esperança de que seja útil, porém SEM GARANTIAS; inclusive
sem a garantia implícita de COMERCIALIZAÇÃO ou ADEQUAÇÃO PARA
UM OBJETIVO ESPECÍFICO. Veja a GNU General Public License para mais detalhes.
Você deve ter recebido um cópia da GNU General Public License
junto deste programa. Do contrário, acesse <https://www.gnu.org/licenses/>'''

#Gerenciador de Janela
import sys
from PyQt5.QtWidgets import *
from MEC import *
from concretoPermeavel import *

class Janela(QMainWindow):
    def __init__(self):     
        super().__init__()
        self.setWindowTitle('PyConcreto')     
        self.resize(1368,720)
        self.menu=self.menuBar()
        
        #Menus
        self.file_menu=self.menu.addMenu('Arquivo')
        self.mec_menu=self.menu.addMenu('MEC')
        #self.dosa_menu=self.menu.addMenu('Dosagem')
        self.conperm_menu=self.menu.addMenu('Concreto Permeável')
        self.about_menu=self.menu.addMenu('Sobre')

        #Arquivo>Sair
        acao_fechar=QAction('Fechar',self)    
        acao_fechar.triggered.connect(self.sair_app)    
        self.file_menu.addAction(acao_fechar)

        #MEC>Misturas binárias
        bin_s=QAction('Misturas Binárias',self)           
        bin_s.triggered.connect(self.mist_bin)    
        self.mec_menu.addAction(bin_s)
        '''#MEC>Misturas ternárias
        tri_s=QAction('Misturas Ternárias',self)           
        tri_s.triggered.connect(self.mist_tri)    
        self.mec_menu.addAction(tri_s)
        #MEC>Misturas quaternárias
        qua_s=QAction('Misturas Quaternárias',self)           
        qua_s.triggered.connect(self.mist_qua)    
        self.mec_menu.addAction(qua_s)'''

        #Concreto Permeável>Traço otimizado
        perm_ot=QAction('Traço otimizado',self)           
        perm_ot.triggered.connect(self.tr_cp)    
        self.conperm_menu.addAction(perm_ot)
        #Concreto Permeável>Substituições
        perm_sub=QAction('Substituições',self)           
        perm_sub.triggered.connect(self.tr_sub)    
        self.conperm_menu.addAction(perm_sub)
        #Concreto Permeável>Substituições - Traço otimizado
        permot_sub=QAction('Substituições - Traço Otimizado',self)           
        permot_sub.triggered.connect(self.trot_sub)    
        self.conperm_menu.addAction(permot_sub)

        #Sobre>Informações
        sob_info=QAction('Informações',self)           
        sob_info.triggered.connect(self.info)    
        self.about_menu.addAction(sob_info)
        #Sobre>Versão
        ver_sion=QAction('Versão',self)           
        ver_sion.triggered.connect(self.versao)    
        self.about_menu.addAction(ver_sion)

    #Eventos
    def sair_app(self):    
        QApplication.quit()     
        self.close()

    def mist_bin(self):
        aplicacao_binaria=SisBin()
        self.setCentralWidget(aplicacao_binaria)

    def mist_tri(self):
        return
    def mist_qua(self):
        return 
    
    def tr_cp(self):
        aplicacao_permot=TrOt()
        self.setCentralWidget(aplicacao_permot)

    def tr_sub(self):
        aviso_r=QMessageBox()
        aviso_r.setWindowTitle("Aviso")
        aviso_r.setText('Gera substituições a partir de um traço não otimizado\nAs substituições aqui calculadas não necessariamente cumprem requisitos\nnormativos, sendo necessárias validações experimentais')
        aviso_r.exec()
        
        aplicacao_permsub=Subs()
        self.setCentralWidget(aplicacao_permsub)

    def trot_sub(self):
        aviso_r=QMessageBox()
        aviso_r.setWindowTitle("Aviso")
        aviso_r.setText('Gera substituições em massa do cimento a partir de um traço otimizado\nAs substituições aqui calculadas não necessariamente cumprem requisitos\nnormativos, sendo necessárias validações experimentais')
        aviso_r.exec()
        
        aplicacao_permotsub=SubsOt()
        self.setCentralWidget(aplicacao_permotsub)

    def info(self):
        info_r=QMessageBox()
        info_r.setIcon(QMessageBox.Information)
        info_r.setWindowTitle("Informações")
        info_r.setText('''PyConcreto: Software para a tecnologia de concreto desenvolvido no LAMCO/UFF
    Copyright (C) 2020  Eugênio Luiz (eugenioluiz@id.uff.br)''')
        informativo = '''Esse programa é um software gratuito: você pode redistribuir e/ou modificá-lo
    sob os termos da GNU General Public License conforme publicados pela Free
    Software Foundation, na terceira versão da Licença. Este programa é
    distribuído na esperança de que seja útil, porém SEM GARANTIAS; inclusive
    sem a garantia implícita de COMERCIALIZAÇÃO ou ADEQUAÇÃO PARA
    UM OBJETIVO ESPECÍFICO. Veja a GNU General Public License para
    mais detalhes.
    Você deve ter recebido um cópia da GNU General Public License
    junto deste programa. Do contrário, acesse <https://www.gnu.org/licenses/>'''
        info_r.setInformativeText(informativo)
        info_r.setStandardButtons(QMessageBox.Ok)
        info_r.exec()
        
    def versao(self):
        ver_atual=QMessageBox()
        #ver_atual.setIcon(QMessageBox.Information)
        ver_atual.setWindowTitle("Versão do Software")
        ver_atual.setText('PyConcreto v.0.9')
        ver_atual.setInformativeText('''Mais informações em: <http://matconst.sites.uff.br/>''')
        ver_atual.setStandardButtons(QMessageBox.Ok)
        ver_atual.exec()
