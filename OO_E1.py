class Ponto2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def __str__(self):
        return "Valor de x: "+ str(self.x) + ", " + str(self.y)
     
    def eixo_x(self):
        return self.x

    def eixo_y(self):
        return self.y   
class Retangulo:

    
    def __init__(self, esq_sup, dir_inf):
        self.__esq_sup = esq_sup
        self.__dir_inf = dir_inf
        self.width = dir_inf.eixo_x() - esq_sup.eixo_x()
        self.height = esq_sup.eixo_y() - dir_inf.eixo_y()
    
    def esq_sup(self):
        return self.__esq_sup

    def dir_inf(self):
        return self.__dir_inf
    
    def __str__(self):
        es = self.__esq_sup()
        return es

    def calcularArea(self):
        larg = self.width
        alt = self.height
        return (larg*alt)

    def calcularIntersecao(self, ret):
        inter_x = min(self.dir_inf().eixo_x(), ret.dir_inf().eixo_x()) - max(self.esq_sup().eixo_x(), ret.esq_sup().eixo_x())
        inter_y = min(self.esq_sup().eixo_y(), ret.esq_sup().eixo_y()) - max(self.dir_inf().eixo_y(), ret.dir_inf().eixo_y())
        if(inter_x>=0) and (inter_y>=0):
            return inter_y*inter_x
            
r1_esq_sup = Ponto2D(-6.5, 5.0)
r1_dir_inf = Ponto2D(-2.0, 2.5)
ret1 = Retangulo(r1_esq_sup, r1_dir_inf)
area1 = ret1.calcularArea() 
print("%.2f %.2f %.2f" % (ret1.width, ret1.height, area1))
 
r2_esq_sup = Ponto2D(2.0, 7.0)
r2_dir_inf = Ponto2D(5.0, 4.0)
ret2 = Retangulo(r2_esq_sup, r2_dir_inf)
area2 = ret2.calcularArea()
print("%.2f %.2f %.2f" % (ret2.width, ret2.height, area2))
intersecao = ret1.calcularIntersecao(ret2)
print(intersecao)