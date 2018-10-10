from selenium import webdriver
from time import sleep


#You must download the chromedriver if you will use the navigator Chrome.
#driver = webdriver.Chrome('/home/shakan/Downloads/chromedriver') #This parameter is necessary, because I use the navigator Chrome.
driver = webdriver.Chrome(
    'C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe')
# this is url of Instagram
driver.get(
    'https://www.instagram.com/accounts/login/?hl=pt-br&source=auth_switcher')
#x= input()
'''Here you must insert your name user and your password'''
name = input('Enter with your username: ')
password = input('Enter with your password: ')

'''the input of name of user and password is same class of name. For this, I need make a 'for' trough function 'find_elements'.'''
acess = driver.find_elements_by_class_name('_2hvTZ')

# I found two class, so the first position in my array is the input user name.
user_name = acess[0]
user_name.send_keys(name)

# Logicaly, the second position is the input for password
password_name = acess[1]
password_name.send_keys(password)

login_acess = driver.find_element_by_class_name('Igw0E')
login_acess.submit()

# sleep here, because the bot need a time for the cause velocity of internet.
# sleep(2.0)
# notification = driver.find_element_by_class_name('aOOlW')
# notification.click()

# Test of like
sleep(2.0)

"""
like = driver.find_elements_by_class_name('coreSpriteHeartOpen')
print(len(like))
like[0].click()
like = driver.find_elements_by_class_name('coreSpriteHeartOpen')
print(len(like))
sleep(2.0)
like[1].click()

"""

# pega a quantidade de fotos q quer curtir
quant = int(input('Quantas fotos você quer curtir? '))

# Um contador começando do zero
# que vai até a quant. de fotos a serem curtidas
# e pelo x que será identificado as fotos na lista "like"
x = 0

while x < quant:
    # pegar as fotos
    like = driver.find_elements_by_class_name('coreSpriteHeartOpen')
    t = len(like)
    # for para percorrer a lista
    for i in range(t):
        # caso base para parar o programa
        if x == quant:
            break
        sleep(2.0)

        # curtindo as fotos
        like[x].click()

        # aumentando contador
        x += 1
