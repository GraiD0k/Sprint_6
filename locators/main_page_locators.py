from selenium.webdriver.common.by import By

class MainPageLocators:
    FIRST_QUESTION_XPATH = (By.XPATH,'//div[@class="accordion__item"][1]')
    FIRST_ANSWER_XPATH = (By.XPATH,'//div [@aria-labelledby="accordion__heading-0"]/p')
    SECOND_QUESTION_XPATH = (By.XPATH,'//div[@class="accordion__item"][2]')
    SECOND_ANSWER_XPATH = (By.XPATH,'//div [@aria-labelledby="accordion__heading-1"]/p')
    THIRD_QUESTION_XPATH = (By.XPATH,'//div[@class="accordion__item"][3]')
    THIRD_ANSWER_XPATH = (By.XPATH,'//div [@aria-labelledby="accordion__heading-2"]/p')
    FOURTH_QUESTION_XPATH = (By.XPATH,'//div[@class="accordion__item"][4]')
    FOURTH_ANSWER_XPATH = (By.XPATH,'//div [@aria-labelledby="accordion__heading-3"]/p')
    FIFTH_QUESTION_XPATH = (By.XPATH,'//div[@class="accordion__item"][5]')
    FIFTH_ANSWER_XPATH = (By.XPATH,'//div [@aria-labelledby="accordion__heading-4"]/p')
    SIXTH_QUESTION_XPATH = (By.XPATH,'//div[@class="accordion__item"][6]')
    SIXTH_ANSWER_XPATH = (By.XPATH,'//div [@aria-labelledby="accordion__heading-5"]/p')
    SEVENTH_QUESTION_XPATH = (By.XPATH,'//div[@class="accordion__item"][7]')
    SEVENTH_ANSWER_XPATH = (By.XPATH,'//div [@aria-labelledby="accordion__heading-6"]/p')
    EIGHTH_QUESTION_XPATH = (By.XPATH,'//div[@class="accordion__item"][8]')
    EIGHTH_ANSWER_XPATH = (By.XPATH,'//div [@aria-labelledby="accordion__heading-7"]/p')
    ORDER_BUTTON_XPATH = (By.XPATH,'//button [@class="Button_Button__ra12g"]')
    LOGO_SCOOTER_XPATH = [By.XPATH, '//a[contains(@class, "Header_LogoScooter")]']
    LOGO_YANDEX_XPATH = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
