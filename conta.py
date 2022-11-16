class Conta:
    def __init__(self, numero, titular, saldo, limite):   # usa __ __ pq é uma função automática
        print("Construinddo objeto...{}".format(self))
        # self é a referência que sabe mencontrar o objeto construído em memória
        # com o self dá para acessar o objeto e definir seus atributos e características
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        # o caractere "ponto" (.) é um comando de ida ao objeto e numero, titular, saldo e limite são atributos.
