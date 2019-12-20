#K번째 수
def solution(array, commands):
    answer=[]
    for n in range(0,3):
        temp=array[commands[n][0]:commands[n][1]+1]
        temp.sort()
        answer.append(temp[commands[n][2]])
    return answer