# while loop with break and continue
print("\n\nWhile Loop with break and continue:")
count = 0
while count < 10:
    count += 1
    if count == 5:
        continue  # skip the rest of the loop when count is 5
    if count == 8:
        break     # break the loop when count is 8
    print(count, end=" ")
