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

#Introdução dos Materiais
import numpy as np

class Material():
    def __init__(self):
        self.p= 0.0
        self.beta= 0.0
        self.d= 0.0
        self.nome= ''

    def matriz_material(self):
        self.matriz=np.array([self.p, self.beta, self.d])

class ConcPermOt():
    def __init__(self):
        self.m_c0 =539.92
        self.m_w0 =189.02
        self.m_b0 =1593.86
        self.m_a0 =28.42
        self.m_0 = np.array([self.m_c0, self.m_w0, self.m_b0, self.m_a0])

    def mass_esp(self, _pc, _pw, _pb, _pa):
        self.vet_ro= np.array([_pc, _pw, _pb, _pa])
        
class ConcPermSub():
    def __init__(self):
        self.m_c0 =563.43
        self.m_w0 =197.25
        self.m_b0 =1580.12
        self.m_m0 =0.0
        self.m_0 = np.array([self.m_c0, self.m_w0, self.m_b0, self.m_m0])

    def mass_esp(self, _pc, _pw, _pb, _pm):
        self.vet_ro= np.array([_pc, _pw, _pb, _pm])

    def teor_sub(self, _sub, _nome):
        self.sub= _sub
        self.material= _nome

class ConcPermSubOt():
    def __init__(self):
        self.m_c0 =539.92
        self.m_w0 =189.02
        self.m_b0 =1593.86
        self.m_a0 =28.42
        self.m_m0 =0.0
        self.m_0 = np.array([self.m_c0, self.m_w0, self.m_b0, self.m_a0, self.m_m0])

    def mass_esp(self, _pc, _pw, _pb, _pa, _pm):
        self.vet_ro= np.array([_pc, _pw, _pb, _pa, _pm])

    def teor_sub(self, _sub, _nome):
        self.sub= _sub
        self.material= _nome

#Modelo antigo
'''class Material2():
    def __init__(self):
        self.p2= float(input('Massa específica do material 2: '))
        self.beta2= float(input('Compacidade do material 2: '))
        self.d2= float(input('Diâmetro do material 2: '))
        self.nome2=input('Nome do material 2: ')
        self.matriz=np.array([self.p2, self.beta2, self.d2, self.nome2])'''

