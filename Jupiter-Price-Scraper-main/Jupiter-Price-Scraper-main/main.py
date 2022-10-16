from selenium import webdriver
from tabulate import tabulate
import math
from playsound import playsound
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
#from os import environ
msg = "Blank"
tel_group_id = "Jixed999_bot"
def send_msg_on_telegram(msg):
    telegram_api_url = f"https://api.telegram.org/bot5094707323:AAF8vnPRN2URUwv60Pva-Fy6jOCPZGO1kio/sendMessage?chat_id=-605976652&text={msg}"
    tel_resp = requests.get(telegram_api_url)
def Automate(driver):
 print("Script Started CT enter the price")
 baseprice=math.floor(float(5000))
 counter=0
 d=[]
 print(tabulate(d, headers=["Marked Price", "Selling price", "Percent","Small Discount","Med Discount","Big Discount"]))
 small=0
 big=0
 mid=0
 exception=0
 try:
     try:
      inputElement = WebDriverWait(driver, 3).until(
         EC.element_to_be_clickable((By.CSS_SELECTOR,
                                     "#__next > div.flex.flex-col.min-h-screen.justify-between > div > div.flex.flex-col.justify-between > div > div.w-full.max-w-md > div.w-full.max-w-md.pb-6.md\:pb-12.lg\:pb-24 > form > div.w-full.rounded-xl.bg-white-75.dark\:bg-white.dark\:bg-opacity-5.shadow-lg.flex.flex-col.p-4.lg\:px-6.lg\:py-8 > div.border-b.border-transparent > div > div > div > div > input")))
     except:
         inputElement = WebDriverWait(driver, 3).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR,
                                         "#__next > div.flex.flex-col.min-h-screen.justify-between > div > div.flex.flex-col.justify-between > div > div.w-full.max-w-md > div.w-full.max-w-md.pb-6.md\:pb-12.lg\:pb-24 > form > div.w-full.rounded-xl.bg-white-75.dark\:bg-white.dark\:bg-opacity-5.shadow-lg.flex.flex-col.p-4.lg\:px-6.lg\:py-8 > div.border-b.border-transparent > div > div > div > div > input")))

     inputElement.send_keys(baseprice)
 except:
     print("Exception ")
     time.sleep(5)
 while(True):
  try:
      print("WWD")
     #Refrest button
      WebDriverWait(driver, 3).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      "#__next > div.flex.flex-col.min-h-screen.justify-between > div > div.flex.flex-col.justify-between > div > div.w-full.max-w-md > div.flex.justify-end.mb-2 > div > button.rounded-full.shadow-sm.bg-white-75.dark\:bg-white-10.w-7.h-7.p-2.cursor-pointer.fill-current.text-jupiter-navy.dark\:text-white-50.disabled\:opacity-50"))).click()
      print("ugj")
      result = WebDriverWait(driver, 300).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > div.flex.flex-col.min-h-screen.justify-between > div > div.flex.flex-col.justify-between > div > div.w-full.max-w-md > div.w-full.max-w-md.pb-6.md\:pb-12.lg\:pb-24 > form > div.w-full.rounded-xl.bg-white-75.dark\:bg-white.dark\:bg-opacity-5.shadow-lg.flex.flex-col.p-4.lg\:px-6.lg\:py-8 > div.relative > div.transition-all.duration-200.overflow-hidden.animate-fade-in > div > div > div > div.cursor-pointer.relative.w-full.rounded-lg.p-0\.5.leading-tight.bg-jupiter-swap-gradient > div.flex.items-center.justify-between.p-4.rounded-lg.dark\:text-white.dark\:border-transparent.text-\[13px\].bg-white\/80.dark\:bg-\[rgba\(62\,62\,69\,0\.9\)\] > div.font-semibold.text-right.dark\:text-white.lg\:text-lg.text-xs")))
      routes = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > div.flex.flex-col.min-h-screen.justify-between > div > div.flex.flex-col.justify-between > div > div.w-full.max-w-md > div.w-full.max-w-md.pb-6.md\:pb-12.lg\:pb-24 > form > div.w-full.rounded-xl.bg-white-75.dark\:bg-white.dark\:bg-opacity-5.shadow-lg.flex.flex-col.p-4.lg\:px-6.lg\:py-8 > div.relative > p")))
      print("fweefewfwefw")
      val = result.text.replace(',', '')
      val = float(val)
      print("WWERWR")
      ##      EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div[2]/div[2]/div/div/div[6]/div[1]/span")))
      print("qda")
      h=WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > div.flex.flex-col.min-h-screen.justify-between > div > div.flex.flex-col.justify-between > div > div.w-full.max-w-md > div.w-full.max-w-md.pb-6.md\:pb-12.lg\:pb-24 > form > div.w-full.rounded-xl.bg-white-75.dark\:bg-white.dark\:bg-opacity-5.shadow-lg.flex.flex-col.p-4.lg\:px-6.lg\:py-8 > div.relative > div.transition-all.duration-200.overflow-hidden.animate-fade-in > div > div > div > div.cursor-pointer.relative.w-full.rounded-lg.p-0\.5.leading-tight.bg-jupiter-swap-gradient > div.flex.items-center.justify-between.p-4.rounded-lg.dark\:text-white.dark\:border-transparent.text-\[13px\].bg-white\/80.dark\:bg-\[rgba\(62\,62\,69\,0\.9\)\] > div:nth-child(1) > div.flex.space-x-1"))).text
      h=h.replace('\n','->')
      r=routes.text
      difference=((float(val)-float(baseprice))*100)/baseprice
      print(h)
      #msg=tabulate([['TC',baseprice,float(val),difference,small,mid,big,r[0:4],host.text]])
      current_time = time.localtime(time.time())
      formatted_time = time.asctime(current_time)
      msg='  CC ', baseprice, round(float(val),2), round(difference,2),h, small, mid, big, r[0:4],formatted_time
      print(msg)
      flag=True
      try:
       driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div[2]/form/div[2]/div/div")
       fff="High Price Impact detected"
       send_msg_on_telegram(fff)
      except:
          print("")
      if(float(difference)>0.02 and float(difference)<1):
         small=small+1
         flag=False
         send_msg_on_telegram(msg)
         playsound(r"Notification Sound.mp3")
      elif(float(difference)>1 and float(difference)<1.5):
         mid=mid+1
         send_msg_on_telegram(msg)
         flag=False
         playsound(r"Paisa Paisa Loud.mp3")
      elif(float(difference)>1.5):
         big=big+1
         flag=False
         send_msg_on_telegram(msg)
         playsound(r"Loud Notification - Tune.mp3")
      if(flag == True):
         time.sleep(5)
      else:
          time.sleep(2)
      exception=0
  except:
     print("EXCEPTION")
     exception=exception+1
     if(exception>10):
         msg='Some Problem occured with script kindly restart/contact Developer @Papa_Zentrex'
         send_msg_on_telegram(msg)
     time.sleep(5)
     continue
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
url='https://jup.ag/swap/USDC-USDC'
driver = webdriver.Chrome(executable_path=r"chromedriver.exe", chrome_options=options)
#driver.minimize_window()
driver.get(url)
driver.set_page_load_timeout(-1)
Automate(driver)
##time.sleep(10)