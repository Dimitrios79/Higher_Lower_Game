from art import logo
from art import vs
from game_data import data
import random

print(logo)

A = random.choice(data)
B = random.choice(data)

x = A.get('name')
y = A.get('description')
r = A.get('country')
print(f"Compare A: {x}, a {y}, from {r}")

print(vs)

x = B.get('name')
y = B.get('description')
r = B.get('country')
print(f"Compare B: {x}, a {y}, from {r}")
score_A = A.get('follower_count')
score_B = B.get('follower_count')
select = input("Who has more followers? Type 'A' or 'B':")

