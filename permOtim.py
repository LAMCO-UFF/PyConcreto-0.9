#Calculadora para otimização de concreto permeável
import numpy as np

class PermOt():
    def __init__(self):
        return

    def calc_vol(self, _materiais, _ro):
        vol_ume=0
        for i in range(4):
            v=_materiais[i]/_ro[i]
            vol_ume=vol_ume+v
        return vol_ume
