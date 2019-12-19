#전화번호 목록

def solution(phone_book):
    answer = True
    phone_book.sort() # 앞 숫자로 시작하는 리스트에 뒷숫자로 시작하는게 들어갈 리 없기 때문
    
    for i in range(len(phone_book)-1) : 
        i_len = len(phone_book[i]) # i번째 value의 길이
        i_value = phone_book[i] # i번째의 값
        for j in range(len(phone_book) - 1 - i) :
            if i_len <= len(phone_book[i+j]) :
                if i_value == phone_book[i+j][0:i_len] :
                    answer = False
                    return answer            
    return answer