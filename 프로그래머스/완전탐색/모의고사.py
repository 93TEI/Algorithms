# 모의고사

def solution(answers):
    # 1,2,3번 수포자를 for문으로 미리 만들어서 비교할 생각
    n1,n2,n3,answer= [],[],[],[]
    n1_cnt, n2_cnt, n3_cnt,temp = 0,0,0,0
    
    # n1 리스트 만들기
    n_list = [1,2,3,4,5]
    for i in range(0,len(answers)+1) :
        if i%5 == 0 :
            temp+=1
        n1.append(n_list[i-(temp*5)])

    # n2 리스트 만들기
    n_list, temp = [2,1,2,3,2,4,2,5], 0
    for i in range(len(answers)):
        if i%8 == 0 :
            temp += 1
        n2.append(n_list[i-(temp*8)])
    
    # n3 리스트 만들기
    n_list, temp = [3,3,1,1,2,2,4,4,5,5], 0
    for i in range(len(answers)) :
        if i%10 == 0 :
            temp += 1
        n3.append(n_list[i-(temp*10)])
    
    # 각각 수포자들이 몇개 맞았는지 확인
    for i in range(len(answers)) :
        if answers[i] == n1[i] :
            n1_cnt += 1
        if answers[i] == n2[i] :
            n2_cnt += 1
        if answers[i] == n3[i] :
            n3_cnt += 1
    
    # max와 같은 값을 가진 수포자를 answer 리스트에 append
    n_cnt = [n1_cnt, n2_cnt, n3_cnt]
    max_cnt = max(n_cnt)
    for i in range(3) :
        if max_cnt == n_cnt[i] :
            answer.append(i+1)
    
    # 2명 이상일 경우 오름차순 정렬
    if len(answer) >1 :
        answer.sort()
    return answer