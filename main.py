import pyautogui
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from src.utils import chrome_browser_options
import csv 
from src.user_config import work,location_user
import openai
from src.apikeys import api_key
from openai import OpenAIError
import os
from src.cv_txt import cv
from src.question_and_answer import questions_and_answer
from selenium.common.exceptions import NoSuchElementException
from class_1 import ChatGPTBot


     
API_KEY = api_key


automation = ChatGPTBot(API_KEY)

try:
    # star Chrome and loggin
    automation.init_browser()
    automation.loginn()

    # Search jobs
    print("Searching your deamer job...")
    automation.search_jobs()
    new_driver = automation.driver.current_url
    for pages in range(2,5):
            
        print(new_driver)
        automation.scraper_job()
        automation.enter_application_jobs()
        sleep(2)
        automation.driver.get(new_driver+ f"?&page={pages}")
        sleep(2)
        try:
            automation.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
        except Exception as e:
            print(f"Error: {e}")
            


    sleep(5)



except Exception as e:
    print(f"Something going wrong: {e}")

finally:

    automation.close_browser()
    print("Closing windows.")