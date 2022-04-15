# -*- coding utf-8 -*-

first = input()
second = input()
third = input()

inseto = {
    "hematofago": "pulga",
    "herbivoro": "lagarta"
}

anelideo = {
    "hematofago": "sanguessuga",
    "onivoro": "minhoca"
}

ave = {
    "carnivoro": "aguia",
    "onivoro": "pomba"
}

mamifero = {
    "onivoro": "homem",
    "herbivoro": "vaca"
}

invertebrado = {
    "inseto": inseto,
    "anelideo": anelideo
}

vertebrado = {
    "ave": ave,
    "mamifero": mamifero
}

animais = {
    "vertebrado": vertebrado,
    "invertebrado": invertebrado
}

print(animais.get(first).get(second).get(third))