def solution(s):
    answer = []
    dic = dict()
    for i,x in enumerate(s) :
        if dic.get(x,-1) == -1 :
            answer.append(-1)
            dic[x] = i
        else :
            answer.append(i-dic[x])
            dic[x] = i
    return answer