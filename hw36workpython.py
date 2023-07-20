

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# browzer = webdriver.Edge()
# browzer.get('https://klik-test.ru/')
# # elem2 = browzer.find_element(By.ID,"clicker")  # нашли кнопку поиск
# # elem2.click()
# # time.sleep(5)
# # elem3 = browzer.find_element(By.ID,"reset")  # нашли кнопку поиск
# # elem3.click()
# # time.sleep(5)
# # browzer.close()
# elem2 = browzer.find_element(By.ID,"clicker")
# while True:
#     try:
#         elem2.click()
#     except:
#         break
# time.sleep(1)
# elem3 = browzer.find_element(By.ID,"result-info")
# print(elem3.text)
# browzer.close()

# browzer = webdriver.Edge()
# browzer.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
# elem5 = browzer.find_elements(By.CLASS_NAME,'ipc-metadata-list-summary-item')
# print(len(elem5))
# # for s in elem5:
# #     title = s.find_element(By.CLASS_NAME,'ipc-title__text')
# #     rate = s.find_element(By.CLASS_NAME,'ipc-rating-star')
# #     # print(title.text,rate.text)
# #     if float(rate.text)>=9:
# #         print(title.text,rate.text)
# # for s in elem6:
# #
#
# time.sleep(3)
# browzer.close()

browzer = webdriver.Edge()
browzer.get('https://www.imdb.com/chart/toptv/?ref_=chttp_ql_6')
elem6 = browzer.find_elements(By.CLASS_NAME,'ipc-metadata-list-summary-item')
print(len(elem6))
for s in range(10):
    print(f"{elem6[s].find_element(By.CLASS_NAME, 'ipc-title__text').text}"
            f"{elem6[s].find_element(By.CLASS_NAME, 'sc-14dd939d-6').text}")



for i in elem6:
    tv_name= i.find_element(By.CLASS_NAME,'ipc-title__text')
    tv_year = i.find_element(By.CLASS_NAME,'sc-14dd939d-6')
    if tv_year.text>='2016':
        print(tv_name.text)
        print('year = ',tv_year.text)



time.sleep(3)
browzer.close()