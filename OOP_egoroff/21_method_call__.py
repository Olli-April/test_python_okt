#method __call__

class Counter:
    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.lenght = 0
        print('init object, self')

    def __call__(self, *args, **kwargs):
        self.counter +=1
        self.summa += sum(args)
        self.lenght += len(args)
        print (f"наш экз. вызывался {self.counter} раз")

    def average(self):
        return self.summa / self.lenght

    # использование как декоратора

from time import perf_counter

class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self,*args, **kwargs):
        start = perf_counter()
        print(f"вызываеться функция {self.fn.__name__}")
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f"функция отработала за {finish - start}")
        return result

    @Timer
    def fact(n):
        pr = 1
        for i in range (1, n+1):
            pr *= i
        return pr
    def fib (n):
        if n<=2:
            return 1
        return fib(n-1) + fib(n_2)





