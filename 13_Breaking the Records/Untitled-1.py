scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]#[10, 5, 20, 20, 4, 5, 2, 25, 1]

cnt_high=0
cnt_low=0

highest= scores[0]
lowest = scores[0]

print(highest, lowest)
for i in range(len(scores)):
    if scores[i] > highest:
        highest = scores[i]
        cnt_high = cnt_high + 1
    if scores[i] < lowest:
        lowest = scores[i]
        cnt_low = cnt_low + 1
print(highest, lowest)
print(cnt_high, cnt_low)
