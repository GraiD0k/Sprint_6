
import allure
import time
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class OrderPage(BasePage):
    @allure.step('Нажимаем на кнопку Заказать')
    def click_button_order(self):
        self.waiting_loading_page(MainPageLocators.ORDER_BUTTON_XPATH)
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_XPATH).click()
        self.waiting_loading_page(OrderPageLocators.FIELD_NAME_XPATH)
    @allure.step('Вводим Имя')
    def set_name(self,name):
        self.driver.find_element(*OrderPageLocators.FIELD_NAME_XPATH).send_keys(name)

    @allure.step('Вводим фамилию')
    def set_last_name(self,last_name):
        self.driver.find_element(*OrderPageLocators.FIELD_FAMILY_XPATH).send_keys(last_name)

    @allure.step('Вводим Адрес')
    def set_address(self,address):
        self.driver.find_element(*OrderPageLocators.FIELD_ADDRESS_XPATH).send_keys(address)

    @allure.step('Выбираем странцию метро')
    def click_metro_station(self):
        self.driver.find_element(*OrderPageLocators.FIELD_METRO_XPATH).click()
        self.waiting_loading_page(OrderPageLocators.DROPDOWN_METRO_XPATH)
        self.driver.find_element(*OrderPageLocators.DROPDOWN_METRO_XPATH).click()

    @allure.step('Вводим телефон')
    def set_phone(self,phone):
        self.driver.find_element(*OrderPageLocators.FIELD_PHONE_NUMBER_XPATH).send_keys(phone)

    @allure.step('Нажимаем кнопку далее')
    def click_button_next(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON_XPATH).click()

    def set_abonent_data_step1(self,name,last_name,address,phone):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.click_metro_station()
        self.set_phone(phone)
        self.click_button_next()
        self.waiting_loading_page(OrderPageLocators.TEXT_ABOUT_RENT_XPATH)

    @allure.step('Проверка, что перешли на второй шаг заказа')
    def assert_go_next_step(self):
        assert 'Про аренду' == self.driver.find_element(*OrderPageLocators.TEXT_ABOUT_RENT_XPATH).text

    @allure.step('Выбираем когда привезти самокат')
    def set_data(self):
        self.driver.find_element(*OrderPageLocators.FIELD_WHEN_BRING_SCOOTER_XPATH).click()
        self.driver.find_element(*OrderPageLocators.DATA_FOR_ORDER_XPATH).click()

    @allure.step('Выбираем срок аренды')
    def set_rental_period(self):
        self.driver.find_element(*OrderPageLocators.FIELD_RENTAL_PERIOD_XPATH).click()
        self.waiting_loading_page(OrderPageLocators.DROPDOWN_RENTAL_PERIOD_XPATH)
        self.driver.find_element(*OrderPageLocators.DROPDOWN_RENTAL_PERIOD_XPATH).click()

    @allure.step('Выбираем чек-бокс цвет самоката')
    def set_checkbox_color_scooter(self):
        self.driver.find_element(*OrderPageLocators.CHECKBOX_COLOR_SCOOTER_XPATH).click()

    @allure.step('Вводим комментарий для курьера')
    def set_comment(self,comment):
        self.driver.find_element(*OrderPageLocators.FIELD_COMMENT_FOR_COURIER_XPATH).send_keys(comment)

    @allure.step('Нажимаем кнопку заказать')
    def click_order_scooter(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_ORDER_XPATH).click()


    @allure.step('Подтверждаем оформление заказа')
    def click_yes_for_popup_do_you_want_place_order(self):
        self.waiting_loading_page(OrderPageLocators.BUTTON_YES_FOR_POPUP_XPATH)
        self.driver.find_element(*OrderPageLocators.BUTTON_YES_FOR_POPUP_XPATH).click()

    @allure.step('Нажимаем на кнопку посмотреть статус')
    def click_watch_status(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_WATCH_STATUS_XPATH).click()

    @allure.step('Получаем текст с фронта о отмене заказа')
    def get_text_for_front(self,locator):
        return self.driver.find_element(*locator).text

    @allure.step('Сравниваем текст с тем что на фронте')
    def assert_succes_create_order(self, text_for_popup):
        assert text_for_popup == self.get_text_for_front(OrderPageLocators.BUTTON_ORDER_CANCEL_XPATH)

    def set_abonent_data_step2(self,comment):
        self.set_data()
        self.set_rental_period()
        self.set_checkbox_color_scooter()
        self.set_comment(comment)
        self.click_order_scooter()
        self.click_yes_for_popup_do_you_want_place_order()
        time.sleep(5)
        self.waiting_loading_page(OrderPageLocators.BUTTON_WATCH_STATUS_XPATH)
        self.click_watch_status()
        self.waiting_loading_page(OrderPageLocators.BUTTON_ORDER_CANCEL_XPATH)