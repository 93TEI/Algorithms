-- 코드를 입력하세요
SELECT NAME, COUNT(*) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) > 1
# 오래 끌었다. COUNT(*)이 아닌 COUNT(NAME)으로 해야 정답
# 결과값은 같았으나 이름을 카운트해야 하는 것 같다
