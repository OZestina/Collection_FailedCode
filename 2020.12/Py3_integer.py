#왜 10은 2보다 작고 1보다 큰가요 (?)

#Coursera 강의 중 Programming for Everybody (Getting Started with Python)의 연습문제(assignment 5.2)를 풀다가 만난 돌부리!
#(Programming for Everybody는 Univ. of Michigan에서 제공하는 강의입니다)

#사용자가 'done'을 입력 할 때까지 사용자에게 숫자(정수)를 입력하라는 메시지를 반복적으로 표시하는 프로그램을 작성합니다.
#사용자가 'done'입력 시 가장 큰 숫자와 가장 작은 숫자를 print합니다.
#사용자가 유효한 숫자가 아닌 다른 것을 입력하면 try / except로 그것을 포착하고 적절한 메시지를 내고 숫자를 무시합니다.

#처음 쓴 코드
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    
    try:
        int(num)
    except:
        print("Invalid input")
        continue
        
    if largest is None:
        largest = num
    elif largest < num:
        largest = num
        
    if smallest is None:
        smallest = num
    elif smallest > num:
        smallest = num
        
print("Maximum is", largest)
print("Minimum is", smallest)

#문제에서 요구한 숫자였던 [7, 2, 10, 4] 입력 시, "Maximum is 7, Minimum in 10" print! 아니 왜?
#여러 수를 대입해 본 결과, 10이 1보다는 크고, 2보다는 작게 인식된다는 것을 발견! 유레카!!!
#하지만 왜???

#옆에서 게임하던 코딩요정이 말씀하시길 (게임: 블서 시즌2) "int(num)이 사용되는 데가 없다!"
#나: 아하! 그러면 line 20을 수정(num=int(num))하면 되겠네!
#코딩요정: 근데 그렇게 하면 num이 str인지 int인지 나중에 헷갈리니까. 이름을 다르게 해주는게 좋아.
#그래서 수정한 코드 ↓

largest = None
smallest = None
while True:
    str_num = input("Enter a number: ")
            
    if str_num == "done" : 
        break
    
    try:
        num = int(str_num)
    except:
        print("Invalid input")
        continue
        
    if largest is None:
        largest = num
    elif largest < num:
        largest = num
        
    if smallest is None:
        smallest = num
    elif smallest > num:
        smallest = num
    
print("Maximum is", largest)
print("Minimum is", smallest)

#이렇게 또 컴퓨터를 이해하는 하루가 저물어 갑니다
