import sys
import csv
from selenium import webdriver
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import re
import os
#s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.maximize_window()

# default path to file to store data


# default number of scraped pages
#num_page = 300
# if (len(sys.argv) == 4):
#     path_to_file = sys.argv[1]
#     num_page = int(sys.argv[2])
#     url = sys.argv[3]

#url = "https://www.tripadvisor.com/Hotel_Review-g60763-d1218720-Reviews-The_Standard_High_Line-New_York_City_New_York.html"
#url = "https://www.tripadvisor.com/Attraction_Review-g187791-d192285-Reviews-Colosseum-Rome_Lazio.html"
#url="https://www.tripadvisor.com/Hotel_Review-g293734-d302479-Reviews-Movenpick_Hotel_Mansour_Eddahbi_Marrakech-Marrakech_Marrakech_Safi.html"



def hotel_name_f(string, start_text, end_text):
    extracted_text = re.search(f'{start_text}(.*?){end_text}', string).group(1)
    return extracted_text



#url="https://www.tripadvisor.com/Hotel_Review-g293731-d549638-Reviews-Iberostar_Founty_Beach-Agadir_Souss_Massa.html"
# import the webdriver


urls = [
 "https://www.tripadvisor.com/Hotel_Review-g293731-d316732-Reviews-Kenzi_Europa_Hotel-Agadir_Souss_Massa.html",
"https://www.tripadvisor.com/Hotel_Review-g293731-d2573287-Reviews-Sofitel_Agadir_Thalassa_Sea_Spa-Agadir_Souss_Massa.html",
"https://www.tripadvisor.com/Hotel_Review-g293731-d600207-Reviews-Hotel_Riu_Tikida_Dunas-Agadir_Souss_Massa.html"]

def create_csv(file_name):
    if not os.path.exists(file_name):
        open(file_name, 'w', newline='').close()




for url in urls:
    driver.get(url)
    # Do something with the current page, such as extract data or take a screenshot
    # ...
    # open the file to save the review
    hotel_name = hotel_name_f(url, 'Reviews-', '.html')
    file_name = f"{hotel_name}.csv"
    csvFile= f"{hotel_name}.csv"
    print(file_name)

    csvFile = open(file_name, 'w', encoding="utf-8")
    #create_csv(file_name)
    #csvWriter = create_csv(csvFile)
    csvWriter = csv.writer(csvFile)
    # for i in range(0, num_page):
    indexfin = True
    i = 0
    while (indexfin):
        # expand the review
        print('Page:' + str(i))
        i = i + 1
        time.sleep(3)
        review_per_page = 0
        container = driver.find_elements(By.XPATH, "//div[@data-reviewid]")
        for j in range(len(container)):
            # print(j)
            try:
                rating = container[j].find_element(By.XPATH,
                                                   ".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute(
                    "class").split("_")[3].replace('0', '')
                title = container[j].find_element(By.XPATH, ".//div[contains(@data-test-target, 'review-title')]").text
                review = container[j].find_element(By.XPATH, ".//q[@class='QewHA H4 _a']").text.replace("\n", "  ")
                datestxt = container[j].find_element(By.XPATH, ".//span[@class='teHYY _R Me S4 H3']").text
                x = datestxt.find(":")
                dates = datestxt[x + 1:]
                # print(title)
                csvWriter.writerow([dates, rating, title, review, hotel_name])
            except NoSuchElementException:
                break

            # change the page

        try:
            btnenabled = driver.find_element(By.XPATH, './/a[@class="ui_button nav next primary "]')
            driver.find_element(By.XPATH, './/a[@class="ui_button nav next primary "]').click()

            # break
        except NoSuchElementException:
            print('Fin')
            indexfin = False
            break

driver.quit()


