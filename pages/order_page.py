import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    @allure.step('Ожидаем формы для оформления заказа')
    def loading_page_order(self):
        self.waiting_loading_page(OrderPageLocators.FIELD_NAME_XPATH)
    @allure.step('Вводим Имя')
    def set_name(self,name):
        self.send_keys_in_field(OrderPageLocators.FIELD_NAME_XPATH,name)

    @allure.step('Вводим фамилию')
    def set_last_name(self,last_name):
        self.send_keys_in_field(OrderPageLocators.FIELD_FAMILY_XPATH,last_name)

    @allure.step('Вводим Адрес')
    def set_address(self,address):
        self.send_keys_in_field(OrderPageLocators.FIELD_ADDRESS_XPATH,address)

    @allure.step('Выбираем странцию метро')
    def click_metro_station(self):
        self.click_element(OrderPageLocators.FIELD_METRO_XPATH)
        self.waiting_loading_page(OrderPageLocators.DROPDOWN_METRO_XPATH)
        self.click_element(OrderPageLocators.DROPDOWN_METRO_XPATH)

    @allure.step('Вводим телефон')
    def set_phone(self,phone):
        self.send_keys_in_field(OrderPageLocators.FIELD_PHONE_NUMBER_XPATH,phone)

    @allure.step('Нажимаем кнопку далее')
    def click_button_next(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON_XPATH)

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
        assert 'Про аренду' == self.text_element(OrderPageLocators.TEXT_ABOUT_RENT_XPATH)

    @allure.step('Выбираем когда привезти самокат')
    def set_data(self):
        self.click_element(OrderPageLocators.FIELD_WHEN_BRING_SCOOTER_XPATH)
        self.click_element(OrderPageLocators.DATA_FOR_ORDER_XPATH)

    @allure.step('Выбираем срок аренды')
    def set_rental_period(self):
        self.click_element(OrderPageLocators.FIELD_RENTAL_PERIOD_XPATH)
        self.waiting_loading_page(OrderPageLocators.DROPDOWN_RENTAL_PERIOD_XPATH)
        self.click_element(OrderPageLocators.DROPDOWN_RENTAL_PERIOD_XPATH)

    @allure.step('Выбираем чек-бокс цвет самоката')
    def set_checkbox_color_scooter(self):
        self.click_element(OrderPageLocators.CHECKBOX_COLOR_SCOOTER_XPATH)

    @allure.step('Вводим комментарий для курьера')
    def set_comment(self,comment):
        self.send_keys_in_field(OrderPageLocators.FIELD_COMMENT_FOR_COURIER_XPATH,comment)

    @allure.step('Нажимаем кнопку заказать')
    def click_order_scooter(self):
        self.click_element(OrderPageLocators.BUTTON_ORDER_XPATH)


    @allure.step('Подтверждаем оформление заказа')
    def click_yes_for_popup_do_you_want_place_order(self):
        self.waiting_loading_page(OrderPageLocators.BUTTON_YES_FOR_POPUP_XPATH)
        self.click_element(OrderPageLocators.BUTTON_YES_FOR_POPUP_XPATH)

    @allure.step('Нажимаем на кнопку посмотреть статус')
    def click_watch_status(self):
        self.click_element(OrderPageLocators.BUTTON_WATCH_STATUS_XPATH)

    @allure.step('Получаем текст с фронта о отмене заказа')
    def get_text_for_front(self,locator):
        return self.text_element(*locator)

    @allure.step('Сравниваем текст с тем что на фронте')
    def assert_succes_create_order(self, text_for_popup):
        assert text_for_popup == self.get_text_for_front(OrderPageLocators.BUTTON_ORDER_CANCEL_XPATH)

    @allure.step('Ожидаем пока загрузиться поле имя')
    def waiting_loading_field_name(self):
        self.waiting_loading_page(OrderPageLocators.FIELD_NAME_XPATH)


    def set_abonent_data_step2(self,comment):
        self.set_data()
        self.set_rental_period()
        self.set_checkbox_color_scooter()
        self.set_comment(comment)
        self.click_order_scooter()
        self.click_yes_for_popup_do_you_want_place_order()
        self.waiting_loading_page(OrderPageLocators.ORDER_REGISTER_XPATH)
        self.waiting_loading_page(OrderPageLocators.BUTTON_WATCH_STATUS_XPATH)
        self.click_watch_status()
        self.waiting_loading_page(OrderPageLocators.BUTTON_ORDER_CANCEL_XPATH)
