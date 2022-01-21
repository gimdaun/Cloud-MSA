import json

# with open("datalab\\mydata.json", "rb") as jsonFile:
#     tempData = json.load(jsonFile)
#     #tempData = json.loads(jsonFile)#오류
#     reusltData1 = tempData["name"]
#     reusltData2 = tempData["age"]
#     reusltData3 = tempData["address"]
#     reusltData4 = tempData["email"]
#     reusltData5 = tempData["empcheck"]
try:
    changeFile = open("datalab\\mydata.json", "rb")
    tempData = json.load(changeFile)
    reusltData1 = tempData["name"]
    reusltData2 = tempData["age"]
    reusltData3 = tempData["address"]
    reusltData4 = tempData["email"]
    reusltData5 = tempData["empcheck"]
except KeyError:
    print("오류 : 잘못된 키값입니다." ) 
except (Exception,TypeError) as error:
    print("오류 : " + error)
else:
    changeFile.close()
    

jsonData1 = {
        "empid": 12345678,
        "name" : "홍길동",
        "info" : [
            {"date1": "2022-01-21", "home": "서울시"},
            {"dep": "개발", "email": "aaa@aaa.co.kr"}
        ]
    }

# with open("datalab\\mydata2.json", "w") as writeFile:
#     json.dump(jsonData1, writeFile) # 옵션으로 indent=숫자   #한글이 이상함
try:
    changeFile = open("datalab\\mydata2.json", "w")
    json.dump(jsonData1, changeFile)
except IndexError as error:
    print("오류 : " + error) 
except FileNotFoundError:
    print("오류 : 파일을 찾을 수 없습니다.") 
else:
    changeFile.close()


# with open("datalab\\mydata3.json", "w", encoding="utf-8") as writeFile:
#     json.dump(jsonData1, writeFile, ensure_ascii=False) # 옵션으로 indent=숫자 , 한글을 완벽히 처리  
try:
    changeFile = open("datalab\\mydata3.json", "w", encoding="utf-8")
    json.dump(jsonData1, changeFile, ensure_ascii=False) 
except Exception as error:
    print("오류 : " + error) 
else:
    changeFile.close()

    
# with open("datalab\\mydata4.json", "w") as writeFile:
#     json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4) # 옵션으로 indent=숫자    
#     # 한글이 문제가 있음
try:
    changeFile = open("datalab\\mydata4.json", "w")
    json.dump(jsonData1, changeFile, ensure_ascii=False, indent=4)
except Exception as error:
    print("오류 : " + error) 
else:
    changeFile.close()


# with open("datalab\\mydata5.json", "w", encoding="utf-8") as writeFile:
#     json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4) # 옵션으로 indent=숫자 , 한글을 완벽히 처리  
try:
    changeFile = open("datalab\\mydata5.json", "w", encoding="utf-8")
    json.dump(jsonData1, changeFile, ensure_ascii=False, indent=4) 
except Exception as error:
    print("오류 : " + error) 
else:
    changeFile.close()

#디버깅 변수 선언함(임시)
temp = 0
