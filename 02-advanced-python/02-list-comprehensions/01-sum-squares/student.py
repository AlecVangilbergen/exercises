# Write your code here
def sum_squares(ns):
    squares = []
    for n in ns:
        squares.append(n ** 2)
    return sum(squares)