# 모의고사
def solution(answers):
    answer = []
    n1_cnt, n2_cnt, n3_cnt = 0
    n1 = {1:'1',2:'2',3:'3',4:'4',5:'5'}
    n2 = {1:'2',2:'1',3:'2',4:'3',5:'2',6:'4',7:'2',8:'5'}
    n3 = {1:'3',2:'3',3:'1',4:'1',5:'2',6:'2',7:'4',8:'4',9:'5',10:'5'}
    
    n_list = [n1,n2,n3]
    n_cnt_list = [0,0,0]
    
    for i in range(3) :
        for j in range(len(answers)) :
            if answers[j] == n_list[i][j] :
                n_cnt_list[i] += 1
    
    # 문제 잘못봤네 다시풀것
        
    return answer