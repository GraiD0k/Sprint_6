from selenium.webdriver.common.by import By

class OrderPageLocators:
    FIELD_NAME_XPATH = (By.XPATH,'//input[@placeholder="* Имя"]')#Локатор имени
    FIELD_FAMILY_XPATH = (By.XPATH,'//input[@placeholder="* Фамилия"]')# Фамилия
    FIELD_ADDRESS_XPATH = (By.XPATH,'//input[@placeholder="* Адрес: куда привезти заказ"]')# Адрес для заказа
    FIELD_METRO_XPATH = (By.XPATH,'//input[@placeholder="* Станция метро"]')# выбор станции метро
    FIELD_PHONE_NUMBER_XPATH = (By.XPATH,'//input[@placeholder="* Телефон: на него позвонит курьер"]')#
    DROPDOWN_METRO_XPATH = [By.XPATH, "(//div[text()='Бульвар Рокоссовского'])[1]"]  # Метро из выпадающего списка
    NEXT_BUTTON_XPATH = (By.XPATH,'//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    TEXT_ABOUT_RENT_XPATH = (By.CLASS_NAME, "Order_Header__BZXOb")  # Текст о аренде
    FIELD_WHEN_BRING_SCOOTER_XPATH = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # Календарь
    DATA_FOR_ORDER_XPATH = (By.XPATH, "//div[@aria-label='Choose понедельник, 27-е января 2025 г.']")  # Выбор даты
    FIELD_RENTAL_PERIOD_XPATH = (By.CLASS_NAME, "Dropdown-placeholder")  # Выпающий список с длительностью аренды
    DROPDOWN_RENTAL_PERIOD_XPATH = (By.XPATH, "//div[text()='четверо суток']")  # Количество дней из выпадающего списка
    CHECKBOX_COLOR_SCOOTER_XPATH = (By.ID, 'black')  # Чекбокс цвет самоката
    FIELD_COMMENT_FOR_COURIER_XPATH = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")  # Комментарий для курьера
    BUTTON_ORDER_XPATH = (By.XPATH,"//div[@class='Order_Buttons__1xGrp']/child::button[text()='Заказать']")  # Кнопка Заказать
    BUTTON_YES_FOR_POPUP_XPATH = (By.XPATH, "//button[text()='Да']")  # Подтверждаем заказ
    ORDER_REGISTER_XPATH= (By.XPATH,'//div[@class="Order_Text__2broi"]')
    BUTTON_WATCH_STATUS_XPATH = (By.XPATH, '//button[text()="Посмотреть статус"]')  # Кнопка посмотреть статус
    BUTTON_ORDER_CANCEL_XPATH = (By.XPATH, '//div[contains(@class, "Track_OrderInfo")]/button')  # Кнопка Отменить заказ