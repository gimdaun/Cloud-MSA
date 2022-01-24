from flask import Flask
import json
import requests

app = Flask(__name__) 

@app.route("/data1")
def FlaskData():
    keyValue =r"tzNdpBB6EDyPn7B1MHodkDLXb5d7rQeJ1JFMfxvFMDxnyw9ii0Kei8Lvvi946HnnhuJNqb%2FJLfkGEUbSddqSMg%3D%3D"

    dataURL = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += "page=" + str(1) + "&perPage=" + str(10)
    dataURL += "&cond" + r"%5BorgZipaddr%3A%3ALIKE%5D=%EC%84%B1%EB%B6%81%EA%B5%AC"
    dataURL += "&serviceKey=" + keyValue

    dataResult = requests.get(dataURL)

    result = json.loads(dataResult.text)
    #result2 = json.dumps(result, ensure_ascii=False, indent=5)
    changeFile = open("FlaskLab\\mydata.json", "w", encoding="utf-8")
    result2 = json.dump(result, changeFile, ensure_ascii=False, indent=5) 
    #print(result2)
    
    return result2
