import urllib.request
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import pyperclip
import datetime
from mimetypes import guess_extension
#from seleniumwire import webdriver  # Import from seleniumwire
from selenium import webdriver
from urllib.parse import urlparse
import bs4
import pyautogui
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"

os.environ["CUDA_VISIBLE_DEVICES"]="1"


#actionmove.move_to_element(finalbutton).perform()
#actionoffset = ActionChains(driver)
#actionoffset.move_by_offset(315, 330).perform()
#actionoffset.move_by_offset(200, 200).perform()
#actionrclick = ActionChains(driver)
#actionrclick.context_click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()
#pyautogui.moveTo
#actionmenu.move_by_offset(20, 50).perform()
#time.sleep(1)
#actionclick2 = ActionChains(driver)
#actionclick2.click().perform()
#actionenter = ActionChains(driver)
#time.sleep(1)
#counter = 0
#actionenter.send_keys('snapshot'+ str(counter)+'.png').perform()
#actionsave = ActionChains(driver)
#actionsave.send_keys(Keys.RETURN).peform()
#images = driver.find_elements_by_tag_name('img')
'''for img in images:
	counter = counter + 1
	source = img.get_attribute("src")
	time.sleep(1)
	print(counter)
	urllib.request.urlretrieve(source, filename="progress" + str(counter) + ".jpg")
driver.find_element_by_class_name('//*[@id="output-body"]/div[4]/div')'''


import discord
import os
import requests
import json
import datetime
#import gpt_2_simple as gpt2
import asyncio, random, string
import random
import sys
import PIL
from PIL import Image, ImageFont, ImageDraw
from discord.ext import commands
sys.path.append('F:/Downloads 2/')
sys.path.append('C:/')



gptinit = False
lockdown = False
vqganinit = False
tflock = False
googleprofile = "2"
#client = discord.Client()
intents = discord.Intents(message_content=True, messages=True, reactions=True)
bot = commands.Bot('.', intents=intents)
#client = commands.Bot(command_prefix=["c."], case_insensitive = True)





def has__numbers(inputString):
	return any(char.isdigit() for char in inputString)


@bot.event
async def on_ready():
	print("logged in as {0.user}".format(bot))
	global gptinit
	global lockdown
	global vqganinit
	global googleprofile
	vqganinit = False
	gptinit = False
	lockdown = False
	activity = discord.Activity(name=".c help, they are in my walls", type=discord.ActivityType.watching)
	await bot.change_presence(status=discord.Status.online, activity=activity)
