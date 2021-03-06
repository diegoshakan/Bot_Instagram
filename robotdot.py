from imports import *


class Robotdot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(
            '/home/shakan/Documentos/Bot_Instagram/chromedriver')
        #self.driver = webdriver.Chrome('chromedriver.exe')

    def baixa_page(self, vezes):
        #um loop para baixar a página e atualizar as fotos - loop to looking for photos and update them
        for i in range(vezes):
            self.driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')
            sleep(3)

    def login(self):
        driver = self.driver
        sleep(1)
        driver.get(
            'https://www.instagram.com/accounts/login/?hl=pt-br&source=auth_switcher')
        sleep(2)
        username_input = driver.find_element_by_xpath(
            '//input[@name="username"]')
        username_input.send_keys(self.username)
        password_input = driver.find_element_by_xpath(
            '//input[@name="password"]')
        password_input.send_keys(self.password)
        sleep(2)
        enter_submit = driver.find_element_by_class_name('Igw0E')
        enter_submit.submit()
        sleep(2)

    def comment(self):
        driver = self.driver
        """try:
            sleep(random.randint(3, 7))
            def comment_button(): return driver.find_element_by_link_text(
                'Comentar')
            comment_button().click()
        except NoSuchElementException:
            pass"""

        try:
            sleep(random.randint(2, 4))

            def comment_write(): return driver.find_element_by_xpath(
                '//textarea[@aria-label="Adicione um comentário..."]')
            comment_write().clear()
            sleep(random.randint(3, 7))
            text = random.choice(comments)
            for i in text:
                comment_write().send_keys(i)
                sleep(random.randint(3, 10)/30)
            comment_write().send_keys(Keys.ENTER)

        except StaleElementReferenceException and NoSuchElementException as e:
            print(e)
            sleep(2)

    def like(self):
        driver = self.driver
        # == Likes
        try:
            sleep(random.randint(2, 4))

            def like_button(): return driver.find_element_by_xpath(
                '/html/body/span/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()
            like_button().click()

        except Exception as e:
            sleep(2)

    def page(self, hashtag, esc):
        ''' Somente para determinados Perfis ou Hastag '''
        driver = self.driver
        if esc == 2:
            driver.get('https://www.instagram.com/explore/tags/' +
                       hashtag + '/')  # para hashtag
        if esc == 1:
            driver.get('https://www.instagram.com/'+hashtag+'/')  # para perfis
        sleep(2)

        self.baixa_page(5)

        #após atualizar as fotos na página, receber seus respectivos endereços
        links = driver.find_elements_by_tag_name('a')
        photos_links = [elem.get_attribute('href') for elem in links]
        photos_links = [href for href in photos_links if '/p/' in href]
        print(hashtag + ' photos ' + str(len(photos_links)))

        for photo_link in photos_links:
            driver.get(photo_link)
            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')

            sleep(1)
            self.comment()
            self.like()

    def perfis(self):
        ''' 
        Entra na página de sugestões de pessoas para seguir 
        e entra no perfil de algumas e curti 3 fotos de cada
        '''
        sleep(3)
        driver = self.driver
        driver.get('https://www.instagram.com/explore/people/suggested/')

        sleep(1)
        self.baixa_page(5)
        sleep(2)

        div = driver.find_elements_by_class_name('_7UhW9')
        a = driver.find_elements_by_tag_name('a')
        links = [elem.get_attribute('href') for elem in a]
        #people = [elem.get_attribute('href') for elem in links]
        print(links)

        for person in links:
            # Entrando em cada pessoa ...
            driver.get(person)

            sleep(5)

            self.baixa_page(2)

            links_photos = driver.find_elements_by_tag_name('a')
            photos = [elem.get_attribute('href') for elem in links_photos]
            photos = [href for href in photos if '/p/' in href]

            # Se a pessoa tem mais de 3 fotos, o robodot só curtirá somente 3
            if len(photos) >= 3:
                for photo in range(3):
                    driver.get(photos[photo])
                    self.like()
                    self.comment()
                    sleep(3)
            # Se a pessoa tem menos que 3 fotos, o robodot curtirá quantas fotos tiverem
            else:
                for photo in photos:
                    driver.get(photo)
                    self.like()
                    self.comment()
                    sleep(3)
