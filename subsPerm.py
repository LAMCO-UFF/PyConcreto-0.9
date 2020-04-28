#Calculadora para substituições de material em concreto permeável
import numpy as np

class PermSub():
    def __init__(self):
        return

    def substituicao(self, substituido, tal):
        return tal*substituido/100

    def calc_quant1(self, _matriz, _substituto, _ro):
        materiais_0= [_matriz[0]-_substituto, 0.35*(_matriz[0]-_substituto), _matriz[2], _substituto]
        fator=self.calc_vol(materiais_0, _ro)
        materiais_f = [0, 0, 0, 0]
        for i in range(4):
            materiais_f[i]= materiais_0[i]/fator
        return materiais_f

    def calc_quant2(self, _matriz, _substituto, _ro):
        materiais_0= [_matriz[0], _matriz[1], _matriz[2]-_substituto, _substituto]
        fator=self.calc_vol(materiais_0, _ro)
        materiais_f = [0, 0, 0, 0]
        for i in range(4):
            materiais_f[i]= materiais_0[i]/fator
        return materiais_f

    def calc_vol(self, _materiais, _ro):
        vol_ume=0
        for i in range(4):
            v=_materiais[i]/_ro[i]
            vol_ume=vol_ume+v
        return vol_ume
