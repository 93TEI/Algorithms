# 모의고사

def solution(answers):
    answer = []
    # 1,2,3번 수포자를 for문으로 미리 만들어서 비교할 생각
    n1 = []
    n2 = []
    n3 = []
    temp = 0
    # n1 리스트 만들기
    for i in range(len(answers)) :
        if i%5 == 0 :
            temp += 1
        n1.append(i+1-(temp*5))
    
    temp = 1
    # n2 리스트 만들기
    for i in range(len(answers)):
        if (i+1)%2 == 1 :
            n2.append(2)
        else :
            if temp == 6 :
                temp = 1
            n2.append(temp)
            temp += 1
    
    # n3 리스트 만들기
    for i in range(len(answers)) :
        
        
    for i in range(len(answers)) :
        answers[i] 
    
    return answer