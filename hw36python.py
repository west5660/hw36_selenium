
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def click_video(browser):
    videos = browser.find_elements(By.XPATH, '//*[@id="video-title"]')
    if videos:
        video = videos[0]
        video.click()

def like_video(browser):
    like_button = browser.find_element(By.XPATH, '//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div')
    like_button.click()

browser = webdriver.Edge()
browser.get('https://www.youtube.com/')
elem3 = browser.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div')
elem3.click()
time.sleep(1)
elem1 = browser.find_element(By.NAME, "search_query")
elem1.send_keys('смешные видео про котов')
elem1.submit()  # Отправить поисковый запрос

time.sleep(3)
click_video(browser)  # Кликнуть на видео
time.sleep(3)
like_video(browser)  # Поставить лайк

time.sleep(5)
browser.close()



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
browser.get('https://citaty.info/')
random = browser.find_element(By.LINK_TEXT, 'Случайная цитата')
random.click()
time.sleep(5)
citata = browser.find_element(By.CLASS_NAME, 'field-items')
print(citata.text)
time.sleep(3)
browser.close()



