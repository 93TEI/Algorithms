# 조이스틱 // 조작 횟수의 최소값을 return
def solution(name):
    n = list(name)
    j_temp = 0
    n1 = min(abs(ord(n[0]) - 65), abs(91 - ord(n[0]))) # 첫 글자
    answer1, answer2 = n1, n1 # 오름차순, 내림차순 판단하기 위해 두 가지 케이스로 나눔
    # 오른차순
    for i in range(1,len(n)):
        temp = min(abs(ord(n[i]) - 65), abs(91 - ord(n[i])))
        answer1 += temp + 1
    for j in range(len(n)-1,0,-1) :
        if n[j] != 'A' : break
        j_temp += 1
    answer1 -= (len(n)-1-j)
    cnt_A = 0
    # 내림차순
    for i in range(len(n)-1,0,-1):
        temp = min(abs(ord(n[i]) - 65), abs(91 - ord(n[i])))
        answer2 += temp + 1
    for j in range(1,len(n)) :
        if n[j] != 'A' : break
        j_temp += 1
    answer2 -= j-1
    answer = min(answer1,answer2)
    return answer

# 4
# len(name)만큼 for문 돌리고
# 그 안에서 각 글자마다 최소값을 판단 (가중치)
# 첫번째, 첫글자 최소값
# 두번째, 두번째글자와 맨뒤(-1)글자 중 A가 있는지 판단 -> 그 반대로 커서 갈것
# 그 방향으로 모든 글자 최소값 판단해서 cnt++