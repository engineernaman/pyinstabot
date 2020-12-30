#main.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import login
import getpages

driver = 0
username = input("Enter Username. : ") # the actual username of the user
password = input("Enter Password. : ") # the password of the user account

def main():
	
	global driver
	driver = webdriver.Chrome("chromedriver.exe") 
	#path where the browser driver exist
	#we an change the browser used, by simply changing the name and driver
	l = login.Login(driver, username , password)
	l.signin()
	#driver.get('https://www.instagram.com/leomessi/?hl=en')
	gp = getpages.Getpages(driver)
	n = int(gp.get_num_flw()//10)
	print(n)
	refs = gp.get_followers()
	run_bot(refs, driver, gp)

def run_bot(refs, driver, gp):
	#global refs, driver
	t = time.time()
	L = 0 #Pages Liked
	F = 0 #Pages Followed
	for r in refs:
		driver.get('https://www.instagram.com'+r)
		time.sleep(2)
		if gp.get_num_flw() > 3000:
			if gp.is_public():
				print('Public Account')
				print('Current Likes: '+str(L))
				if L < 350:
					gp.like_post()
					L+=1
					print('Post Liked !!')
				else:
					time.sleep(3600)
			else:
				print('Account is private.')
				print('Current Follows : '+str(F))
				if F < 50:
					time.sleep(2)
					gp.follow_page()
					print('Page Followed!!')
					F+=1
				else:
					time.sleep(3600)

if __name__ == "__main__" :
	main()