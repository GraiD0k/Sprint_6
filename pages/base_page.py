import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем пока загрузиться элемент')
    def waiting_loading_page(self,xpath):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(xpath))

    @allure.step('Переключение на новую вкладку')
    def switch_to_new_tab(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    @allure.step('Проверка адреса страницы')
    def assert_current_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))
        assert self.driver.current_url == url

    @allure.step('Нажимаем кнопку заказать')
    def click_button_order(self):
        self.waiting_loading_page(MainPageLocators.ORDER_BUTTON_XPATH)
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_XPATH).click()
    @allure.step('Нажимаем на элемент ')
    def click_element(self,xpath):
        self.driver.find_element(*xpath).click()

    @allure.step('Получаем текст элемента')
    def text_element(self , xpath_text_):
        return self.driver.find_element(*xpath_text_).text
    @allure.step('Промотать страницу')
    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step('Заполняем поле данными')
    def send_keys_in_field(self,xpath,text):
        self.driver.find_element(*xpath).send_keys(text)

    def create_driver(self,url):
        self.driver.get(url)