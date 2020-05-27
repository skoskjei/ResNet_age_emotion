
# To make sure the Multi-label binarizer is consistent for all variation use of data

AGE_CATEGORIES = 26
EMOTION_CATEGORIES = 2

possible_sol = []
for i in range(1,AGE_CATEGORIES + 1):
    for j in range(EMOTION_CATEGORIES):
        if len(str(i)) < 2:
            i = '{:02}'.format(i)
        possible_sol.append(str(i) + '_' + str(j))

print(possible_sol)

f = open("all_categories.txt", "w")
for sol in possible_sol:
    f.write(sol + '\n')
f.close()