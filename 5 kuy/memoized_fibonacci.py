chache = {}

def fibonacci(n):
    def fibonacci_memoized(m):
        assert m >= 0
        if m in [0,1]:
            return m
        if m in chache:
            return chache[m]
        result = fibonacci_memoized(m - 1) + fibonacci_memoized(m - 2)
        chache[m] = result
        return result
    return fibonacci_memoized(n)
