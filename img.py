import urllib.request
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import pyperclip
import discord
from discord.ext import commands
gptinit = False
lockdown = False
vqganinit = False
googleprofile = "1"

bot = commands.Bot('.')

@bot.event
async def on_ready():
	print("logged in as {0.user}".format(bot))
	global gptinit
	global lockdown
	global vqganinit
	global googleprofile
	gptinit = False
	lockdown = False
	activity = discord.Activity(name="c.gen help, they are in my walls", type=discord.ActivityType.watching)
	await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.event
async def on_message(message):
	global gptinit
	global lockdown
	global vqganinit
	global googleprofile
	phases = 0
	if message.author == bot.user:
		return
	if lockdown == False:
		if 'c.gen clip' in message.content:
			if 'profile' in message.content:
				googleprofile = message.content[19:len(message.content)]
				await message.channel.send("Profile set to " + googleprofile + ".")
				return
			if 'reset' in message.content:
				options = webdriver.ChromeOptions()
				#options.add_experimental_option("detach", True)
				options.add_argument(r"--user-data-dir=C:\Users\firewolf\AppData\Local\Google\Chrome\User Data")
				options.add_argument(r"--profile-directory=Profile " + (googleprofile))
				if driver is not None:
					driver.quit()
				driver = webdriver.Chrome('N:\discordbot\gpt-2-simple\chromedriver.exe', chrome_options=options)
				driver.get("https://gelbooru.com/index.php?page=post&s=list&tags=all")
				page_html = driver.page_source
				time.sleep(2)
				driver.switch_to.parent_frame()
				print("exit")
				time.sleep(1)
				driver.switch_to.parent_frame()
				actionmove2 = ActionChains(driver)
				dropdown = driver.find_element_by_xpath('//*[@id="runtime-menu-button"]')
				actionmove2.move_to_element(dropdown).perform()
				time.sleep(0.5)
				actionclick3 = ActionChains(driver)
				actionclick3.click().perform()
				actionoffset = ActionChains(driver)
				actionoffset.move_by_offset(0,344).click().perform()
				time.sleep(0.5)
				actionterm = ActionChains(driver)
				actionterm.move_by_offset(740, -51).click().perform()
				time.sleep(0.5)
				actionterm2 = ActionChains(driver)
				actionterm2.move_by_offset(25, 190).click().perform()
				await message.channel.send("Shutting down.")
				return
			aftermode = False
			if lockdown == False:
				if 'shutdown' in message.content:
					aftermode = False
				if 'standby' in message.content:
					aftermode = True
				else:
					await message.channel.send('You must specfiy shutdown or standby.')
					return
				phases = message.content[11:12]
				if aftermode == False:
					cliparg = message.content[22:len(message.content)]
				if aftermode == True:
					cliparg = message.content[21:len(message.content)]
				await message.channel.send('Generating ' + cliparg + ' for ' + str(phases) + ' phases.')
				if vqganinit == False:
					await message.channel.send('\nStarting engine, this will take a bit.')
				#lockdown = True
				if vqganinit == False:
					options = webdriver.ChromeOptions()
					#options.add_experimental_option("detach", True)
					options.add_argument(r"--user-data-dir=C:\Users\firewolf\AppData\Local\Google\Chrome\User Data")
					options.add_argument(r"--profile-directory=Profile " + (googleprofile))
					driver = webdriver.Chrome('N:\discordbot\gpt-2-simple\chromedriver.exe', chrome_options=options)
					driver.switch_to.parent_frame()
					driver.get("https://gelbooru.com/index.php?page=post&s=list&tags=all")
					page_html = driver.page_source
				time.sleep(2)
				#if vqganinit == False:
				'''button1 = driver.find_element_by_xpath('//*[@id="cell-VA1PHoJrRiK9"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button')
				button1.click()
				time.sleep(2)
				try:
					button2 = driver.find_element_by_xpath('//*[@id="ok"]')
					button2.click()
				except:
					print('not clicking')
				finally:
					print('continuing')
				time.sleep(1)
				try:
					button2 = driver.find_element_by_xpath('//*[@id="ok"]')
					button2.click()
				except:
					print('not clicking')
				finally:
					print('continuing')
				#time.sleep(1)
				#button2 = driver.find_element_by_xpath('//*[@id="ok"]')
				#button2.click()
				#time.sleep(2)
				#cell4 = driver.find_element_by_xpath('//*[@id="cell-IO09yGQNSmSd"]')
				#cell4.send_keys(Keys.RETURN, Keys.CONTROL)
				#button5 = driver.find_element_by_xpath('//*[@id="cell-IO09yGQNSmSd"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button')
				#button5.click()
				time.sleep(2)
				print('install librarys')
				cell6 = driver.find_element_by_xpath('//*[@id="cell-wSfISAhyPmyp"]')
				cell6.send_keys(Keys.RETURN, Keys.CONTROL)
				button7 = driver.find_element_by_xpath('//*[@id="cell-wSfISAhyPmyp"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button')
				button7.click()
				installlibtime = 90
				if vqganinit == True:
					installlibtime = 5
				time.sleep(installlibtime)
				print('selection of models')
				cell8 = driver.find_element_by_xpath('//*[@id="cell-FhhdWrSxQhwg"]')
				cell8.send_keys(Keys.RETURN, Keys.SHIFT)
				button9 = driver.find_element_by_xpath('//*[@id="cell-FhhdWrSxQhwg"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button')
				button9.click()
				installmodeltime = 80
				if vqganinit == True:
					installmodeltime = 5
				time.sleep(installmodeltime) #80
				print('load librarys')
				driver.find_element_by_xpath('//*[@id="cell-EXMSuW2EQWsd"]').click()
				actionsb = ActionChains(driver)
				actionsb.key_down(Keys.SHIFT).send_keys(Keys.RETURN).key_up(Keys.SHIFT).perform()
				time.sleep(12)
				print('go to old params')
				driver.find_element_by_xpath('//*[@id="cell-ZdlpRFL8UAlW"]').click()
				time.sleep(1)
				#cut

				#cell12 = driver.find_element_by_xpath('//*[@id="cell-ZdlpRFL8UAlW"]')
				#cell12.send_keys(Keys.RETURN, Keys.CONTROL)
				#cell12.click()
				#prompt = driver.find_element_by_xpath('//*[@id="cell-ZdlpRFL8UAlW"]/div[2]/div[2]/div[1]/colab-form/div/colab-form-input[1]')
				#driver.find_element_by_xpath('//*[@id="cell-ZdlpRFL8UAlW"]').send_keys(Keys.BACKSPACE)

				#cut
				newcode = driver.find_element_by_xpath('//*[@id="toolbar-add-code"]')
				newcode.click()
				#newcodetext = driver.find_element_by_xpath('//*[@id="cell-TnEftrBB74gP"]/div[2]')
				f = open("parameters.py")
				text = f.read()
				f.close()
				pyperclip.copy(text)
				actions = ActionChains(driver)
				actions.send_keys('texts =' + '\"' + cliparg + '\"\n').perform()
				actiontame = ActionChains(driver)
				#actiontame.send_keys('!pip install taming-transformers\n').perform()
				actions2 = ActionChains(driver)
				actions2.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
				#actions.send_keys(Keys.ESCAPE).perform()
				print('put params')
				time.sleep(1)
				actions3 = ActionChains(driver)
				actions3.key_down(Keys.SHIFT).send_keys(Keys.RETURN).key_up(Keys.SHIFT).perform()
				time.sleep(3)
				#driver.find_element_by_xpath('//*[@id="cell-g7EDme5RYCrt"]').click()
				actionsdupe = ActionChains(driver)
				actionsdupe.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT).perform()
				actionmove = ActionChains(driver)
				print('AI start')
				actiondown = ActionChains(driver)
				time.sleep(1)
				actiondown.send_keys(Keys.ARROW_DOWN).perform()
				actiondown2 = ActionChains(driver)
				actiondown2.send_keys(Keys.ARROW_DOWN).perform()
				actiondown2.send_keys(Keys.ARROW_DOWN).perform()
				time.sleep(28)
				iframe = driver.find_element_by_xpath('//iframe')
				driver.switch_to.frame(iframe)
				time.sleep(1)
				#img = driver.find_element_by_xpath('//*[@id="output-body"]/div[11]/div/img')
				images = driver.find_elements_by_tag_name('img')
				while len(images) > 1:
					print("blocking")'''
				counter = 0
				images = driver.find_elements_by_tag_name('img')
				while counter < int(phases):
					print(len(images))
					print(counter, phases)
					images = driver.find_elements_by_tag_name('img')
					for index, image in enumerate(images):
						print(index, counter, phases)
						source = image.get_attribute("src")
						#print('image found', index, counter)
						if index >= counter:
							urllib.request.urlretrieve(source, filename="progress" + str(counter) + ".png")
							#driver.save_screenshot("progress.png")
							await message.channel.send('Phase ' + str(counter) + ' for ' + cliparg + ':')
							await message.channel.send(file=discord.File(r"N:/discordbot/gpt-2-simple/progress" + str(counter) + ".png"))
							print(index)
							counter = counter + 1
				vqganinit = True
				print(aftermode)
				if aftermode == False:
					print("exit")
					time.sleep(1)
					driver.switch_to.parent_frame()
					actionmove2 = ActionChains(driver)
					dropdown = driver.find_element_by_xpath('//*[@id="runtime-menu-button"]')
					actionmove2.move_to_element(dropdown).perform()
					time.sleep(0.5)
					actionclick3 = ActionChains(driver)
					actionclick3.click().perform()
					actionoffset = ActionChains(driver)
					actionoffset.move_by_offset(0,344).click().perform()
					time.sleep(0.5)
					actionterm = ActionChains(driver)
					actionterm.move_by_offset(740, -51).click().perform()
					time.sleep(0.5)
					actionterm2 = ActionChains(driver)
					actionterm2.move_by_offset(25, 190).click().perform()
					await message.channel.send("Shutting down.")
					driver.quit()
					return
				else:
					driver.switch_to.parent_frame()
					stopbutt = driver.find_element_by_xpath('//*[@id="cell-g7EDme5RYCrt"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button')
					time.sleep(0.5)
					actionstandclick = ActionChains(driver)
					actionstandclick.move_to_element(stopbutt).click().perform()
					actionfinalterm = ActionChains(driver)
					await message.channel.send("Standing by. Enter another prompt soon.")
					actiongouppre = ActionChains(driver)
					actiongouppre.send_keys(Keys.ARROW_UP).perform()
					actiongoup = ActionChains(driver)
					actiongoup.send_keys(Keys.ARROW_UP).perform()
					actiongoup.send_keys(Keys.ARROW_UP).perform()
					time.sleep(0.5)
					actionfinalterm.key_down(Keys.CONTROL).key_down("m").send_keys("i").key_up(Keys.CONTROL).key_up("m").perform()
					time.sleep(2)
					return
	if message.author == bot.user:
		return
bot.run('OTYzOTU2NzA3NDA5Njc4MzM2.YldopA.v4nepZWBzXDP6pDsx_NuRMRmfgM')