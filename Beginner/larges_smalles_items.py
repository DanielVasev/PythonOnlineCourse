"""
How to extract larges ot smalles objects from a list

"""
import heapq

import heapq
grades = [32,43,654,34,132,66,99,532]
names = ["Daniel", "Roky", "Pena", "Niki", "Amalia"]


largest_three_graders = []
largest_three_graders = heapq.nlargest(3, grades)
print(*largest_three_graders)