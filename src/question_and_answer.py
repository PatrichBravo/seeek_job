def questions_and_answer(self):
    #Which of the following statements best describes your right to work in Australia?
        rights = self.driver.find_element(By.ID, "question-AU_Q_6_V_9") 
        rights_to_work = Select(rights)
        rights_to_work.select_by_value("AU_Q_6_V_9_A_14978")#Require sponsorship or by visible text