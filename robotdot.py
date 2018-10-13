from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from time import sleep


class Robotdot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('/home/shakan/Downloads/chromedriver')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/?hl=pt-br&source=auth_switcher')
        username_input = driver.find_element_by_xpath('//input[@name="username"]')
        username_input.send_keys(self.username)
        password_input = driver.find_element_by_xpath('//input[@name="password"]')
        password_input.send_keys(self.password)
        enter_submit = driver.find_element_by_class_name('Igw0E')
        enter_submit.submit()
        sleep(2)
        notification = driver.find_element_by_class_name('aOOlW')
        notification.click()
        sleep(2)

    def curtir(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        sleep(2)

        #um loop para baixar a página e atualizar as fotos - loop to looking for photos and update them
        for i in range(1, 2):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(2)


        #após atualizar as fotos na página, receber seus respectivos endereços
        links = driver.find_elements_by_tag_name('a')
        photos_links = [elem.get_attribute('href') for elem in links]
        photos_links = [href for href in photos_links if hashtag in href]
        print(hashtag + ' photos ' + str(len(photos_links)))


        for photo_link in photos_links:
            driver.get(photo_link)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('/html/body/span/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()
                like_button().click()

            except Exception as e:
                sleep(2)



ig = Robotdot() #put here your username and password as arguments - coloque seu usuário e senha
ig.login()
ig.curtir() #here, you put the hashtag that you are looking for - Coloque aqui a hashtag que vc está procurando

