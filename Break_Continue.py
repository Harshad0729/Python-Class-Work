# Use of break and continue
'''
for i in range(1,21):
    if(i == 10):
        break
    print(i)
print("-----------------")
'''
for i in range(1,21):
    if(i == 10):
        print("Skipped")
        continue
    print(i)