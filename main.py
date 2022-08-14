# import turtle
#
# def main():
#     x = turtle.Turtle()
#     x.penup()
#     x.goto(-150, -150)
#     x.pendown()
#     x.left(90)
#     for i in range(2):
#         for j in range(4):
#             x.right(90)
#             x.pendown()
#             x.forward(300)
#             x.right(180)
#             x.forward(300)
#             x.right(90)
#             x.penup()
#             x.forward(100)
#         x.backward(100)
#         x.right(90)
#
# main()
#
#
from turtle import Screen, Turtle
from numpy import random



N = 9  # N by N grid
LENGTH = 30  # each grid element will be LENGTH x LENGTH pixels

def grid(turtle, n, length):
    sign = 1
    for _ in range(2):

        for _ in range(n):
            turtle.forward(length * n)
            turtle.left(sign * 90)
            turtle.forward(length)
            turtle.left(sign * 90)
            sign = 0 - sign

        turtle.forward(length * n)
        [turtle.right, turtle.left][n % 2](90)
        sign = 0 - sign

# screen = Screen()
# yertle = Turtle()
#
# yertle.penup()
# yertle.goto(-N * LENGTH/2, -N * LENGTH/2)  # center our grid (optional)
# yertle.pendown()
#
# grid(yertle, N, LENGTH)
#
# screen.exitonclick()

#=================================


def removeNumber(i, j, table):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for element in table[i]:
        if element in numbers:
            numbers.remove(element)

    for row in table:
        if len(row) <= j:
            break
        if row[j] in numbers:
            numbers.remove(row[j])
    print(table)
    print(numbers)
    return numbers


table =[]

for i in range(9):
    table.append([])
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for j in range(9):
        randomNubmer = random.choice(removeNumber(i, j, table))
        table[i].append(randomNubmer)
        # numbers.remove(randomNubmer)

for row in table:
    print(row)

print('===')













