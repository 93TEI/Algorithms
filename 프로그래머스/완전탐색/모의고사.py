# 모의고사
from itertools import cycle
def solution(answers):
    n1, n2, n3 = [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]
    cnt, answer = [0,0,0],[] # 미리 패턴을 선언해둠
    #zip을 이용해서 묶고 cycle로 반복해서 가져와서 비교함
    for _n1,_n2,_n3,_answers in zip(cycle(n1),cycle(n2),cycle(n3),answers) :
        if _answers == _n1 : cnt[0] += 1
        if _answers == _n2 : cnt[1] += 1
        if _answers == _n3 : cnt[2] += 1
    _max =max(cnt) # for문에서 돌리면 3번 돌리게 돼 비효율적이라 생각해 위로 빼서 한번만 돌림
    for i in range(3): # 비교 후 앞에서부터 넣기 때문에 오름차순 정렬을 하지 않아도 됨
        if cnt[i] == _max : answer.append(i+1)
    return answer