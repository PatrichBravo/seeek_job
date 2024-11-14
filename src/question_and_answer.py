from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from class_1 import BrowserAutomation

def questions_and_answer(self):
    try:
        #Which of the following statements best describes your right to work in Australia?
        rights = self.driver.find_element(By.ID, "question-AU_Q_6_V_9") 
        rights_to_work = Select(rights)
        rights_to_work.select_by_value("AU_Q_6_V_9_A_14978")#Require sponsorship or by visible text
        #---------------Codes---------------------------------        
        #AU_Q_6_V_9_A_14970	I'm an Australian citizen
        #AU_Q_6_V_9_A_14971	I'm a permanent resident and/or NZ citizen
        #AU_Q_6_V_9_A_14972	I have a family/partner visa with no restrictions
        #AU_Q_6_V_9_A_14973	I have a graduate temporary work visa
        #AU_Q_6_V_9_A_14974	I have a holiday temporary work visa
        #AU_Q_6_V_9_A_14975	I have a temporary visa with restrictions on work location (e.g. skilled regional visa 491)
        #AU_Q_6_V_9_A_14976	I have a temporary protection or safe haven enterprise work visa
        #AU_Q_6_V_9_A_28629	I have a temporary visa with no restrictions (e.g. doctoral student)
        #AU_Q_6_V_9_A_14977	I have a temporary visa with restrictions on work hours (e.g. student visa, retirement visa)
        #AU_Q_6_V_9_A_29143	I have a temporary visa with restrictions on industry (e.g. temporary activity visa 408)
        #AU_Q_6_V_9_A_14978	I require sponsorship to work for a new employer (e.g. 482, 457)
    except:
        pass
    
    
    #How many years' experience do you have as a data analyst?
    
    data_analyst_exp = self.driver.find_element(By.ID, "question-AU_Q_6048_V_4") 
    data_analyst_exp = Select(rights)
    data_analyst_exp.select_by_value("AU_Q_6048_V_4_A_6054")
    
    #AU_Q_6048_V_4_A_6049	No experience
    #AU_Q_6048_V_4_A_6050	Less than 1 year
    #AU_Q_6048_V_4_A_6051	1 year
    #AU_Q_6048_V_4_A_6052	2 years
    #AU_Q_6048_V_4_A_6053	3 years
    #AU_Q_6048_V_4_A_6054	4 years
    #AU_Q_6048_V_4_A_6055	5 years
    #AU_Q_6048_V_4_A_6056	More than 5 years
    
    #Do you have experience working on data migration projects?
    #yes
    data_mig_exp = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[3]/div/form/div/fieldset[1]/div/div/div/div[1]/div/input") 
    #no
    #data_mig_exp = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[3]/div/form/div/fieldset[1]/div/div/div/div[2]/div/input") 
    data_mig_exp.click()