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
    try:
        #How many years' experience do you have as a Business Intelligence Analytics Consultant?
        bus_int_exp = self.driver.find_element(By.ID, "question-AU_Q_63C65D2B02CF667945308F559E1FCB5A_V") 
        bus_int_exp = Select(rights)
        bus_int_exp.select_by_value("AU_Q_63C65D2B02CF667945308F559E1FCB5A_V_1_A_63C65D2B02CF667945308F559E1FCB5A_3")
        
        #Option Text: No experience
        #Option ID: AU_Q_63C65D2B02CF667945308F559E1FCB5A_V_1_A_63C65D2B02CF667945308F559E1FCB5A_1
        #Option Text: Less than 1 year
        #Option ID: AU_Q_63C65D2B02CF667945308F559E1FCB5A_V_1_A_63C65D2B02CF667945308F559E1FCB5A_2
        #Option Text: 1 year
        #Option ID: AU_Q_63C65D2B02CF667945308F559E1FCB5A_V_1_A_63C65D2B02CF667945308F559E1FCB5A_3
        #Option Text: 2 years
        #Option ID: AU_Q_63C65D2B02CF667945308F559E1FCB5A_V_1_A_63C65D2B02CF667945308F559E1FCB5A_4
        #Option Text: 3 years
        #Option ID: AU_Q_63C65D2B02CF667945308F559E1FCB5A_V_1_A_63C65D2B02CF667945308F559E1FCB5A_5
        #Option Text: 4 years
        #Option ID: AU_Q_63C65D2B02CF667945308F559E1FCB5A_V_1_A_63C65D2B02CF667945308F559E1FCB5A_6
        #Option Text: 5 years
        #Option ID: AU_Q_63C65D2B02CF667945308F559E1FCB5A_V_1_A_63C65D2B02CF667945308F559E1FCB5A_7
        #Option Text: More than 5 years
        #Option ID: AU_Q_63C65D2B02CF667945308F559E1FCB5A_V_1_A_63C65D2B02CF667945308F559E1FCB5A_8
    except:
        pass
    try:
        real_int_exp = self.driver.find_element(By.ID, "question-AU_Q_1113_V_2") 
        real_int_exp = Select(rights)
        real_int_exp.select_by_value("AU_Q_1113_V_2_A_20932")
        #Option Text: No experience
        #Option ID: AU_Q_1113_V_2_A_20931
        #Option Text: Less than 1 year
        #Option ID: AU_Q_1113_V_2_A_20932
        #Option Text: 1 year
        #Option ID: AU_Q_1113_V_2_A_20933
        #Option Text: 2 years
        #Option ID: AU_Q_1113_V_2_A_20934
        #Option Text: 3 years
        #Option ID: AU_Q_1113_V_2_A_20935
        #Option Text: 4 years
        #Option ID: AU_Q_1113_V_2_A_20936
        #Option Text: 5 years
        #Option ID: AU_Q_1113_V_2_A_20937
        #Option Text: More than 5 years
        #Option ID: AU_Q_1113_V_2_A_20938
    except:
        pass
    
    try:
        #How would you rate your English language skills?
        english_exp = self.driver.find_element(By.XPATH, '//*[@id="question-AU_Q_122_V_2_1"]') 
        english_exp.click()
        #Limited proficiency
        #//*[@id="question-AU_Q_122_V_2_0"]
        #Professional working proficiency
        #//*[@id="question-AU_Q_122_V_2_1"]
        #Native or Bilingual proficiency
        #//*[@id="question-AU_Q_122_V_2_2"]
        
    except:
        pass
        
    try:
        #Have you completed a qualification in mathematics / mathematical science?
        completed_math = self.driver.find_element(By.ID, "AU_Q_1080_V_3") 
        completed_math = Select(rights)
        completed_math.select_by_value("AU_Q_1080_V_3_A_26973")
        
        #AU_Q_1080_V_3_A_26978	Yes, Diploma
        #AU_Q_1080_V_3_A_26977	Yes, Associate Degree
        #AU_Q_1080_V_3_A_26979	Yes, Bachelor Degree
        #AU_Q_1080_V_3_A_26980	Yes, Bachelor Degree (Honours)
        #AU_Q_1080_V_3_A_26971	Yes, Graduate Certificate
        #AU_Q_1080_V_3_A_26972	Yes, Graduate Diploma
        #AU_Q_1080_V_3_A_26970	Yes, Masters Degree
        #AU_Q_1080_V_3_A_26974	Yes, Doctoral Degree
        #AU_Q_1080_V_3_A_26973	I have a qualification in mathematics which isn't listed
        #AU_Q_1080_V_3_A_26975	I don't have a qualification in mathematics
        
    except:
        pass
    
    try:
        #Have you completed a qualification in science?
        completed_sience = self.driver.find_element(By.ID, "AU_Q_1078_V_2") 
        completed_sience = Select(rights)
        completed_sience.select_by_value("AU_Q_1078_V_2_A_27078")
        
        #AU_Q_1078_V_2_A_27068	Yes, Diploma
        #AU_Q_1078_V_2_A_27069	Yes, Advanced Diploma
        #AU_Q_1078_V_2_A_27070	Yes, Associate Degree
        #AU_Q_1078_V_2_A_27071	Yes, Bachelor Degree
        #AU_Q_1078_V_2_A_27072	Yes, Bachelor Degree (Honours)
        #AU_Q_1078_V_2_A_27074	Yes, Graduate Certificate
        #AU_Q_1078_V_2_A_27075	Yes, Graduate Diploma
        #AU_Q_1078_V_2_A_27073	Yes, Masters Degree
        #AU_Q_1078_V_2_A_27077	Yes, Doctoral Degree
        #AU_Q_1078_V_2_A_27076	I have a qualification in science which isn't listed
        #AU_Q_1078_V_2_A_27078	I don't have a qualification in science
        
    except:
        pass
        
        