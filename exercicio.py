# Exercício de fixação 1
# Além do liquidificador, podemos modelar inúmeros eletrodomésticos, tais como: ventilador, batedeira, secador, máquina de lavar e etc.


# Em seguida faça com que a pessoa tenha um ventilador como atributo através da composição.

# Crie também um método comprar_ventilador.

# Faça com que o print (__str__) de Pessoa informe se sua instância possui ou não um ventilador.

# Para fixar crie uma objeto da classe Ventilador, semelhante ao exemplo do liquidificador.

# Crie um construtor

class Ventilador:
    def __init__(self, cor, potencia, tensao, 
    preco):
        self.preco = preco
        self.cor = cor
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0
