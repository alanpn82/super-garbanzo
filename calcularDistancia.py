
import math

from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class CalculandoDistancia():

    def __init__(self, posicao_cliente, lojas, plano):
        self.posicao_cliente = posicao_cliente
        self.lojas = lojas
        self.plano = plano

    def calcular_distancia(self,a_vect, b_vect):
        return math.sqrt((b_vect[0] - a_vect[0]) ** 2 + (b_vect[1] - a_vect[1]) ** 2)

    def calcular(self):
        for i in range(len(self.lojas)):
            self.lojas[i].insert(2, self.calcular_distancia(self.posicao_cliente, self.lojas[i]))

    def ordenando_pela_distancia(self,elemnto):
        return elemnto[2]

    def ordenar_pela_distancia(self):
        self.lojas.sort(key=self.ordenando_pela_distancia)

    def remover_distancia(self):
        for i in range(len(self.lojas)):
            self.lojas[i].pop(2)

    def top_3_lojas_proximas(self):
        self.calcular()
        print("distancia calculada")
        self.ordenar_pela_distancia()
        print("vetor ordenado pela distancia ")
        self.remover_distancia()

        return self.lojas[0:3]


def eh_valido_para_plano(numero):
    if 0 <= numero and 1000 >= numero:
        return True
    else:
        return False

def eh_valido_no_plano(coord, plano):
    if ( coord[0] >= 0 and coord[0] <= plano[0] ) and (coord[1] >= 0 and coord[1] <= plano[1] ):
        return True
    else:
        return False

def requerer_um_numero_stdin():
    i=0
    while i < 4:
        try:
            ret = input(" Entre com um número inteiro: ")
            return int(ret)
        except:
            print("Ooops {} não é um número válido!".format(ret))
            i = i + 1
            print("o número máximo de tentativas é 4 \n Voce ja tentou {} vezes".format(i))
            if i >= 4:
                print("O programa será encerrado!")
                exit()
            print("Vamos tentar novamente ")
            continue


def requerer_uma_coordenada():
    x = requerer_um_numero_stdin()
    y = requerer_um_numero_stdin()
    coordenada = [x,y]
    return coordenada

def coordenada_errada():
    raise ValueError('oops!')

def montar_um_plano():
    i=0
    while i < 4:
        try:
            plano = requerer_uma_coordenada()

            if not eh_valido_para_plano(plano[0]) or not eh_valido_para_plano(plano[1]):
                coordenada_errada()
            return plano
        except:
            print(" x = {} e y = {} não são valores válidos para um plano!".format(plano[0],plano[1]) )
            i = i + 1
            print("o número máximo de tentativas é 4 \n Voce ja tentou {} vezes".format(i))
            if i >= 4:
                print("O programa será encerrado!")
                exit()
            print("Vamos tentar novamente montar um plano")
            continue


def requerer_a_posicao_do_cliente(plano):
    i = 0
    while i < 4:
        try:
            posicao_cliente = requerer_uma_coordenada()

            if not eh_valido_no_plano(posicao_cliente,plano) :
                coordenada_errada()
            return posicao_cliente
        except:
            print(" x = {} e y = {} não são valores válidos para para a posicao do cliente no plano {}!".format(posicao_cliente[0], posicao_cliente[1], plano))
            i = i + 1
            print("o número máximo de tentativas é 4 \n Voce ja tentou {} vezes".format(i))
            if i >= 4:
                print("O programa será encerrado!")
                exit()
            print("Vamos tentar novamente montar a posicao do cliente ")
            continue



def carregar_uma_lista_de_lojas_validas_em_um_plano(plano):
    i=0 #quantidade de erros
    j=0 #quantidade de lojas
    lojas = []

    while i < 4 :
        print("por favor entre com a quantidade de lojas ")
        qtd_lojas = requerer_um_numero_stdin()
        if qtd_lojas > 0 and qtd_lojas <= plano[1]:
            break
        else:
            print(" qtd_lojas = {}  não é um valor válido! \n ou ele é menor do que 0 ou maior que {} ".format(qtd_lojas , plano[1]))
            i = i + 1
            print("o número máximo de tentativas é 4 \n Voce ja tentou {} vezes".format(i))
            if i >= 4:
                print("O programa será encerrado!")
                exit()
            print("Vamos tentar novamente entrar com a quantidad de lojas")
            continue
    i=0

    while j < qtd_lojas:
        try:
            print("Entre com as coordenadas de uma loja válida no plano {}".format(plano))
            loja = requerer_uma_coordenada()
            if eh_valido_no_plano(loja,plano):
                lojas.append(loja)
            else:
                coordenada_errada()
            j = j + 1
            print("loja {} adicionada a lista de lojas de um total de {} lojas ".format(j,qtd_lojas) )
        except:
            print(" x = {} e y = {} não são valores válidos para uma loja!".format(loja[0],loja[1]) )
            i = i + 1
            print("o número máximo de tentativas é 4 \n Voce ja tentou {} vezes".format(i))
            if i >= 4:
                print("O programa será encerrado!")
                exit()
            print("Vamos tentar novamente montar uma loja")
            continue
    return lojas

clear()


print("Olá por favor informe um plano para validação dos valores \n")
print ("Um plano deve conter dois números com um valor entre 0 e 1000")
print ("Você terá que entrar com dois números")




plano = montar_um_plano()


#print (plano)
clear()
print("Agora favor indicar a posicao do cliente com valores dentro do plano")

posicao_cliente = requerer_a_posicao_do_cliente(plano)

clear()

lojas = carregar_uma_lista_de_lojas_validas_em_um_plano(plano)

clear()

obj_calcular_distancia = CalculandoDistancia(posicao_cliente, lojas, plano)

print("resultado 3 primeiras lojas")
print(obj_calcular_distancia.top_3_lojas_proximas())







