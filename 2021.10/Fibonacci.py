#입력을 정수 n으로 박았을 때, n이하까지의 피보나치 수열을 출력하는 함수 만들기

#1st try
#수열출력까지 한 번에 되는 함수로 짰는데,
#0과 1을 입력하면 원하는대로 나오지 않았다...
#if문으로 0과 1 입력시 별도 배열 return을 해줄 수도 있었으나! 재귀 함수를 써보고자 하여
def fibonacci(n):
    farray = [0,1]
    while n > farray[len(farray)-1]:
        newNum = farray[len(farray)-1]+farray[len(farray)-2]
        if n>= newNum:
            farray.append(newNum)
        else:
            break
    return farray
print(fibonacci(4))         #[0, 1, 1, 2, 3]
print(fibonacci(0))         #[0, 1]
print(fibonacci(1))         #[0, 1]


#2nd try
#피보나치 수를 만드는 함수와 배열을 만들어서 return해주는 함수를 별도로 구성
def fib(n):                 #n번째 
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-2) + fib(n-1)

def fib2(n):
    result = []
    for i in range(n+2):    #0과 1 입력 시 [0,1,1] 부분이 잘 나오도록 n+2해줌
        if n >= fib(i):
            result.append(fib(i))
        else:
            break
    return result
print(fib2(0))          #[0]
print(fib2(1))          #[0, 1, 1]
print(fib2(2))          #[0, 1, 1, 2]
print(fib2(3))          #[0, 1, 1, 2, 3]
print(fib2(4))          #[0, 1, 1, 2, 3]
