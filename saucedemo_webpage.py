"""
Visit the URL https://www.saucedemo.com/ and login with the following credentials:-
    username = 'standard_user'
    password = 'secret_sauce'

    Try to fetch the following using Selenium Python:-
        1. Title of the webpage.
        2. Current URL o f the webpage.
        3. Extract the entire contents of the webpage and save it in a text file whose name will be 'Webpage_task_11.txt'.

"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


class Saucedemo:

    # Locators Data
    username_locator = 'user-name'
    password_locator = "password"
    button_locator = "/html/body/div[1]/div/div[2]/div[1]/div/div/form/input"
    login_status=False

    #Construtor for the class
    def __init__(self, url,username,password):
        self.url=url
        self.username=username
        self.password=password
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    #Method to start the webpage automation
    def start_automation(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True

        except Exception as _:
            print("Error: Unable to Start Python Automation")
            return False

    #Method to login into the webpage
    def webpage_login(self):
        if self.start_automation():
            global login_status
            self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
            sleep(2)
            self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
            sleep(2)
            self.driver.find_element(by=By.XPATH, value=self.button_locator).click()
            if self.driver.current_url!=self.url:
                self.login_status = True
                return True
            else:
                return False
        else:
            print("Error: Unable to Login to the webpage")

    #Method to fetch the contents of the webpage
    def fetch_details(self):
        if self.login_status == True:
            data= self.driver.page_source
            page_text= self.driver.find_element(by=By.XPATH, value='/html/body').text

            #File Handaling to fetch the entire webpage content in HTML
            with open('Webpage_task_11.txt','w') as f:
                f.write(data)

            #File Handling to fetch the text present in the webpage
            with open('Webpage_text.txt','w') as f:
                f.write(page_text)
            return True
        else:
            return False

    #Method to fetch the current URL of the webpage
    def fetch_weburl(self):
        if self.login_status == True:
            return self.driver.current_url
        else:
            return 'Invalid Login'

    #Method to fetch the title of the webpage
    def fetch_webpage_title(self):
        if self.login_status == True:
            return self.driver.title
        else:
            return 'Invalid Login'


    #Method to logout of the webpage
    def webpage_logout(self):
        if self.login_status == True:
            self.driver.find_element(by=By.ID, value='react-burger-menu-btn').click()
            sleep(2)
            self.driver.find_element(by=By.ID, value='logout_sidebar_link').click()
            sleep(2)
            return True
        else:
            print("Unable to Logout : Invalid Login")
            return False

    #Method to close the webpage
    def shutdown_automation(self):
        self.driver.quit()
        return None


if __name__ == '__main__':
    url='https://www.saucedemo.com/'

    #Valid User
    ketchup=Saucedemo(url,'standard_user','secret_sauce')
    ketchup.start_automation()
    ketchup.webpage_login()
    print(ketchup.fetch_webpage_title())
    print(ketchup.fetch_weburl())
    ketchup.fetch_details()
    ketchup.webpage_logout()
    ketchup.shutdown_automation()

    # #Invalid User
    # mayo=Saucedemo(url,'locked_out_user','secret_sauce')
    # mayo.start_automation()
    # mayo.webpage_login()
    # mayo.fetch_webpage_title()
    # mayo.fetch_weburl()
    # mayo.fetch_details()
    # mayo.webpage_logout()
    # mayo.shutdown_automation()



