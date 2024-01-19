from selenium import webdriver
from selenium.webdriver.common.by import By


# Нажать на кнопку с наградами
def is_click_price(driver):
    button_price = driver.find_element(by=By.XPATH,
                                       value='//*[@id="live-page-chat"]/div/div/div[2]/div/div/section/div/div[6]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/button/div/div/div/div[1]/div/img')
    button_price.click()


# Нажать на кнопку с музыкой
def is_click_music(driver):
    button_music = driver.find_element(by=By.XPATH,
                                       value='//*[@id="channel-points-reward-center-body"]/div/div/div[7]/div/button')
    button_music.click()


# Вписать музыку
def is_get_link_music(driver):
    area_music = driver.find_element(by=By.XPATH,
                                     value='//*[@id="WYSIWGChatInputEditor_SkipChat"]/div/div[2]/div/span/span/span')
    area_music.send_keys('https://youtu.be/aOLXZOc2iwk?si=SbVlaV2U6ekG7-DN')


# Отправить музыку
def is_button_send(driver):
    button_send = driver.find_element(by=By.XPATH,
                                      value='//*[@id="live-page-chat"]/div/div/div[2]/div/div/section/div/div[6]/div[2]/div[2]/div[2]/div[3]/div/button')
    button_send.click()


def main(link_stream):
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\Дом\\AppData\\Local\\Google\\Chrome\\User Data")  # Путь до браузера
    options.add_argument("profile-directory=Profile 1")  # выбор профиля
    options.add_experimental_option("detach", True)  # Оставить браузер открытым
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2.5)
    driver.get(link_stream)
    is_click_price(driver)
    is_click_music(driver)
    is_get_link_music(driver)
    # is_button_send(driver)


if __name__ == '__main__':
    main('https://www.twitch.tv/ankeriascarlet')
