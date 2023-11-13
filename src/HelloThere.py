'''
Created on Nov 12, 2023

@author: walte
'''
print("Hello There")

nbrs = {3, 5, 6, 8, 12, 14}

sum = 0
for i in nbrs :
    sum += i

avg = sum / len(nbrs)
print(f"sum {sum}  average: {avg}")
