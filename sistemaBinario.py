#Calculadora para sistema binário
import numpy as np
import matplotlib.pyplot as plt

class Sistema():
    def __init__(self, M1, M2):
        self.prp=np.array([M1.matriz, M2.matriz])
        prp=self.prp
        self.M= np.ones((2,2))

        for i in range(2):
            for j in range(2):
                if i<j:
                    self.M[i,j]=(1-(1-prp[1,2]/prp[0,2])**1.02)**0.5
                if i==j:
                    self.M[i,j]=1
                if i>j:
                    self.M[i,j]=1-(1-prp[1,2]/prp[0,2])**(3/2)

    def Gama1(self, _prp, _M, _y1):
        gama_1= (_prp[0,1])/(1-(1-_M[0,1]*(_prp[0,1])/(_prp[1,1]))*(1-_y1))
        return gama_1

    def Gama2(self, _prp, _M, _y1):
        gama_2= (_prp[1,1])/(1-_y1*(1-_prp[1,1]+_M[1,0]*_prp[1,1]*(1-1/_prp[0,1])))
        return gama_2

    def equacao(self, _prp, _M, _y1):
        gama_1= self.Gama1(_prp, _M, _y1)
        gama_2= self.Gama2(_prp, _M, _y1)
        return gama_1-gama_2

    def resolver(self):
        f=1.0
        prp=self.prp
        M=self.M
        mistura_otima=0
        for y1 in np.arange(0.0001, 0.95, 0.0001):
            if f>abs(self.equacao(prp, M, y1)):
                f=abs(self.equacao(prp, M, y1))
                mistura_otima=y1
        return mistura_otima

    def max_compacidade(self):
        prp=self.prp
        M=self.M
        mistura_otima=self.resolver()
        gama=self.Gama1(prp, M, mistura_otima)
        return gama*100

    def plotar(self):
        limite=self.resolver()
        prp=self.prp
        M=self.M
        vet_comp=[]
        for y1 in np.arange(0.0, 1.0, 0.0001):
            if y1<=limite:
                comp=self.Gama2(prp, M, y1)
            else:
                comp=self.Gama1(prp, M, y1)
            vet_comp.append(comp)

        plt.plot(100*np.arange(0.0, 1.0, 0.0001), vet_comp)
        plt.title('Compacidade pela porção volumétrica')
        plt.xlabel('Porção volumétrica y1 (%)')
        plt.ylabel('Compacidade virtual')
        plt.show()
