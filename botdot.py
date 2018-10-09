from selenium import webdriver


#You must download the chromedriver if you will use the navigator Chrome.
driver = webdriver.Chrome('/home/shakan/Downloads/chromedriver') #This parameter is necessary, because I use the navigator Chrome.
driver.get('https://www.instagram.com/accounts/login/?hl=pt-br&source=auth_switcher') #this is url of Instagram

'''Here you must insert your name user and your password'''
name = input('Enter with your username: ')
password = input('Enter with your password: ')

'''the input of name of user and password is same class of name. For this, I need make a 'for' trough function 'find_elements'.'''
acess = driver.find_elements_by_class_name('_2hvTZ')

user_name = acess[0] #I found two class, so the first position in my array is the input user name.
user_name.send_keys(name)

password_name = acess[1] #Logicaly, the second position is the input for password
password_name.send_keys(password)

login_acess = driver.find_element_by_class_name('Igw0E')
login_acess.submit()
