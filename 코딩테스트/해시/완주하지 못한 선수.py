# 완주하지 못한 선수
def solution(participant, completion):
    for i in range(0,len(participant)):
        completion.pop(completion.index(participant[i]))
    answer = completion
    return answer