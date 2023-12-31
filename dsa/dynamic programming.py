def fib_no_dp(n):
    if n == 2: return 1
    if n == 1: return 1
    return fib_no_dp(n-1) + fib_no_dp(n-2)

def fib_dp(n):

    # this cache will record all our previous calculations
    # so if we have calculated fib(x) before, we don't need to calculate it again, we can just get it from our cache
    cache = {}

    def fib(n):
        if n == 2: return 1
        if n == 1: return 1
        if (n-1) in cache:
            l = cache[n-1]
        else:
            cache[n-1] = fib(n-1)
            l = cache[n-1]
        if (n-2) in cache:
            r = cache[n-2]
        else:
            cache[n-2] = fib(n-2)
            r = cache[n-2]

        return l + r
    
    return fib(n)

print(fib_no_dp(10))
print(fib_dp(10))

print(fib_no_dp(40)) # this takes a long time
print(fib_dp(40))

# print(fib_no_dp(100)) # don't even bother running this unless u wanna crash ur computer
print(fib_dp(100))