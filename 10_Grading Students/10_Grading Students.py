import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    result=[]
    grades = [int (i) for i in grades] #리스트를 int형으로 형변환해줌
    for i in grades:
        if i >= 38 : #38보다 클 때만 변환의 의미가 있음
            if (i+1) % 5 == 0 : # 5로 나눠 떨어지면 반올림할껀데 그 경우의 수는 +1과+2 두개뿐
                result.append(i+1)
            elif (i+2) % 5 == 0 :
                result.append(i+2)
            else :
                result.append(i)
        else :
            result.append(i)
        
    return result
        


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    grades = []
    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)
    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')
    f.close()