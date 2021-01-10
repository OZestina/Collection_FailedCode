# 안배운거 나오니까 헤멘다..ㅎㅎ
#오늘은 딕셔너리 배움! 지금까지 내 사전에 파이선 사전은 없었다, 이젠 있당

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

email = dict()

for line in handle:
    if line.startswith('From '):
        words = line.split()
        a = words[1]
        
        #From 으로 시작되는 문장의 두번째 단어(이메일주소)의 개수를 dictionary(email로 딕셔너리 미리 만들어둠)를 통해 세보자!
        #email의 a(key)에 1 추가
        #딕셔너리에 a가 없을 경우 원래 에러가 뜨는데, 하기의 방법으로 없었을 경우 디폴트 값을 0으로 해서 바로 진행 가능
        email[a] = email.get(a, 0) +1
        
bigword = None
bigcount = None

#딕셔너리.items()를 하면 key,value 값이 나옴! (정확하게는 key, value값으로 구성된 tuple list 생성)
#값이 두개여서 for과 in 사이에 두개의 값을 넣어줘야함!
for address,count in email.items():
    if bigcount == None or bigcount < count:
        bigword = address
        bigcount = count

print(bigword, bigcount)
