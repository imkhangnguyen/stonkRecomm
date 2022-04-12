import sentiment_check as sen

companylist = ['Apple', 'Telsa', 'Nvidia']
companyscore =['10','-24','99']
D = dict(zip(companylist, companyscore))

def get_key(val):
    for key, value in D.items():
         if val == value:
             return key
 
    return "key doesn't exist"
queue = []
for item in companylist:
    queue.append(D[item])
print("\nInitialize queue")
print(queue)

print("\nPop")
for item in companylist:
    score = queue.pop(0)
    print(get_key(score))