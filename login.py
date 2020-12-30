#login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time




class Login:  
	def __init__(self,driver, username, password):
		self.driver = driver
		self.username = username
		self.password = password

	def signin(self):
		self.driver.get("https://www.instagram.com/accounts/login/?hl=en")
		uid = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')))
		#the above line is to connect insta sign in page and select username field
		#the sign in page url and the CSS selector path can change time to time therefore must check it once before use
		#to get CSS path inspect element username block > right click > copy > path selector
		uid.click()
		uid.send_keys(self.username)
		# by above lines we will input username
		
		pswd = self.driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input')
		# the css selector may vary
		pswd.click()
		pswd.send_keys(self.password)
		#by above we will input password
		
		btn = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button > div")
		#above line is for selecting submit buttton, css selector path may vary
		btn.click()
		time.sleep(10)