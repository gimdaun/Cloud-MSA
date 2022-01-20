#1. 딕셔너리를 이용해서 평균 점수 구하기
dicData1 = { "국어": 95, "영어": 90, "수학": 80, "과학": 50 }
dicData2 = { "국어": 100, "영어": 50, "수학": 90, "과학": 90 }
dicData3 = { "국어": 99, "영어": 60, "수학": 100, "과학": 40 }
dicData4 = { "국어": 55, "영어": 80, "수학": 80, "과학": 60 }
dic=[dicData1,dicData2,dicData3,dicData4]
sum=0
all_sum=0
all_ave=0
print("\n개인 합계, 평균 : ")
for i in dic:
    #print(i)
    for j in i.values():
        sum=sum+j
    print(sum,end=' ') 
    ave=sum/len(i.keys())
    print(ave,end=' ')
    print()
    all_sum=sum+all_sum
    all_ave=ave+all_ave
    sum=0
    average = 0
print("\n전체 4명의 합계, 평균 : ")
print(all_sum,end=' ')
print(all_ave,end=' ')
    
print("\n과목별 합계")
for num in range(4):
    for i in dic:
        value=list(i.values())
        #print(value)
        sum=sum+value[num]       
    ave=sum/len(i.keys())
    print(sum,end=' ')
    print(ave,end=' ')
    print()
    sum=0
    ave=0

temp = 0