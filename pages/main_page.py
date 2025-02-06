import allure
from conftest import driver
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Нажатие на вопрос')
    def click_question(self,xpath):
        self.driver.find_element(*xpath).click()
    @allure.step('Получение ответа на вопрос')
    def receiving_text_answer (self,xpath_text_):
        return self.driver.find_element(*xpath_text_).text
    @allure.step('Сравниваем ответ на вопрос')
    def check_text_answers(self, xpath ,xpath_text,answer_text):
        self.waiting_loading_page(xpath)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.waiting_loading_page(xpath)
        self.click_question(xpath)
        assert self.receiving_text_answer(xpath_text) == answer_text