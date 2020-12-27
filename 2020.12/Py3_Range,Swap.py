#프로그래머스 코딩테스트 연습문제 [두 정수 사이의 합]

#파이선에서 두 값을 바꾸는 방법이 있었는데~~(swaping) 하면서 기억 못해서 결국 원초적인 방법으로(line 13~15) 작성

def solution(a, b):
    answer = 0

    if a == b:
        answer = a
    else:
        if a > b:
            c = b
            b = a
            a = c
        while b+1-a > 0:
            answer = answer + a
            a = a+1

    return answer
    
    
 #다른사람 코드 보고 수정한거(라고 쓰고 따라쓴거라고 읽는다 ><)
    
 def solution(a, b):
    if a > b: a,b = b,a
 return sum(range(a,b+1))
    
 #sum도 알고 있었고, range도 알고 있었다. 하지만 아는 것과 적용할 수 있는건 다른 것이지^^ㅎㅎ
