# 체육복

# 전체 학생 n, 도난당한 학생들 번호 배열 lost, 여벌 체육복 학생 번호 배열 reserve
import collections
def solution(n, lost, reserve):
    answer = n - len(lost)
    temp_lost = list(lost)
    for i in temp_lost :
        if i in reserve : # 여벌 체육복 학생이 도난당하면 다른학생 못빌려주고 자신이 입어야함
            answer += 1
            reserve.pop(reserve.index(i))
            lost.pop(lost.index(i))            
    temp_lost = list(lost)
    for i in lost : # lost의 앞번호 학생이 여분을 가지고 있다면 1 올리기
        temp = (i-1) in reserve
        if temp == True :
            answer += 1
            reserve.pop(reserve.index(i-1))
        else : # 앞번호 학생이 여분이 없다면 뒷번호 학생의 여분 확인해서 1 올리기
            temp = (i+1) in reserve
            if temp == True :
                answer += 1
                reserve.pop(reserve.index(i+1)) # 빌려주면 여분에서 빼기
    return answer

# 계속 런타임 오류 났던 이유 : for i in lost인데 lost.pop(i)를 하니까 중간에 빠지는 게 생긴 것
# -> 그래서 lost를 복사해서 for문을 돌렸다.