# 문자열 내림차순으로 배치하기
def solution(s):
    answer = s
    temp_answer, cnt = '', 0 # 임시변수
    for i in range(len(s)-1) : # 정렬
        if answer[i] > answer[i+1] :
            temp = answer[i]
            answer[i] = answer[i+1]
            answer[i+1] = i
    for i in range(len(s)) : # 대문자는 뒤로 빼서 다시 합치기
        if int(answer[i]) >= 65 and int(answer[i]) <= 90 :
            temp_answer += answer[i]
            cnt += 1
    result = answer[cnt:]+temp_answer
    return result