#@client.command()
#async def nipah(message):
#	await message.channel.send('nipah')
#@client.command()
#async def helpme(message):
#	await message.channel.send('c.gen - Generates a message.\n\nLength, temp (temperature), and topic are all optional arguments.\n\nExample: c.gen length 50 temp 0.4 topic I really like it when')
@bot.event
async def on_message(message):
	global gptinit
	global lockdown
	global vqganinit
	global googleprofile
	global tflock
	phases = 0
	if message.author == bot.user:
		return
	if lockdown == False:
		if '.c dalle' in message.content:
			dprompt =  message.content[9:len(message.content)]
			s = Service('N:\discordbot\gpt-2-simple\chromedriver.exe')
			driver = webdriver.Chrome(service=s)
			driver.get("https://huggingface.co/spaces/dalle-mini/dalle-mini")
			time.sleep(1)
			iframe = driver.find_element_by_xpath('//iframe')
			time.sleep(1)
			driver.switch_to.frame(iframe)
			driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div/div/section[2]/div/div[1]/div[3]/div/div[1]/div/input').send_keys(dprompt)
			#time.sleep(0.2)
			driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div/div/section[2]/div/div[1]/div[3]/div/div[1]/div/input').send_keys(Keys.ENTER)
			images = driver.find_elements_by_tag_name('img')
			time.sleep(15)
			for image in images:
				source = image.get_attribute("src")
				urllib.request.urlretrieve(source, filename=dprompt + ".jpeg")
				await message.channel.send(file=discord.File(r"N:/discordbot/gpt-2-simple/" + dprompt + ".jpeg"))
			return


			return
		if '.c clip' in message.content:
			if 'profile' in message.content:
				googleprofile = message.content[16:len(message.content)]
				await message.channel.send("Profile set to " + googleprofile + ".")
				return
			if 'reset' in message.content:
				options = webdriver.ChromeOptions()
				#options.add_experimental_option("detach", True)
				options.add_argument(r"--user-data-dir=C:\Users\firewolf\AppData\Local\Google\Chrome\User Data")
				options.add_argument(r"--profile-directory=Profile " + (googleprofile))
				#if driver is not None:
					#driver.quit()
				s = Service('N:\discordbot\gpt-2-simple\chromedriver.exe')
				driver = webdriver.Chrome(service=s)
				driver.get("https://colab.research.google.com/github/justinjohn0306/VQGAN-CLIP/blob/main/VQGAN%2BCLIP(Updated).ipynb")
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
				elif 'standby' in message.content:
					aftermode = True
				else:
					await message.channel.send('You must specfiy shutdown or standby.')
					return
				if has__numbers(message.content):
					print('good phases')
				else:
					await message.channel.send('You must specfiy phase count.')
					return
				phases = message.content[8:9]
				owner = message.author
				if aftermode == False:
					cliparg = message.content[19:len(message.content)]
				if aftermode == True:
					cliparg = message.content[18:len(message.content)]
				await message.channel.send('Generating ' + cliparg + ' for ' + str(phases) + ' phases.')
				if vqganinit == False:
					fontsize = 90
					randomfont = random.choice(os.listdir("N:\discordbot\gpt-2-simple\konts"))
					try:
						font = ImageFont.truetype(randomfont, fontsize)
					except:
						try:
							randomfont = random.choice(os.listdir("N:\discordbot\gpt-2-simple\konts"))
							font = ImageFont.truetype(randomfont, fontsize)
						except:
							randomfont = random.choice(os.listdir("N:\discordbot\gpt-2-simple\konts"))
							font = ImageFont.truetype(randomfont, fontsize)
					finally:
						while font.getsize("Engine is starting...")[0] > 508:
							fontsize -= 1
							font = ImageFont.truetype(randomfont, fontsize)
						randomcat = (random.choice(os.listdir(r'F:/Downloads 2/stylegan2-ada-main/acceptdata')))
						basememe = Image.open((r"F:/Downloads 2/stylegan2-ada-main/acceptdata/" + randomcat + "/" + (random.choice(os.listdir(r'F:/Downloads 2/stylegan2-ada-main/' + randomcat + '/')))))
						draw = ImageDraw.Draw(basememe)
						draw.text((20, 40), "Engine is starting...", fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0), font=font)
						draw.text((20, 400), "Please be patient!", fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0), font=font)
						basememe.save("HereIsMeme.jpg")
						await message.channel.send(file=discord.File("HereIsMeme.jpg"))
						os.remove("HereIsMeme.jpg")
				#lockdown = True
				options = webdriver.ChromeOptions()
				#options.add_experimental_option("detach", True)
				options.add_argument(r"--user-data-dir=C:\Users\rin\AppData\Local\Google\Chrome\User Data")
				options.add_argument(r"--profile-directory=Profile " + (googleprofile))
				s = Service('N:\discordbot\gpt-2-simple\chromedriver.exe')
				driver = webdriver.Chrome(service=s)
				driver.get("https://colab.research.google.com/github/justinjohn0306/VQGAN-CLIP/blob/main/VQGAN%2BCLIP(Updated).ipynb")
				page_html = driver.page_source
				time.sleep(2)
				driver.switch_to.parent_frame()
				time.sleep(4)
				print("inited")
				#if vqganinit == False:
				button1 = driver.find_element_by_xpath('//*[@id="cell-VA1PHoJrRiK9"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button')
				button1.click()
				print("button1")
				time.sleep(5)
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
				time.sleep(0.5)
				try:
					button2 = driver.find_element_by_xpath('//*[@id="ok"]')
					button2.click()
				except:
					print('not clicking')
				finally:
					print('continuing')
				time.sleep(0.5)
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
				time.sleep(2)
				#cell4 = driver.find_element_by_xpath('//*[@id="cell-IO09yGQNSmSd"]')
				#cell4.send_keys(Keys.RETURN, Keys.CONTROL)
				#button5 = driver.find_element_by_xpath('//*[@id="cell-IO09yGQNSmSd"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button')
				#button5.click()
				time.sleep(2)
				#driver.find_element_by_xpath('//*[@id="cell-eq0-E5mjSpmP"]').send_keys(Keys.RETURN, Keys.CONTROL)
				#driver.find_element_by_xpath('//*[@id="cell-eq0-E5mjSpmP"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button').click()
				time.sleep(0.5)
				#driver.find_element_by_xpath('//*[@id="cell-IO09yGQNSmSd"]').send_keys(Keys.RETURN, Keys.CONTROL)
				#driver.find_element_by_xpath('//*[@id="cell-IO09yGQNSmSd"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button').click()
				print('install librarys')
				time.sleep(1)
				cell6 = driver.find_element_by_xpath('//*[@id="cell-wSfISAhyPmyp"]')
				cell6.send_keys(Keys.RETURN, Keys.CONTROL)
				button7 = driver.find_element_by_xpath('//*[@id="cell-wSfISAhyPmyp"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button')
				button7.click()
				print(vqganinit)
				installlibtime = 90
				if vqganinit == True:
					installlibtime = 5
				time.sleep(installlibtime)
				print('selection of models')
				cell8 = driver.find_element_by_xpath('//*[@id="cell-FhhdWrSxQhwg"]')
				cell8.send_keys(Keys.RETURN, Keys.SHIFT)
				button9 = driver.find_element_by_xpath('//*[@id="cell-FhhdWrSxQhwg"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button')
				button9.click()
				installmodeltime = 90
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
				time.sleep(41)
				iframe = driver.find_element_by_xpath('//iframe')
				time.sleep(1)
				driver.switch_to.frame(iframe)
				#img = driver.find_element_by_xpath('//*[@id="output-body"]/div[11]/div/img')
				counter = 0
				images = driver.find_elements_by_tag_name('img')
				send = ["faggg"]
				#while len(images) > 1:
					#print("blocking")
				while counter < int(phases):
					#print("list old " + str(send))
					images = driver.find_elements_by_tag_name('img')
					for index, image in enumerate(images):
						#print(index, counter, phases, len(images))
						source = image.get_attribute("src")
						#print('image found', index, counter)
						if len(images) > counter:
							if str(images.index(image)) not in send:
								urllib.request.urlretrieve(source, filename="progress" + str(counter) + ".png")
								#driver.save_screenshot("progress.png")
								await message.channel.send('Phase ' + str(counter) + ' for ' + cliparg + ':')
								await message.channel.send(file=discord.File(r"N:/discordbot/gpt-2-simple/progress" + str(counter) + ".png"))
								#print(index)
								counter = counter + 1
								send.append(str(images.index(image)))
								#print("list new " + str(send))
							else:
								print("not sending")
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
					await message.channel.send(f"@{owner}")
					await message.channel.send("Standing by. Enter another prompt soon.")
					actiongouppre = ActionChains(driver)
					actiongouppre.send_keys(Keys.ARROW_UP).perform()
					actiongoup = ActionChains(driver)
					actiongoup.send_keys(Keys.ARROW_UP).perform()
					actiongoup.send_keys(Keys.ARROW_UP).perform()
					time.sleep(0.5)
					actionfinalterm.key_down(Keys.CONTROL).key_down("m").send_keys("i").key_up(Keys.CONTROL).key_up("m").perform()
					time.sleep(1)
					driver.quit()
					return
	if message.author == bot.user:
		return
	roll = random.randint(1,100)
	if message.content.startswith('.c') or roll == 8:
		if 'clip' in message.content:
			return
		if '.c help' in message.content:
			await message.channel.send('.c - Generates a message.\n\nLength, temp (temperature), and topic are all optional arguments.\n\nExample: `.c length 50 temp 0.8 topic I really like it when`')
			return
	
	
		if roll == 8:
			ctopic = message.content
		if 'tf' in message.content:
				if tflock == False:
					tflock = True
					await message.channel.send("GPU applications locked.")
					return
				else:
					tflock = False
					await message.channel.send("GPU applications unlocked.")
					return

		if 'length' in str(message.content):
			index = message.content.index("length ")
			await message.channel.send("Length: " + message.content[index+7:index+10])
			clength = int(message.content[index+7:index+10])
		else:
			clength = 132
		if 'temp' in str(message.content):
			index = message.content.index("temp ")
			await message.channel.send("Temperature: " + message.content[index+5:index+8])
			ctemp = float(message.content[index+5:index+8])
		else:
			ctemp = 0.9
		if 'topic' in str(message.content):
			index = message.content.index("topic ")
			if not " " in message.content[index+6:len(message.content)]:
				ctopic = message.content[index+6:len(message.content)]
			else:
				ctopic = str(message.content[index+6:])
				print(ctopic)
			if 'length' in ctopic or 'temp' in ctopic:
				await message.channel.send("Topic must be the last argument specified.")
				return
			await message.channel.send("Topic: " + ctopic)
		else:
			ctopic = " "
		if tflock == True:
				await message.channel.send("GPU applications are currently locked.")
				return
		async with message.channel.typing():
			if 'jeffymode' in message.content:
				clength = random.randint(40, 150)
				ctemp = 0.9
				index = message.content.index(".c jeffymode")
				ctopic = ctopic = message.content[index+12:len(message.content)]
			if gptinit == False:
				global sess
				sess = gpt2.start_tf_sess()
				gpt2.load_gpt2(sess, run_name='345M') # The name of your checkpoint
				gptinit = True
			gentext = (gpt2.generate(sess, run_name="345M", temperature=ctemp, nsamples=1, batch_size=1, prefix=ctopic, length=clength, include_prefix=True, return_as_list=True))
			gentexted = ' '.join(gentext)
			await message.channel.send(gentexted)
	#	roll = random.randint(1,10)
	#	if roll == 3:
	#		gentext = (gpt2.generate(sess, run_name="345M", temperature=0.9, nsamples=1, batch_size=1, prefix=" ", length=132, include_prefix=False, return_as_list=True))
	#		gentexted = ' '.join(gentext)

	#		await message.channel.send(gentexted) 

#bot.run('OTYzOTU2NzA3NDA5Njc4MzM2.YldopA.v4nepZWBzXDP6pDsx_NuRMRmfgM')
loop = asyncio.get_event_loop()
loop.create_task(bot.start('OTYzOTU2NzA3NDA5Njc4MzM2.YldopA.v4nepZWBzXDP6pDsx_NuRMRmfgM'))
loop.run_forever()