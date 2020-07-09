class Conta:
    def __init__(self, num):
        self.__numero = num
        self.saldo = 0.0

 
    def depositar(self, valor):
        self.saldo = self.saldo+valor

    def sacar(self, valor):
        self.saldo = self.saldo-valor

    def get_saldo(self):
        valSaldo = self.saldo
        return valSaldo

  #  def get_saldo_p(self):
       # return self.__get_saldo()    

    def setnum(self, num):
        self.__numero = num       

class ContaCorrente(Conta):

    def __init__(self, num=1, taxa=0.5):
        super().__init__(num)
        self.taxa = taxa

    def cobrar_taxa(self):
        self.sacar(self.taxa)

class ContaPoupanca(Conta):

    def __init__(self, num=1, juro=0.5):
        super().__init__(num)
        self.setnum(num)
        self.juro = juro

    def aplicar_juros(self):
        self.depositar(self.juro*self.saldo)

