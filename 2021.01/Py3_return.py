
arr = [1, 1, 3, 3, 0, 1, 1]

def solution(arr):
    answer = []
    arr_count = -1
    for a in arr:
        if len(answer) == 0:
        #이실직고) 여기서 if len(answer) = 0: 으로 작성해서 계속 오류떴었다^^ '='은 대입, '=='가 equal임을 잊지맙시당!
            answer.append(a)
        else:
            if a is not answer[len(answer)-1]:
                answer.append(a)
                print(answer)
            else:
                print(answer)
                continue
    return answer

print(answer)

#line19에서 answer 값이 정의되지 않았다고 계속 뜸
#아니 answer 저기 있잖아ㅠㅠ
#그러다가 깨달음

print(solution(arr))

#라고 해야 나옵니다.....ㅎㅎ
#사족) def solution 안에서 return된 answer는 'answer'로서 존재하는 것이 아닌 'solution()'함수로서 존재하는것!
#연초부터 지독하게 껍질깨기^^ 아 됴타

