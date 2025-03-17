def solution(n, arr1, arr2):
    answer = [[" "]*n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            b1 = format(arr1[i],f'0{n}b')[j]
            b2 = format(arr2[i],f'0{n}b')[j]
            if  b1 == '1' or b2 == '1' :
                answer[i][j] = "#"
        answer[i] = "".join(answer[i])
    return answer