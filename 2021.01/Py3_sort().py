#메소드 너무 어렵다

line = 'But soft what light through yonder window breaks'

#.split() 사용 시 : 별도 변수 필요
words = line.split()
# print(words) --> ['But', 'soft', 'what', 'light', 'through', 'yonder', 'window', 'breaks']
#line은 string이고, .split()은 list를 만드는 메소드여서 별도의 변수 필요

#그래서 아래의 방법은 안먹음...
line.split()
# print(line) --> But soft what light through yonder window breaks
# line은 string이어서, 그 안에 리스트를 저장할 수 없음
--------------------------------------------

#.sort() 사용 시 : 변수 필요 없음
#잘못된 방법
x = words.sort()
# print(x) --> None

#이렇게 써야함(ㅠㅜ)
words.sort()
# print(words) --> ['But', 'breaks', 'light', 'soft', 'through', 'what', 'window', 'yonder']

#리스트.sort() 는 리스트를 정렬하는 것(리스트 안에서 정렬만! 정렬해서 '원래의 리스트'에 다시 저장하는 셈)이어서 그냥 선언(?)만 해주면 됨
