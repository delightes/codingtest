def solution(num, total):
    answer = [0] * num
    average = total // num
    middle = 0
  
    if (num % 2 == 1):
      middle = int(((num + 1) / 2) - 1)
    else:
      middle = int(num / 2)-1

    answer[middle] = average

    for i in range(middle-1, -1, -1):
      answer[i] = answer[i+1] - 1

    for i in range(middle+1, num, +1):
      answer[i] = answer[i-1] + 1
  
    return answer

print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))