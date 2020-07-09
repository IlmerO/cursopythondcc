class Item:
    def __init__(self, nome, valor):
        global identificadorGlobal
        identificadorGlobal = 0
        self.quantidade=0
        self.nome = nome
        self.valor = valor
        self.id =  identificadorGlobal
        identificadorGlobal =  identificadorGlobal + 1
    

class Livro(Item):
    def __init__(self, nome, valor):
        super().__init__(nome, valor)
        self.tipo = "Livro"
        self.desconto = 0.03
        self.valorSemDesc = 0
        self.valorComDesc = 0
    
    def __str__(self):        
        return(str(self.tipo) + ", " + str(self.nome) + ", " + str(self.quantidade) + ", " + str("%.2f" % (self.valor)) + ", " + str("%.2f" % (self.valorSemDesc)) + ", " + str("%.2f" % (self.valorComDesc)))

class Brinquedo(Item):
    def __init__(self, nome, valor):
        super().__init__(nome, valor)
        self.tipo = "Brinquedo"
        self.desconto = 0.05
        self.valorSemDesc = 0
        self.valorComDesc = 0
    def __str__(self):        
        return(str(self.tipo) + ", " + str(self.nome) + ", " + str(self.quantidade) + ", " + str("%.2f" % (self.valor)) + ", " + str("%.2f" % (self.valorSemDesc)) + ", " + str("%.2f" % (self.valorComDesc)))

class Eletronico(Item):
    def __init__(self, nome, valor):
        super().__init__(nome, valor)
        self.tipo = "Eletronico"
        self.desconto = 0.08    
        self.valorSemDesc = 0
        self.valorComDesc = 0
    def __str__(self):        
        return(str(self.tipo) + ", " + str(self.nome) + ", " + str(self.quantidade) + ", " + str("%.2f" % (self.valor)) + ", " + str("%.2f" % (self.valorSemDesc)) + ", " + str("%.2f" % (self.valorComDesc)))
idDicionario = 0
class CestaCompras:
   
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, item, qtde):
        item.quantidade = qtde
        item.valorSemDesc = item.valor * qtde
        item.valorComDesc = item.valor * qtde * (1-item.desconto)
      #  print("Quantidade registrada: " + str(item.quantidade))
        global idDicionario
        idNovo = idDicionario
        self.id = idNovo
        self.itens.update({item:qtde})
        idDicionario = idNovo + 1

    def relatorio_final(self):
        #print somatório de todos os itens ja com desconto aplicado
        #print tipo item, nome, quantidade, valor_unitaario, total_sem_desconto, total_com_desconto
        self.valorTotal = 0
        for key in self.itens.keys():
            self.valorTotal = self.valorTotal + key.valorComDesc
        print("%.2f" % (self.valorTotal))
        for key in self.itens.keys():
            print(key)


livro1 = Livro("Senhor dos Aneis", 15.00)
brinq1 = Brinquedo("Carrinho", 12.99)

cesta = CestaCompras()
cesta.adicionar_item(livro1, 3)
cesta.adicionar_item(brinq1, 4)

#for item, qtde in cesta.itens.items():
 #       print("%s, %i" % (item.nome, qtde))

cesta.relatorio_final()
