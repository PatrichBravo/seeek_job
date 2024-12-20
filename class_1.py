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
from src.logging import logger

class BrowserAutomation:
    def __init__(self):
        try:
            self.options = chrome_browser_options()  # Configuración personalizada
            self.service = ChromeService(ChromeDriverManager().install())
            self.driver = None
        except Exception as e:
            raise RuntimeError(f"Failed to initialize browser setup: {str(e)}")

    def init_browser(self):
        try:
            self.driver = webdriver.Chrome(service=self.service, options=self.options)
        except Exception as e:
            raise RuntimeError(f"Failed to initialize browser: {str(e)}")

    def loginn(self):
        if not self.driver:
            raise RuntimeError("Browser not initialized. Call init_browser() first.")
        
        self.driver.get('https://login.seek.com/login?state=hKFo2SAzLWdoSVBpNnJleWp6cEZ0cW1IeFZJbU9ZTTFJS2FaRKFupWxvZ2luo3RpZNkgR3hJZ3loYmdiazN3a2hHeWNqU0RnR2p6dU5QWjk0RGOjY2lk2SB5R0JWZ2U2Nks1TkpwU041dTcxZlU5MFZjVGxFQVNOdQ&client=yGBVge66K5NJpSN5u71fU90VcTlEASNu&protocol=oauth2&redirect_uri=https%3A%2F%2Fwww.seek.com.au%2Foauth%2Fcallback%2F&scope=openid%20profile%20email%20offline_access&audience=https%3A%2F%2Fseek%2Fapi%2Fcandidate&fragment=%2Foauth%2Flogin%3Flocale%3Dau%26language%3Den%26realm%3DUsername-Password-Authentication%26da_cdt%3Dvisid_01931366de6c000523dae529aa3305075003906d00942-sesid_1731197329007-hbvid_81b41409_b72c_4aed_a211_9c0183ec5bf1-tempAcqSessionId_1731197329009-tempAcqVisitorId_81b41409b72c4aeda2119c0183ec5bf1&ui_locales=en&JobseekerSessionId=cf618dba-afe0-4ff5-8d44-7a8c9be7a72d&language=en-AU&response_type=code&response_mode=query&nonce=c2NVQkxQbjl6MzA1VC5TUzZhUFYwdnNFN1pjU1JEZkhVZGNrOXVTcS5xRw%3D%3D&code_challenge=izRMkFftM_hVrAUkIceIiJCaIVHj6P-eFBUXstHI_d4&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtc3BhLWpzIiwidmVyc2lvbiI6IjEuMjIuMyJ9#/login?locale=au&language=en&realm=Username-Password-Authentication&da_cdt=visid_01931366de6c000523dae529aa3305075003906d00942-sesid_1731197329007-hbvid_81b41409_b72c_4aed_a211_9c0183ec5bf1-tempAcqSessionId_1731197329009-tempAcqVisitorId_81b41409b72c4aeda2119c0183ec5bf1')  # URL completo
        self.driver.maximize_window()
        press = input("PRESS ENTER WHEN YOU LOG IN..!!")
        logger.info(f'NOW I’LL START WORKING FOR YOU. {press}')

        sleep(5)
        
        self.wait_time_out = 15
        self.wait_variable = W(self.driver, self.wait_time_out)
        logger.info("Login completed and browser maximized!")
        
    def search_jobs(self):
        self.wait_time_out = 15
        self.wait_variable = W(self.driver, self.wait_time_out)
        try:
            keyword = self.driver.find_element("xpath","//input[@id='keywords-input']" )
            keyword.send_keys(work)
            sleep(2)
            pyautogui.press('enter')
            sleep(2)
        except:
            pass
        try:    
            location_field = self.driver.find_element("xpath","/html/body/div[1]/div/div[3]/div/div/div/div/div/div/section/div[2]/form/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/input" )
            location_field.clear() 
            location_field.send_keys(location_user)
            logger.info("LOCATION IS GOING GOOD")
            sleep(2)
        except Exception as e:
            logger.critical(f"we got an error here: {e}")
        
        #touch seek button
        
        seek = self.driver.find_element("xpath","//button[@id='searchButton']" )
        seek.click()
        logger.info("we find your element")
        sleep(2)
        
        
    def scraper_job(self):
        self.rows = []
        for i in range (1,7):#23
            
            try:
                jobs = self.driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div/section/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div[3]/div["+str(i)+"]/article/div[2]/a")
                jobs.click()
                sleep(2)
                
                try:
                    status = self.driver.find_element("xpath","/html/body/div[1]/div/div[3]/div/section/div[2]/div/div/div[1]/div/div/div[2]/div/div/div[3]/div/div/div[2]/div[2]/div/div[1]/div[4]/div/div/div/div[1]/div/div/div/span/span/span[2]")
                    status_text = status.text
                except:
                    pass
                try:
                    if "You applied" in status_text:
                        logger.info(f"Skipping job {i} because status is: {status_text}")
                        continue

                except:
                    pass
                

                jobs_href = jobs.get_attribute("href")
                self.rows.append(jobs_href)
                sleep(2)
                logger.debug(self.rows)
                

            except Exception as e:
                logger.critical(f"Error while processing job {i}: {e}")                        
        else:
                pass
            
            
    def enter_application_jobs(self):
        for row in self.rows:
            self.driver.get(row)
            sleep(5)
            
            try:
                self.about_job = self.driver.find_element("xpath","/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div/div[2]/section[1]/div/div/div")
                #self.about_job = self.driver.find_element("xpath","//div[contains(@class, '_47fs8z0') and contains(@class, '_30qf0g0')]")
                self.about_job_text = self.about_job.text

                logger.info('we find your element')
            except:
                logger.critical(' you are doing something wrong fix your code now!!!!')
                pass    
            
            try:
            # Wait for all "job-detail-apply" buttons to be present
                buttons = W(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//a[@data-automation='job-detail-apply']")))
    
                for button in buttons:
                    # Check the text content of each button
                    if "Quick apply" in button.text:
                    # Scroll into view and click the correct button
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                        button.click()
                        logger.info("Quick Apply button clicked successfully!")
                        sleep(5)
                    else:  print("No 'Quick Apply' button found.")
                        # Exit after clicking the correct button
                   
            except Exception as e:
                logger.info(f"Could not find or click the Quick Apply button: {e}")
                sleep(2)
                pass

             #------------------ add function apply_jobs----------------------#   
            BrowserAutomation.apply_jobs(self)          
            #------------------end of the function---------------------------# 

    def apply_jobs(self):
        
        try:
            resume = self.driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div/div/div[3]/div[2]/div[2]/fieldset/div/div/div/div[2]/div/input")
            resume.click()
            sleep(2)
            cover_letter = self.driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div/div[3]/div[2]/div[3]/fieldset/div/div/div/div[2]/div/input")
            cover_letter.click()
            sleep(2)
            
            cover_letter_text = self.driver.find_element("id","coverLetter-text-:r6:-description")
            cover_letter_text_job = cover_letter_text.text
            #cover_letter_text_get =cover_letter_text.get_attribute("text")
            
            message = f"Write a cover letter for this job base on my cv just start with dear manager it have to be simple, and also put my name at the end Patrich Bravo, dont pu anything in []. about the job: {self.about_job_text} they ask: {cover_letter_text_job} and this is my cv: {cv}" 
            logger.debug(message)
            
            self.message_chat = ChatGPTBot(api_key=api_key)

            response = self.message_chat.send_message(message=message)
            
            cover_letter_dialog = self.driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div/div[3]/div[2]/div[3]/fieldset/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/textarea")
            cover_letter_dialog.click()
            cover_letter_dialog.clear()
            
            sleep(3)
            cover_letter_dialog.send_keys(response)
            
            sleep(5)
        except Exception as e:
            logger.critical(f"Error while processing job: {e}")
            pass
        try:
            press_continue = self.driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div/div[3]/div[2]/div[4]/div/button")
            press_continue.click()
        except:
            logger.critical("i coulnd't find it")
            pass

        sleep(3)
#------------------------question and answers-------------------------- 
        try:
            questions_and_answer(self)
            sleep(5)
        except:
            pass
#------------------------END QUESTION AND ANSWERS-----------------------

#---------------CONTINUES BUTTONS---------------------------------
        xpaths = ["/html/body/div/div/div[1]/div/div/div[3]/div/form/div/div/div[1]/button",
                "/html/body/div[1]/div/div[1]/div/div/div[3]/div/form/div/div[6]/div[1]/button",
    "/html/body/div[1]/div/div[1]/div/div/div[3]/div/div[6]/div[1]/button",
    '//*[@id="app"]/div/div[1]/div/div/div[3]/div/div[5]/div/button',
    '/html/body/div[1]/div/div[1]/div/div/div[3]/div/div[5]/div/button',
    '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[4]/div[1]/button[1]']
        

        for i, xpath_1 in enumerate(xpaths, start=1):
            try:
                find_xpth = self.driver.find_element(By.XPATH,xpath_1)
                BrowserAutomation.scroll_down(driver=self.driver, scroll_by=500, max_attempts=20, button_xpath=xpath_1)
                sleep(5)
                #if find_xpth == True:             
                #    BrowserAutomation.scroll_down(driver=self.driver, scroll_by=500, max_attempts=20, button_xpath=xpath_1)
                #    sleep(5)
                #print(f"we could, find {xpath_1}, Number{i}")
            except Exception as e:
                logger.critical(f"Error with button {i}: {e}")
                pass
        
 #-----------------------------------END CONTINUES BUTTONS--------------------------------------
    def scroll_down(driver, scroll_by=500, max_attempts=20, button_xpath="//button[@data-testid='continue-button']"):

        for attempt in range(max_attempts):
            try:
                # Locate the button by XPath
                button = driver.find_element(By.XPATH, button_xpath)
                logger.debug(f"Button found after {attempt} scroll attempts!")
                
                # Scroll to the button
                driver.execute_script("arguments[0].scrollIntoView(true);", button)
                
                # Click the button
                button.click()
                logger.debug("Button clicked successfully!")
                return True
            except Exception as e:
                # If button not found, scroll down by the specified pixels
                driver.execute_script(f"window.scrollBy(0, {scroll_by});")
                logger.debug(f"Scrolled {scroll_by} pixels. Attempt {attempt + 1}/{max_attempts}")
        logger.debug("Button not found after maximum scroll attempts.")
        
               
class ChatGPTBot(BrowserAutomation):
    def __init__(self, api_key):
        super().__init__() 
        openai.api_key = api_key
        self.chat_history = []

    def send_message(self, message):

        """Send the message to ChatGPT and return the response."""
        self.chat_history.append(f"Tú: {message}")
        logger.debug(f"Sending message: {message}")

        try:
            # Correct usage of the OpenAI API for chat completion
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert in recruiting and talent acquisition."},
                    {"role": "user", "content": message}
                ]
            )

            # Extract the content of the first choice
            reply = response["choices"][0]["message"]["content"]
            self.chat_history.append(f"ChatGPT: {reply}")
            logger.debug(f"We got your answer: {reply}")
            return reply

        except openai.OpenAIError as e:
            # Handle OpenAI-specific exceptions
            logger.critical(f"An error occurred with OpenAI: {e}")
            self.chat_history.append(f"Error: Unable to process the request. Reason: {e}")
            return "An error occurred while processing your request."

        except Exception as e:
            # Catch unexpected errors
            logger.critical(f"Unexpected error: {e}")
            self.chat_history.append("An unexpected error occurred.")
            return "An unexpected error occurred."

    def show_history(self):
        """show the chat history."""
        logger.debug("\nChat history:")
        for line in self.chat_history:
            logger.debug(line)
        


if __name__ == "__main__":
 
    logger.debug('hello')
    press = input("PRESS ENTER WHEN YOU LOG IN..!!")
    logger.info(f'NOW I’LL START WORKING FOR YOU. {press}')