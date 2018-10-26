from random import shuffle

list_of_groups = []
prioritet = []
with open("file.csv", "r") as file:
    for line in file:
        temp = line[:-1].split(",")
        prioritet.append(temp[0])
        ar = []
        for item in temp:
            if item != "":
                ar.append(item)
        if len(ar) != 0:
            list_of_groups.append(ar)


inGroup3 = []
inGroup2 = []
inGroup1 = []

for item in list_of_groups:
    if len(item) == 3:
        print(str(item) + " - 3")
        added = False
        for val in prioritet:
            if val == item[1]:
                print("Removed -> " + str(item[1]))
                if val == item[2]:
                    print("Removed -> " + str(item[2]))
                    # item.remove(item[1])
                    inGroup1.append(item[0])
                    added = True
                else:
                    inGroup2.append([item[0], item[2]])
                    added = True
            elif val == item[2]:
                print("Removed -> " + str(item[2]))
                # item.remove(item[2])
                inGroup2.append([item[0], item[1]])
                added = True
        if not added:
            inGroup3.append(item)
    if len(item) == 2:
        print(str(item) + " - 2")
        added = False
        for val in prioritet:
            if val == item[1]:
                print("Removed -> " + str(item[1]))
                # item.remove(item[1])
                inGroup1.append(item[0])
                added = True
        if not added:
            inGroup2.append(item)
    if len(item) == 1:
        print(str(item) + " - 1")
        inGroup1.append(item)

# print(inGroup1)
shuffle(inGroup1)
# print(inGroup1)

# print(inGroup2)
shuffle(inGroup2)
# print(inGroup2)

# print(inGroup3)
shuffle(inGroup3)
# print(inGroup3)


def zapolnenie(group, chislo_comand):
    k = comands.index(min(comands, key=len))
    for item in group:
        for each in item:
            comands[k].append(each)
        k = comands.index(min(comands, key=len))


comands = []
chislo_comand = 6
for i in range(chislo_comand):
    comands.append([])
zapolnenie(inGroup3, chislo_comand)
zapolnenie(inGroup2, chislo_comand)
zapolnenie(inGroup1, chislo_comand)

with open("out.csv", "w") as file:
    k = len(max(comands, key=len))
    for j in range(k):
        for i in range(chislo_comand):
            if len(comands[i]) > j:
                file.write(str(comands[i][j]) + ",")
            elif len(comands[i]) == j + 1:
                file.write(str(comands[i][j]))
        file.write("\n")

















