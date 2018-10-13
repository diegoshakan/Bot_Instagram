from imports import *

class Robotdot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        #self.driver = webdriver.Chrome('/home/shakan/Downloads/chromedriver')
        self.driver = webdriver.Chrome('chromedriver.exe')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/?hl=pt-br&source=auth_switcher')
        username_input = driver.find_element_by_xpath('//input[@name="username"]')
        username_input.send_keys(self.username)
        password_input = driver.find_element_by_xpath('//input[@name="password"]')
        password_input.send_keys(self.password)
        sleep(2)
        enter_submit = driver.find_element_by_class_name('Igw0E')
        enter_submit.submit()
        sleep(2)

    def curtir(self, hashtag, esc):
        driver = self.driver
        if esc == 2:
            driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/') # para hashtag
        if esc == 1:
            driver.get('https://www.instagram.com/'+hashtag+'/') # para perfis
        sleep(2)

        #um loop para baixar a página e atualizar as fotos - loop to looking for photos and update them
        for i in range(1, 3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(1)


        #após atualizar as fotos na página, receber seus respectivos endereços
        links = driver.find_elements_by_tag_name('a')
        photos_links = [elem.get_attribute('href') for elem in links]
        photos_links = [href for href in photos_links if hashtag in href]
        print(hashtag + ' photos ' + str(len(photos_links)))

                    
        for photo_link in photos_links:
            driver.get(photo_link)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            try:
                sleep(random.randint(3, 7))
                comment_button = lambda: driver.find_element_by_link_text('Comentar')
                comment_button().click()
            except NoSuchElementException:
                pass


            # == Comments
            try:
                sleep(random.randint(3, 7))
                comment_write = lambda: driver.find_element_by_xpath('//textarea[@aria-label="Adicione um comentário..."]')
                comment_write().clear()
                sleep(random.randint(3, 10))
                comment_write().send_keys(random.choice(comments))
                comment_write().send_keys(Keys.ENTER)

            except StaleElementReferenceException and NoSuchElementException as e:
                print(e)
                sleep(2)


            # == Likes
            try:
                sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('/html/body/span/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()
                like_button().click()

            except Exception as e:
                sleep(2)



user = input('Username: ')
password = input('Password: ')

while True:
    esc = int(input('[1]Perfil ou [2]tag: '))
    if esc ==1 or esc==2:
        break

tag = input('Hastag ou perfil: ')
ig = Robotdot(user, password) #put here your username and password as arguments - coloque seu usuário e senha
ig.login()
ig.curtir(tag,esc) # here, you put the hashtag that you are looking for - Coloque aqui a hashtag que vc está procurando
