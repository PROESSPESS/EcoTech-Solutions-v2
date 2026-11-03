class Personaje:
    def __init__(xd,vida,escudo,ataque,nivel):
        xd.vida = vida
        xd.escudo = escudo
        xd.ataque = ataque
        xd.nivel = nivel


jhon = Personaje(100,100,"xd",20)
print(jhon.ataque)