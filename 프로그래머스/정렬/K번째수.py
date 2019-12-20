#K번째 수
def solution(array, commands):
    answer=[]
    for n in range(0,len(commands)):
        temp=array[commands[n][0]-1:commands[n][1]] # 범위 실수
        temp.sort()
        answer.append(temp[commands[n][2]-1]) # 범위 2번째 실수
    return answer

# 쉽다고 생각했는데 틀렸다.
# 항상 자만하지 말고 정확히 푸는 습관을 들여야할 것