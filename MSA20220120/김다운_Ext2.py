#1. 딕셔너리를 이용해서 평균 점수 구하기
dicData1 = { "국어": 95, "영어": 90, "수학": 80, "과학": 50 }
dicData2 = { "국어": 100, "영어": 50, "수학": 90, "과학": 90 }
dicData3 = { "국어": 99, "영어": 60, "수학": 100, "과학": 40 }
dicData4 = { "국어": 55, "영어": 80, "수학": 80, "과학": 60 }

dic=[dicData1,dicData2,dicData3,dicData4]

sum=0
all_sum=0
all_ave=0
i=0
j=0
num=0
print("개인 합계, 평균 : ")
while True:
    value=list(dic[i].values()) 
    
    if num < 4:
        j=value[num]
        sum=sum+j
        num=num+1
        if num==4:
            i=i+1
            print(sum, end=" ")
            ave=sum/len(value)
            print(ave,end=' ')
            print()
            all_sum=sum+all_sum
            all_ave=ave+all_ave
            sum=0
            num=0
            if i==4:
                i=0
                j=0
                print("\n전체 4명의 합계, 평균 : ")
                print(all_sum,end=' ')
                print(all_ave,end=' ')
                break
print("\n\n과목별 합계, 평균 : ")
while True:
    value=list(dic[i].values()) 
    if num != 4:
        j=value[num]
        sum=sum+j
        i=i+1
        if i==4:
            num=num+1
            print(sum, end=" ")
            ave=sum/len(value)
            print(ave,end=' ')
            print()
            i=0
            sum=0        
    else:    
        break

temp = 0