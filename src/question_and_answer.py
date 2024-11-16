from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from time import sleep

def questions_and_answer(self):
    try:
        #Which of the following statements best describes your right to work in Australia?
        rights = self.driver.find_element(By.ID, "question-AU_Q_6_V_9")
        #rights.click()
        print() 
        rights_to_work = Select(rights)
        rights_to_work.select_by_value("AU_Q_6_V_9_A_14978")#Require sponsorship or by visible text
        sleep(1)
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
    
    try:
        #How many years' experience do you have as a data analyst?
        
        data_analyst_exp = self.driver.find_element(By.ID, "question-AU_Q_6048_V_4") 
        data_analyst_exp = Select(rights)
        data_analyst_exp.select_by_value("AU_Q_6048_V_4_A_6054")
        sleep(1)
        
        #AU_Q_6048_V_4_A_6049	No experience
        #AU_Q_6048_V_4_A_6050	Less than 1 year
        #AU_Q_6048_V_4_A_6051	1 year
        #AU_Q_6048_V_4_A_6052	2 years
        #AU_Q_6048_V_4_A_6053	3 years
        #AU_Q_6048_V_4_A_6054	4 years
        #AU_Q_6048_V_4_A_6055	5 years
        #AU_Q_6048_V_4_A_6056	More than 5 years
    except:
        pass
    try:
        #Do you have experience working on data migration projects?
        #yes
        data_mig_exp = self.driver.find_element(By.ID, "question-AU_Q_970_V_2_0") 
        #question-AU_Q_970_V_2_0	Yes
        #question-AU_Q_970_V_2_1	No
        data_mig_exp.click()
        sleep(1)
    except:
        pass
    try:
        #Do you hold Australian Security Clearance?
        #no
        aus_seg_clearance = self.driver.find_element(By.ID, "question-AU_Q_176_V_4_4")
        aus_seg_clearance.click()
        #question-AU_Q_176_V_4_0	Yes, Baseline
        #question-AU_Q_176_V_4_1	Yes, NVL1
        #question-AU_Q_176_V_4_2	Yes, NVL2
        #question-AU_Q_176_V_4_3	Yes, TSPV
        #question-AU_Q_176_V_4_4	No
        sleep(1)
    except:
        pass
    try:
        #How many years' experience do you have using SQL queries?
        sql_exp = self.driver.find_element(By.ID, "question-AU_Q_221_V_2") 
        sql_exp = Select(rights)
        sql_exp.select_by_value("AU_Q_221_V_2_A_23228")
        
        #AU_Q_221_V_2_A_23224	No experience
        #AU_Q_221_V_2_A_23225	Less than 1 year
        #AU_Q_221_V_2_A_23226	1 year
        #AU_Q_221_V_2_A_23227	2 years
        #AU_Q_221_V_2_A_23228	3 years
        #AU_Q_221_V_2_A_23229	4 years
        #AU_Q_221_V_2_A_23230	5 years
        #AU_Q_221_V_2_A_23231	More than 5 years
        sleep(1)
    except:
        pass
    try:
        #Do you have strong Tableau experience?

        #yes
        tableau_exp = self.driver.find_element(By.ID, "question-indirect_4ad8449d-0db6-432c-a34e-d0695bd98627_4089e634-86be-42be-b847-3bcbf7b500a6_0") 
        #no
        #data_mig_exp = self.driver.find_element(By.ID, "question-indirect_4ad8449d-0db6-432c-a34e-d0695bd98627_4089e634-86be-42be-b847-3bcbf7b500a6_1") 
        tableau_exp.click()
        sleep(1)
    except:
        pass
    try:
        
        #Can you start a new role within 2 weeks?
        start_2_weeks = self.driver.find_element(By.ID, "question-indirect_4ad8449d-0db6-432c-a34e-d0695bd98627_bb22e15e-af85-486a-a898-e76706528c3e_0") 
        start_2_weeks.click()
        sleep(1)

        #question-indirect_4ad8449d-0db6-432c-a34e-d0695bd98627_bb22e15e-af85-486a-a898-e76706528c3e_0	Yes
        #question-indirect_4ad8449d-0db6-432c-a34e-d0695bd98627_bb22e15e-af85-486a-a898-e76706528c3e_1	No
        
    except:
        pass
    