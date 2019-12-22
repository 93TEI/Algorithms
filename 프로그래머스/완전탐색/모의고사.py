# 모의고사

def solution(answers):
    answer = []
    # 1,2,3번 수포자를 for문으로 미리 만들어서 비교할 생각
    n1 = []
    n2 = []
    n3 = []
    temp=0
    for i in range(len(answers)) :
        if temp == 6 :
            temp = 0
        n1.append(i+1+temp)
        
    for i in range(len(answers)) :
        answers[i] 
    
    return answer