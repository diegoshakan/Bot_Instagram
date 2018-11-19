from robotdot import Robotdot

user = input('Username: ')
password = input('Password: ')
# user = 'geektest'
#password = 'testando123'

while True:
    x = int(
        input('[1] Perfil ou tag\n[2] Curtir fotos de pessoas sugeridas\nEscolha: '))
    if x == 1 or x == 2:
        if x == 1:
            while True:
                esc = int(input('[1]Perfil ou [2]tag: '))
                if esc == 1 or esc == 2:
                    break

            tag = input('Hastag ou perfil: ')
            tag = tag.lower()

            # put here your username a# put here your username and passgeektesword as arguments - coloque seu usuário e senha
            ig = Robotdot(user, password)
            ig.login()

            # here, you put the hashtag that you are looking for - Coloque aqui a hashtag que vc está procurando
            ig.page(tag, esc)
            break

        elif x == 2:
            ig = Robotdot(user, password)
            ig.login()
            ig.perfis()
            break
        break
