#to get all pages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import pyautogui


class Getpages:
	def __init__(self, driver):
		self.driver = driver
		self.driver.get('https://www.instagram.com/instagram/?hl=en')
		self.hrefs = []
			#12 pages on one loading

	def get_num_flw(self):
		time.sleep(1)
		flw = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main')))
		sflw = b(flw.get_attribute('innerHTML'), 'html.parser')
		#print(sflw)  //i used this to get the class name and finally get exact location
		followers = sflw.findAll('span', {'class':'g47SY'})
		f = followers[1].getText().replace(',', '')
		#print(F) // to check at what index is the followers are at
		if 'k' in f:
			f = float(f[:-1]) * 10**3
			return f
		elif 'm' in f:
			f = float(f[:-1]) * 10**6
			return f
		else:
			return float(f)



	"""def get_followers(self):
					time.sleep(2)
					#self.driver.get('https://www.instagram.com/engineer_naman/?hl=en')
					time.sleep(2)
					flw = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main')))
					sflw = b(flw.get_attribute('innerHTML'), 'html.parser')
					#print(sflw)  //i used this to get the class name and finally get exact location
					followers = sflw.findAll('span', {'class':'g47SY'})[1]
					followers.click()
					
					#flw_btn = self.driver.find_element_by_css_selector('#react-root > section > main > div > ul > li:nth-child(2) > a > span')[0]
					#flw_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/ul/li[2]/a/span")))
					#print(flw_btn)
					#flw_btn = self.driver.find_element_by_css_selector("#react-root > section > main > div > ul > li:nth-child(2) > a > span")
					flw_btn.click()
					time.sleep(30)
					#the above css path of button may change depending upon the instagram working
					#the xpath of the popup window of followers
					self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
					'''for i in range (15):
						time.sleep(2)
						self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(h), popup)
					self.popup = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]')))
					b_popup = b(self.popup.get_attribute('innerHTML'), 'html.parser')
					for p in b_popup.findAll('li', {'class': 'wo9IH'}):
						print(p.findAll('a', {'class':'FPmhX notranslate  _0imsa '})[0])
					'''
			"""
	def is_public(self):
		try:
			astate = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'rkEop')))
			if astate.text == 'This Account is Private':
				return False
			else:
				return True
		except:
			return True


	def like_post(self):
		post = self.driver.find_element((By.CSS_SELECTOR, '#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1) > a'))
		html = post.get_attribute('innerHTML')
		h = b(html, 'html.parser')
		href = h/a['href']
		self.driver.get('https://www.instagram.com' + href)

		like_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')))
		like_btn.click()

	def follow_page(self):
		follow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > div.Y2E37 > button')))
		f_text = follow.text
		if f_text.lower() == 'follow' or f_text.lower() == 'follow back':
			follow.click()
		elif f_text == 'already following':
			print('already following')

	def get_followers(self):
			time.sleep(2)
			flw_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > span')))
			flw_btn.click()
			time.sleep(3)
			self.popup = WebDriverWait(self.driver, 10). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]')))
			for h in range(11):
				time.sleep(1)
				print('scrolling')
				print(h)
				print('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)))
				self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)), self.popup)
				if h == 5:
					break
			for i in range(40):
				time.sleep(2)
				self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', self.popup)
			self.popup = WebDriverWait(self.driver, 10). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]')))
			b_popup = b(self.popup.get_attribute('innerHTML'), 'html.parser')
			for p in b_popup.findAll('li', {'class': 'wo9IH'}):
				try:
					hlink = p.find_all('a')[0]['href']
					print(hlink)
					if 'div' in hlink:
						print('div found not adding to list')
					else:
						self.hrefs.append(hlink)
				except:
					pass
			return self.hrefs
	"""def get_followers(self, n):
								time.sleep(1)
								driver = self.driver
								time.sleep(5)
								# Change this function according to need
								flw_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')))
								flw_btn.click()
								popup = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]')))
						
								for i in range(15): #change this 15 for more followers
									time.sleep(1)
									self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
								popup = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]')))
								b_popup = b(popup.get_attribute('innerHTML'), 'html.parser')
								for p in b_popup.findAll('li', {'class': 'wo9IH'}):
									try:
										hlink = p.findAll('a')[0]['href']
										
										if 'div' in hlink:
											return self.href
										else:
											self.href.append(hlink)
									except:
										pass
								return self.hrefs
						"""			

			#f = followers[1].getText().replace(',', '')
"""for h in range(10):
											time.sleep(1)
											self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(11-h), popup)
										#self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
										for i in range (15):
											time.sleep(2)
											self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(h), popup)
											popup = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]')))
											
										"""		




"""
				pyautogui.press("tab")
		pyautogui.press("tab")
		pyautogui.press("tab")
		pyautogui.press("tab")
		pyautogui.press("tab")
		pyautogui.press("tab")
		pyautogui.press("tab")
		pyautogui.press("enter")"""

	