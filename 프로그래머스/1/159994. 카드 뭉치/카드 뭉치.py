def solution(cards1, cards2, goal):
    c1 = 0
    c2 = 0
    for i in range(len(goal)) :
        if c1 < len(cards1) and cards1[c1] == goal[i] :
            c1 += 1
        elif c2 < len(cards2) and cards2[c2] == goal[i] :
            c2 += 1
        else :
            answer = "No"
            break
    else :
        answer = "Yes"
    return answer