# saramin-repo-2
사람인 웹데이터 수집 담당자 전진환


# Commit 가이드
아래 테이블을 참고하여 commit 할 때 최소한의 기록을 해주세요.

|순서|커밋네이밍|설명|
|:---:|:---:|---|
|1|feat|새로운 기능 추가|
|2|fix|문서 수정|
|3|style|코드 스타일 수정|
|4|test|테스트 코드|
|5|refactor|리팩토링 코드|
|6|rename|파일 혹은 폴더명만 수정한 경우|
|7|remove|파일 혹은 폴더만 삭제한 경우|

- Ex : git commit -m "fix: 34~40 line의 코드를 수정하였습니다."

# 설명  
안녕하세요. 혹시나 코드를 보시고 짚어주실게 있다면 코드리뷰 꼭 부탁드리겠습니다. 많이 배우겠습니다. 감사합니다.

해당 코드는 동적크롤링인 selenium을 활용하였습니다.
설치가 어렵더라도 **저를 찾지 말아주세요**.

# 진행 상황
data 키워드를 입력하고 들어가서 10page 가량의 텍스트를 가져와서 dataframe에 저장하고 csv file을 생성합니다.
10page 넘으면 예외처리를 안해서 에러가 발생되고 멈춥니다.

# 개선 방향
하고 싶은거 선택해서 진행하셔도 무방합니다.
1. 코드를 깔끔하게 수정할 계획입니다. 
2. 수정이 끝나면 코드의 기능을 개선할 예정입니다.

```python

class docs:
    '''docstring'''

    def tag_click() -> list:
        '''docstring'''
        return

def main():
    '''docstring'''
    return

if __name__=='__main__':
    docs.tag_click()
    main()

```

# 설치 가이드
1. 크롬 최신버전 설치
    - 과거와 다르게 별도의 chromedriver 설치 및 chrome 강제 업데이트 막기가 필요없습니다.
2. anaconda 설치 및 가상환경 셋팅
    - conda create -n crawling python=3.8
    - conda activate crawling
    - pip install selenium pandas numpy
3. 아래 간단한 동작 실행

# Selenium 바뀐 문법 간단하게 알아보기
- [문법 바뀐 Selenium](https://velog.io/@bbhaunt/%EB%AC%B8%EB%B2%95-%EB%B0%94%EB%80%90-selenium)


# 간단한 동작해보기

```python
import time
import selenium
from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
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
```