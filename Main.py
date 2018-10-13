from imports import *
from robotdot import Robotdot

user = input('Username: ')
password = input('Password: ')

while True:
    esc = int(input('[1]Perfil ou [2]tag: '))
    if esc == 1 or esc == 2:
        break

tag = input('Hastag ou perfil: ')
tag = tag.lower()

# put here your username and password as arguments - coloque seu usuário e senha
ig = Robotdot(user, password)
ig.login()
# here, you put the hashtag that you are looking for - Coloque aqui a hashtag que vc está procurando
ig.page(tag , esc)
