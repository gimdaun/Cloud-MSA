#1. 딕셔너리를 이용해서 평균 점수 구하기
dicData1 = { "국어": 95, "영어": 90, "수학": 80, "과학": 50 }
SumData1 = dicData1["국어"]+dicData1["영어"]+dicData1["수학"]+dicData1["과학"] 
result = SumData1/4

#2. Set을 이용해서 1~100까지 숫자중에 공배수를 구함 : 5의 공배수만 구하기
#setData1 = range(1,101)   
setData1 = {i for i in range(1,101) if (i % 3) == 0}
setData2 = {i for i in range(1,101) if (i % 5) == 0}
result2 = setData1 | setData2 
print(result2)

#3. 리스트 데이터 7,5,3,1,-1,-3,-5,-7 출력
listData = [i for i in range(-7,8) if i % 2 != 0] 
listData.reverse()
print(listData)

#4. 튜플로 변경
tupleData = tuple(listData) 
print(tupleData)

temp = 0