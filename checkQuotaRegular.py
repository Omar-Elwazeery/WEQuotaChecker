import sys
import os
from colorama import Fore, init
import colorama
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
init()

sys.stdout.write("\x1b]0;[+] [BW] Check the remaining quota of WE [Mostafa Mohamed] [+]\x07")
print(Fore.MAGENTA + """
888       888 8888888888       .d88888b.  888     888  .d88888b. 88888888888     d8888 
888   o   888 888             d88P" "Y88b 888     888 d88P" "Y88b    888        d88888 
888  d8b  888 888             888     888 888     888 888     888    888       d88P888 
888 d888b 888 8888888         888     888 888     888 888     888    888      d88P 888 
888d88888b888 888             888     888 888     888 888     888    888     d88P  888 
88888P Y88888 888             888 Y8b 888 888     888 888     888    888    d88P   888 
8888P   Y8888 888             Y88b.Y8b88P Y88b. .d88P Y88b. .d88P    888   d8888888888 
888P     Y888 8888888888       "Y888888"   "Y88888P"   "Y88888P"     888  d88P     888 
                                     Y8b                                               
                                                                 """)
print("")
print(Fore.YELLOW + "                [+]",Fore.CYAN +" Dev : Mostafa Mohamed ",Fore.YELLOW+"[+]")
print(Fore.YELLOW + "                    [+]",Fore.WHITE +" Fb.com/vk0x65 ",Fore.YELLOW+"[+]")
print(Fore.YELLOW + "                 [+]",Fore.MAGENTA +" WE REMAINING QUOTA ",Fore.YELLOW+"[+]")
print("")

try:
    user = input("Please enter your phone number (ex: 0551234567) : ")
    passwd = input("Please enter your password : ")
    os.environ['MOZ_HEADLESS'] = '1'
    driver = webdriver.Firefox()
    driver.get("https://my.te.eg/user/login")
    element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div[1]/app-login/div/div/div/p-card[1]/div/div/div/form/div/div[1]/p-inputmask/input')))
    element.send_keys(user)
    element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    element.send_keys(passwd)
    button = driver.find_element(By.XPATH, '/html/body/app-root/div/div[1]/app-login/div/div/div/p-card[1]/div/div/div/form/div/button[1]').click()
    driver.implicitly_wait(3)
    remaining = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div[1]/app-dashboard/div/div/div[3]/p-card/div/div/div/div[2]/p-carousel/div/div/div/div/div/div/app-gauge/div[2]/span[1]')))
    print(Fore.CYAN +" REMAINING QUOTA : " + Fore.GREEN +remaining.text[0:5]+Fore.WHITE+" GB")
    input("Press Enter to close...")
    driver.quit()
except:
    print(Fore.RED +"Your connection isn't stable .. try again later!")
    input("Press Enter to close...")
    driver.quit()