
def findValues(values, target):
    if target>1:
        val_dict = {}
        for val in values:
            if val in val_dict:
                val_dict[val] +=1
            else:
                val_dict[val] = 0

        for val in values:
            target_compliment = target - val
            if target_compliment in val_dict:
                if target_compliment == val:
                    if not val_dict[target_compliment] > 0:
                        continue
                print(str(val) + " and " + str(target_compliment))
                return str(val) + " and " + str(target_compliment)
    return "No valid pairs"

print(findValues([14, 13, 6, 7, 8, 10, 1, 2], 3) == "1 and 2")


