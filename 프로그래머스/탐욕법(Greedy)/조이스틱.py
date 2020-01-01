# 조이스틱 // 조작 횟수의 최소값을 return
def solution(name):
    answer = 0
    n = list(name)
    n1 = min(abs(ord(n[0]) - 65), abs(91 - ord(n[0])))
    
    return answer


# len(name)만큼 for문 돌리고
# 그 안에서 각 글자마다 최소값을 판단 (가중치)
# 첫번째, 첫글자 최소값
# 두번째, 두번째글자와 맨뒤(-1)글자 중 A가 있는지 판단 -> 그 반대로 커서 갈것
# 그 방향으로 모든 글자 최소값 판단해서 cnt++