#Gerador de funções gama
import numpy as np

class Gama():
    def __init__(self):
        return

    def composicao(self, _n):
        self.n=_n
        y=np.ones(self.n)
        g_ama=np.ones(self.n)

        for i in range(1, self.n+1):
            termo1=0
            termo2=0
            for j in range(1, i):
                if (i-1)>0:
                    termo1=termo1+(1-beta[i]+M[i,j]+beta[i]*(1-1/beta[j]))*y[j]
            for j in range(i+1, self.n+1):
                if (i+1)<=self.n:
                    termo2=termo2+(1-M[i,j]*beta[i]/beta[j])*y[j]
            g_ama[i]=beta[i]/(1-termo1-termo2)


