#coding: utf-8
## 兔子问题：一个月成长，一个月生一对，一年多少？
def fib(n):
    if n<= 2:
        return 1
    else:
        return fib(n-1)+ fib(n-2)
       

fib1 = lambda n:1 if n<=2 else fib1(n-1)+ fib1(n-2)
if __name__ == '__main__':
    print[fib1(i) for i in range(12)]
    
    print[fib(i) for i in range(12)]
