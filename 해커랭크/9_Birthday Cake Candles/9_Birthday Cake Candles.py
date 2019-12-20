import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    split_of_s = s.split(':')
    if split_of_s[2][2] =='A' and split_of_s[0]=="12" :
        split_of_s[0]="00"

    elif split_of_s[2][2] == 'P' and split_of_s[0]=="12":
        pass
    elif split_of_s[2][2] == 'P':
        split_of_s[0]=str(int(split_of_s[0]) + 12)
        
    result = split_of_s[0]+':'+split_of_s[1]+':'+split_of_s[2][0]+split_of_s[2][1]
    return result
    
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()