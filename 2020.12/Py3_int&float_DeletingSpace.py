#Coursera 연습문제 6.5
#저장된 스트링 중 숫자만 뽑아내기!

text = "X-DSPAM-Confidence:    0.8475";

#1st try
a = text.find(' ')
b = text[a:]
int_num = b.lstrip()
num = float(int_num)
print(num)

#숫자만 발라내려고 앞의 띄어쓰기에 너무 집중한 나머지 띄어쓰기부터 찾아버림 (콜론 앞의 내용에 띄어쓰기가 있으면 못쓰는 방법ㅠ)
#숫자 앞의 띄어쓰기는 배운 strip 메소드로 없앤 나 자신 칭찬해^^ 하려고 했는데,
#이게 필요없는 과정이었다는 걸 곧 깨달음^^

#2nd try
a = text.find(':')
b = text[a+1:]
num = float(b)
print(num)

#1. ':'을 기준으로 잡아 find하면 더 나음(콜론 앞의 내용에 띄어쓰기가 있어도 쓸 수 있는 방법!)
#2. TIL) float()과 int()는 불필요한 띄어쓰기를 없애준다! (숫자로 변환하는 과정에서 문자열이 아닌 띄어쓰기는 무시해줌!) - 난 몰랐즹...
#3. line 20에서 num = int(b)로 하면 error남! (소순데 왜 정수함수쓰냐 그거지)
