def solution(babbling):
    count = 0
    
    canSay = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for j in canSay:
            if j in i:
                i = i.replace(j, ' ') #띄어쓰기로 대체
            
        if (len(i.strip()) == 0): #공백 없애서 글자수 0이면 +1
            count += 1
            
    return count

result = solution(["aya", "yee", "u", "maa", "wyeoo", "yemaye"])
print(result)