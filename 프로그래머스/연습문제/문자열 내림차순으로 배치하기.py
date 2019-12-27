# 문자열 내림차순으로 배치하기
def solution(s):
    answer = list(s)
    result = ''
    for i in range(len(s)-1) : # 정렬
        for j in range(len(s)-1) :
            if ord(answer[j]) < ord(answer[j+1]) :
                temp = answer[j]
                answer[j] = answer[j+1]
                answer[j+1] = temp
    for i in range(len(answer)) : # 리스트였기 때문에 다시 문자열로 만들어서 return
        result += answer[i]
    return result