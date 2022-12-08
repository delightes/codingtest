def solution(common):
    answer = 0
    a,b,c = common[:3]
    
    if (b-a == c-b): #등차수열
        answer = common[-1] + (b-a)
    else: #등비수열
        answer = common[-1] * (b//a)
    
    return answer

result = solution([2, 4, 8])
print(result)