import time
import selenium
from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument('log-level=3')
import warnings
warnings.filterwarnings('ignore')

# 페이지 진입
driver = webdriver.Chrome()
url = 'https://www.saramin.co.kr/'
driver.get(url)
time.sleep(1.5)

# 검색창에 검색 키워드 입력
search = "data"


# 검색창 클릭
driver.find_element(By.CSS_SELECTOR, 'button#btn_search.btn_search').click()
time.sleep(1.5)

# 검색창을 클릭했을때 검색창이 한번 더 나오고 다시 클릭
search_bax = driver.find_element(By.TAG_NAME, 'input')
search_bax.send_keys(search)
time.sleep(1.5)

driver.find_element(By.CSS_SELECTOR, 'button#btn_search_recruit.btn_search').click()
time.sleep(1.5)

# 채용정보 리스트 태그를 찾고 text 값으로 출력하기
info_list_all = driver.find_elements(By.XPATH, '//*[@id="recruit_info_list"]/div[1]/div')
info_list_addr = driver.find_elements(By.XPATH, '//*[@id="recruit_info_list"]/div[1]/div/div/h2/a')
    

# 다음 채용정보 리스트로 넘어가기
next_buttom = len(driver.find_elements(By.XPATH, '//*[@id="recruit_info_list"]/div[2]/div/a'))

df = pd.DataFrame()

for i in range(1000):
    info_list_all
    info_list_addr
    
    '''
    pandas 변환
    '''
    # info_list_all 리스트에서 각 값을 innerText 속성으로 가져옵니다.
    info_list_all_inner = [i.get_attribute('innerText') for i in info_list_all]
    time.sleep(3)

    # info_list_addr 리스트에서 각 값을 href 속성으로 가져옵니다.
    info_list_addr_href = [i.get_attribute('href') for i in info_list_addr]
    time.sleep(3)

    # info_list_all_inner 리스트와 info_list_addr_href 리스트를 컬럼으로 가지는 데이터프레임을 생성합니다.
    df = pd.DataFrame({'이름': info_list_all_inner, '링크': info_list_addr_href})

    print(df)
    time.sleep(5)
    
    # df = pd.concat([df, pd.DataFrame({'이름': info_list_all_inner, '링크': info_list_addr_href})])
    # time.sleep(5)
            
    try:
        for j in range(next_buttom):
            refix_buttom = driver.find_elements(By.XPATH, '//*[@id="recruit_info_list"]/div[2]/div/a')[j]
            time.sleep(3)
            refix_buttom.click()
            time.sleep(3)
            print('다음 페이지로 넘어갑니다. :')
            time.sleep(10)
            
            df = pd.concat([df, pd.DataFrame({'이름': info_list_all_inner, '링크': info_list_addr_href})])
            time.sleep(5)
    except:
        break
    finally:
        df.to_csv('data.csv', index=False)


# if __name__=='__main__':
    