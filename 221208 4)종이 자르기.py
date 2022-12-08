def solution(M, N):
    answer = 0
    width = (M-1)
    height = M * (N-1)
    answer = width+height
    return answer #그냥 answer = (M * N) - 1도 됨

print(solution(2, 2))