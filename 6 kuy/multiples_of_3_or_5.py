def solution(number):
    numbers = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            numbers.append(i)
    return sum(numbers)
  
