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

from sys import *
from janela import *

app=QApplication(sys.argv)        
janela=Janela()
janela.show()
sys.exit(app.exec_())
    
