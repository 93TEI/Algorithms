# 완주하지 못한 선수
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

# 풀기 위해 많은 것을 배웠다.
# 튜플, 딕셔너리, 리스트를 다시 봄은 물론, 해시에 대해서도 알아보는 시간이 되었다.
# 그중 시간복잡도에 대한 생각을 가지게 된 것이 가장 큰 수확인 것 같다.