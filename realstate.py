<수집계획서>

<데이터 수집 목적>

 아파트 주변의 환경요인(학군,교통,편의시설,개발구역 등)들이 실거래가에 어떤 영향을 미쳤는지 알아보기 위해 국토교통부 홈페이지에서 아파트 실거래가를 크롤해온다.


<데이터 수집 과정>

1. 아파트 메뉴에서 지역 (서울특별시,노원구)를 선택하여 노원구에 해당하는 동들의 코드를 가지고온다.
2. 한 동 (ex. 공릉동)에 있는 아파트 목록을 검색하여 불러온다
3. 각 아파트의 아파트코드를 가지고온다.
4. 각각의 아파트코드가 가지고 있는 아파트의 상세내역을 가지고온다.
5. 상세내역에는 년도, 월, 아파트이름, 전용면적, 계약일, 거래금액, 층, 건축년도, 도로조건의 정보가 들어있다.
6. 200개 정도의 데이터를 가지고 온 후 보안번호 팝업시 보안번호를 해제하고 보안번호 팝업 직전의 데이터부터 다시 가져온다.
7. 가져온 데이터를 HTML에 저장한다.

<수집과정에서 어려웠던 부분>
- 일정량의 데이터를 가지고 오면 보안이 막혀서 데이터를 한번에 가지고 오는게 원활하지 않았었다. 보안번호를 우회하거나 무력화시키는 방법도 해보았지만 쉽지 않았다.


from bs4 import BeautifulSoup
import requests
import json
import urls

headers = { "Referer": "http://rt.molit.go.kr/new/gis/srh.do?menuGubun=A&gubunCode=LAND",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

def open_captcha():
    from selenium import webdriver
    import os

    if os.name == "nt":
        driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32/chromedriver.exe')
    elif os.name == "posix": 
        driver = webdriver.Chrome('/Users/mac/workspace/chromedriver')  # mac or linux
    else:
        print("Not supported OS")
        exit()

    driver.get("http://rt.molit.go.kr/new/pop/captcha_Popup.do")
    userinput = input("<<<<<<<<<<<<<<<<<<<<< ===================")
    driver.close()



def get_dong_code():
    from bs4 import BeautifulSoup
    import requests

    url = "http://rt.molit.go.kr/new/gis/getDongListAjax.do" #POST

    simplified_apt_code_list = {}
    params = {'menuGubun': 'A' ,
              'gubunCode': 'LAND',
              'sidoCode': '11',
              'gugunCode': '11350'}

    html = requests.post(url, params=params, headers=headers)
    jsonData = json.loads(html.text)
    dong_name_list = jsonData["jsonList"]

    simplified_dong_code_list = {}
    for dong_name in dong_name_list:
        simplified_dong_code_list[dong_name["NAME"]] = dong_name["CODE"]
        print("Keep-Alive >>>>>>>>>>>>", html.headers['Keep-Alive'])
        print("", html.headers['Set-Cookie'])
        print("기초 동을 가지고 오는 중입니다..........................", dong_name["NAME"])
    
    return simplified_dong_code_list



def get_apartment_code(dongCode):
    url = "http://rt.molit.go.kr/new/gis/getDanjiComboAjax.do" #POST

    params = {
        'menuGubun': 'A',
        'srhYear': '2019',
        'srhLastYear': '2018',
        'gubunCode': 'LAND',
        'sidoCode': '11',
        'gugunCode': '11350',
        'dongCode': dongCode,
        'rentAmtType': '3'
    }

    html = requests.post(url, params=params, headers=headers)
    jsonData = json.loads(html.text)
    apt_name_list = jsonData["jsonList"]

    simplified_apt_code_list = {}
    for apt_name in apt_name_list:
        simplified_apt_code_list[apt_name["APT_NAME"]] = apt_name["APT_CODE"]
        print("Keep-Alive >>>>>>>>>>>>", html.headers['Keep-Alive'])
        print("", html.headers['Set-Cookie'])
        print("아파트 이름을 가지고 오는 중입니다..........................", apt_name["APT_NAME"])

    return simplified_apt_code_list



def get_detailed_apartment_information(dong_name, APT_NAME, APT_CODE, session_cnt, session):
    url = "http://rt.molit.go.kr/new/gis/getDanjiInfoDetail.do"  #GET

    params = {"menuGubun": "A",
            'p_apt_code': str(APT_CODE),
            'p_house_cd':'1',
            'p_acc_year':'2018',
            'areaCode':'',
            'priceCode':''}
    print(params)

    if session_cnt >= 90:
        print("\n서버로부터 새로운 SESSION ID를 할당받아 사용합니다.")
        session = requests.session()
        session_cnt = 0
    
    elif session_cnt == 0:
        print("\n서버로부터 새로운 SESSION ID를 할당받아 사용합니다.")
        session = requests.session()

    else:
        print("\n할당된 SESSION ID를 이용하여 재접속합니다.")
        
    html = session.get(url, params=params, headers=headers)
    jsonData = json.loads(html.text)

    try:
        detailed_information_list = jsonData["result"]
    except:
        open_captcha()

    html = session.get(url, params=params, headers=headers)
    jsonData = json.loads(html.text)
    detailed_information_list = jsonData["result"]        

    print("Keep-Alive >>>>>>>>>>>>", html.headers['Keep-Alive'])
    print("아파트 정보를 가지고 오는 중입니다.......................... ", dong_name, ". ", APT_NAME)
    
    arranged_apartment_informations = {}
    # saveFile = "./GW_Study/Crawling/results/test_____house.html"
    saveFile = "./results/test_____house____{}.html".format(dong_name)
    try:
        file = open(saveFile, mode='x')
        file.close()
    except:
        pass
    sseion_cnt_in_function = 1
    for detailed_information in detailed_information_list:
        sseion_cnt_in_function += 1

        arranged_apartment_informations[detailed_information["BLDG_CD"]] = {
                    "DNAME"   : detailed_information["DNAME"],
                    "BLDG_NM": detailed_information["BLDG_NM"],
                    "BOBN": detailed_information["BOBN"],
                    "BLDG_AREA": detailed_information["BLDG_AREA"],
                    "DEAL_MM": detailed_information["DEAL_MM"],
                    "DEAL_DD": detailed_information["DEAL_DD"],
                    "SUM_AMT": detailed_information["SUM_AMT"],
                    "APTFNO": detailed_information["APTFNO"],
                    "BUILD_YEAR": detailed_information["BUILD_YEAR"],
                    "ROAD_LEN": detailed_information["ROAD_LEN"],
                    "BC_RAT": detailed_information["BC_RAT"],
                    "VL_RAT": detailed_information["VL_RAT"]
                }

        adding = open(saveFile, mode='a')
        adding.writelines(str(arranged_apartment_informations[detailed_information["BLDG_CD"]]))
        adding.close()

    # print(">>>>>>>>>>>>>>>sssss : ", sseion_cnt_in_function)
    session_cnt += sseion_cnt_in_function
    return (session_cnt, session)




if __name__ == "__main__":
    dong_names = get_dong_code()
    for dong_name in dong_names:
        apt_names = get_apartment_code(dong_names[dong_name])
        print("현재의 동은 ", dong_name," 입니다.")
        print(apt_names)

        session = requests.session()
        session_cnt = 0
        for apt_name in apt_names:
            result = get_detailed_apartment_information(dong_name, apt_name, apt_names[apt_name], session_cnt, session)
            session_cnt = result[0]
            session = result[1]



