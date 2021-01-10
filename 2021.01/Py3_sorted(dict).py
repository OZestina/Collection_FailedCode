#Dict의 key or value 값으로 sorting 하기!

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

time = dict()
for line in handle:
    if line.startswith('From '):
        a = line.split()
        b = a[5].split(':')
        c = b[0]
        time[c] = time.get(c, 0) + 1
        
#아래를 통해 time의 key 값으로 sorting된 tuple list가 생성돼 time에 저장된다
time = sorted(time.items())

#만약에 역순으로 sort하고 싶다면
#time = sorted(time.items(), Reverse=True)

#만약에 value 값으로 sort하고 싶다면 --> key와 value의 위치를 바꿔 저장해 sorting하면 됨!
'''
lst = []
for k,v in time.items():
    neworder = (v, k)
    lst.append(neworder)
lst = sorted(lst) #역순으로 정렬하고 싶을 경우 ',Reverse=True 추가
'''

for k,v in time:
    print (k,v)
