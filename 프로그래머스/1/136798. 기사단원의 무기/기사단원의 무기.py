def solution(number, limit, power):
    wp_list = [0]*number
    wp_list[0] = 1
    for x in range(1, number+1) : #10만
        if wp_list[x-1] != 0 : 
            continue
        cnt = 0
        big = x
        for y in range(1, int(x**0.5)+1) :
            if y >= big :
                break
            if x % y == 0 and x / y != y: # 제곱수가 아닌 경우
                cnt += 2
                big = x / y
            elif x / y == y : # 제곱수인 경우
                cnt += 1
                
            if cnt > limit : # 배수는 모두 초과
                cnt = power
                for xx in range(x,number+1,x) :
                    wp_list[xx-1] = power
                break
                
        wp_list[x-1] = cnt
    answer = sum(wp_list)
    return answer