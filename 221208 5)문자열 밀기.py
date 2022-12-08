"""
첫번째 풀이
"""
def solution1(A, B):
    answer = 1
    temp = ''
    word = A[-1] + A[0:-1]
    
    if(A == B):
        return 0
    
    elif (word == B):
        return answer
    
    else:
        for i in range(len(B)):
            temp = word[0:-1]
            word = word[-1] + temp
            answer += 1
            print(i,'번째', word, answer)
            
            if (word == B):
                return answer

        if(answer >= len(B)):
            return -1

"""
두번째 풀이 - 큐 사용
"""
from collections import deque
def solution2(A, B):
    answer = 0
    a, b = deque(A), deque(B)
    
    for i in range(len(A)):
        if (a == b):
            return answer
        answer += 1
        a.rotate(1)
        
    return -1

"""
세번째 풀이 - 리스트 사용
"""
def solution3(A, B):
    a, b = list(A), list(B)
    answer = 0

    for i in range(len(A)):
        if (a == b):
            return answer
        
        temp = a.pop()
        a.insert(0, temp)
        answer += 1
        print(a, b, answer)

    return -1
