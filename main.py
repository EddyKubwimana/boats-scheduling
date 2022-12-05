#greedy appraoch for boats to save people

people = [1,2,3,7,6,7]
people.sort()
boats = 0
start, end = 0, len(people)-1
limit = 7
while start<=end:
    if people[start]+people[end]<=limit:
        start+= 1
    boats += 1
    end -= 1
print(boats)
