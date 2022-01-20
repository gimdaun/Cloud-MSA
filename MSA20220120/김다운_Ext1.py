#1. 딕셔너리를 이용해서 평균 점수 구하기
dicData1 = { "국어": 95, "영어": 90, "수학": 80, "과학": 50 }
dicData2 = { "국어": 100, "영어": 50, "수학": 90, "과학": 90 }
dicData3 = { "국어": 99, "영어": 60, "수학": 100, "과학": 40 }
dicData4 = { "국어": 55, "영어": 80, "수학": 80, "과학": 60 }

dic=[dicData1,dicData2,dicData3,dicData4]
sum=0
ave_sum=0
all_sum=0
for i in dic:
    for j in i.values():
        sum=sum+j
    #print(sum)
    ave=sum/len(i.keys())
    #print(ave)
    all_sum=sum+all_sum
    ave_sum=ave+ave_sum
    sum=0
    average = 0
all_ave=ave_sum/len(i.keys())
print(all_sum)
print(all_ave)


temp = 0
