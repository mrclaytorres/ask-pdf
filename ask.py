from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import subprocess
import random
import pandas as pd
import datetime
import sys
import os
import os.path
import time
# import creds
import csv
import re
import glob
import env

def initialize_browser():

  directory = os.path.dirname(os.path.realpath(__file__))
  driver_path = os.path.join(directory, glob.glob('chromedriver*')[0])

  user_agents = user_agent()

  # Setup random proxy and user-agent
  random_user_agents = random.randint(1, len(user_agents) - 1)
  print(user_agents[random_user_agents])

  chrome_options = Options()
  chrome_options.add_argument("--disable-extensions")
  chrome_options.add_argument("--log-level=3")
  chrome_options.add_argument("--start-maximized")
  prefs = {
      "profile.default_content_settings.popups": 0,
      # Used when you have to download something from the browser
      # "download.default_directory" : env.DOWNLOAD_DIRECTORY,
      "directory_upgrade": True,
      "user-agent": user_agents[random_user_agents]
      }
  chrome_options.add_experimental_option("prefs", prefs)

  browser = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
  
  return browser

def user_agent():
    user_agent_list = []
    with open('user_agents.csv', 'r') as f:
        for agents in f:
            user_agent_list.append(agents)
    return user_agent_list

def ask_pdf():
  
  time_start = datetime.datetime.now().replace(microsecond=0)
  
  # Initialize variables
  pdf_filenames = []
  pdf_ids = []

  # AutoIt Scripts executables
  dir_path = os.path.dirname(os.path.realpath(__file__))
  uploadfile_script = dir_path + r"\upload_pdf.exe"
  move_file = dir_path + r"\move_file.exe"
  uploaded_file = dir_path + r"\uploaded.exe"

  # Check how many pdfs does pdf folder contains and use it as loop counter
  pdf_count = 0
  directory = os.path.dirname(os.path.realpath(__file__))
  pdf_directory = os.path.join(directory,'pdf/')
  upload_directory = os.path.join(directory,'uploads/')
  os.chdir(pdf_directory)
  print(f'Changing directory to {pdf_directory}\n')

  for path in os.listdir(pdf_directory):
    #check if current path is a file
    if os.path.isfile(os.path.join(pdf_directory, path)):
      pdf_count += 1
  print('File count:', pdf_count)

  # After determining the pdf count, go back to the root dir
  os.chdir(directory)

  loop_count = 0

  while pdf_count > loop_count:

    browser = initialize_browser()
    browser.get('https://askyourpdf.com/')

    try:
      
      # Move pdf file from pdfs to uploads - ready for upload
      os.system(move_file)

      WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section/main/main/div[2]/div/span/div[1]/span/div/div/div/div/div/div[2]/div/div/div'))).click()
      time.sleep(5)

      # Upload the pdf file to askyourpdf
      os.system(uploadfile_script)
      time.sleep(20)

      # Extract informations
      print(f"Current browser: {browser.current_url}")
      WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section/main/div/div[2]/div/form/button[2]'))).click()
      url = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/span'))).text
      pdf_ids.append(browser.current_url)
      time.sleep(5)
      WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/button'))).click()
      time.sleep(5)
      WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section/main/div/header/div/div/div[3]/button[2]'))).click()

      # Get the current pdf filename
      os.chdir(upload_directory)

      for path in os.listdir(upload_directory):
        #check if current path is a file
        if os.path.isfile(os.path.join(upload_directory, path)):  
          print(f"Current PDF: {path}")
          pdf_filenames.append(path)

      # After determining the pdf filename, go back to the root dir
      os.chdir(directory)

      # Move uploaded pdf file to uploaded folder
      os.system(uploaded_file)
      time.sleep(10)

      loop_count += 1
      time.sleep(5)

      browser.quit()

    except:
      
      pdf_ids.append(browser.current_url)

      # Get the current pdf filename
      os.chdir(upload_directory)

      for path in os.listdir(upload_directory):
        #check if current path is a file
        if os.path.isfile(os.path.join(upload_directory, path)):  
          print(f"Current PDF: {path}")
          pdf_filenames.append(path)

      # After determining the pdf filename, go back to the root dir
      os.chdir(directory)

      # Move uploaded pdf file to uploaded folder
      os.system(uploaded_file)
      time.sleep(10)

      loop_count += 1
      browser.quit()

      print("\nUnexpected error occured.")
      
      pass

  # Save scraped URLs to a CSV file   
  now = datetime.datetime.now().strftime('%Y%m%d-%Hh%M')
  print('Saving to a CSV file...')
  data = {"Filename":pdf_filenames, "PDF ID URL":pdf_ids}
  df = pd.DataFrame.from_dict(data, orient='index')
  df = df.transpose()

  filename = f"askpdf{ now }.csv"
  file_path = os.path.join(directory,'csvfiles/', filename)
  df.to_csv(file_path)

  print(f'Your file {filename} is ready.\n')

  time_end = datetime.datetime.now().replace(microsecond=0)
  runtime = time_end - time_start
  print(f"Script runtime: {runtime}.")

if __name__ == '__main__':
  ask_pdf()