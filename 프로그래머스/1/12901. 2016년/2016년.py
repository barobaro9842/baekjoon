def solution(a, b):
    ds = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = sum(months[:a-1]) + (b-1)
    answer = ds[day % 7]
    return answer