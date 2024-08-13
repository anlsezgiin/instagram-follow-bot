from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from time import sleep
import random

EMAIL = ""
PASSWORD = ""
TARGET_ACCOUNT = "https://www.instagram.com/culture/" # any account

class InstagramFollowBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def login(self):

        self.driver.get("https://www.instagram.com/")

        sleep(2)
        email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        loginButton = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')

        email.send_keys(EMAIL)
        password.send_keys(PASSWORD)
        loginButton.click()

        sleep(4)
        ignoreButton = self.driver.find_element(By.XPATH, '//div[contains(@class, "x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37")]')
        ignoreButton.click()

        sleep(4)
        notNowButton = self.driver.find_element(By.XPATH, '//button[contains(@class, "_a9--") and contains(@class, "_ap36") and contains(@class, "_a9_1") and text()="Not Now"]')
        notNowButton.click()
    
    def find_followers(self):
        sleep(4)
        self.driver.get(f"{TARGET_ACCOUNT}")

        sleep(4)
        followersButton = self.driver.find_element(By.XPATH, '//a[contains(@href, "/followers/") and contains(@role, "link")]')
        followersButton.click()

        sleep(5)
    
    def follow(self):
        counter = 1
        sleep(5)
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="button._acan")
        print("\nFollow buttons found")
 
        while True:
            
            if (follow_buttons[counter].text=="Follow" or follow_buttons[counter].text=="follow"):
                follow_buttons[counter].click()
                sleep(2)
                print(f"{counter}. account followed!")
                counter+=1
            else:
                print("Not clicked!")
                sleep(2)
                counter+=1
            

bot = InstagramFollowBot()
bot.login()
bot.find_followers()
bot.follow()



