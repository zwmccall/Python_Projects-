"""
Author: Pranav Goel
Takes user's name as input and returns a random type of house they'll have when they grow up.
"""


import random

future = ['bungalow','mansion','villa']

name = input("What is your name?\n")

num = random.random()%3

print(name,", you'll have a ",future[int(num)]," when you grow up! :)")