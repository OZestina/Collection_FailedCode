#와 오늘은 세개나 배움^^ㅠ
#https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3

#리스트는 sort()로 정렬하는데, string은 어떻게 정렬하지?
#답은 sorted(_)! --> _에 string을 넣으면 '글자 하나하나마다 정렬된 리스트가 나옴!'

#정렬 안하고 그냥 리스트로 만들고 싶은 경우에는 a(아무거나) = list(s) 하면 됨
#(파이선에서는 s = list(s) 로 해도되나, 문자열로 정의된 변수를 리스트화 하는게 안되는 언어가 있으니 이렇게 정리해둠)

#역순으로 정렬하려면 .reverse() 사용
#sorted 하면서 역순으로 바로 정렬하려면 sorted(리스트명, reverse=True) ㄱㄱ

#리스트를 다시 하나의 string으로 합치려면 join을 사용하는데, 이게 또 애매허다^^ㅠ
#리스트 사이에 넣고 싶은 것을 '' 사이에 넣고 (딱 붙이고 싶으면 아무것도 없이 진행ㄱㄱ) 괄호 안에 리스트를 넣으면 됨!


#구글링해서 배우고(^^아이씬나) 작성한 코드는 하기와 같고,
def solution(s):
    x = sorted(s)
    x.reverse()
    answer = ''.join(x)
    return answer 
    
#다른 분들 코드를 참고해 라인을 더 줄이면 아래처럼도 가능!
def solution(s):
    answer = ''.join(sorted(s, reverse=True))
    return answer
