count = 0
range_count = 10
for_count = 0
run = True
while run:
    print("Hello Cycle")

while run:
   print("Step = ", count)
   count += 1

while count < range_count:
    print("Step =", count)
    count += 1

while count < range_count:
    print("Step =", count)
    count += 1
    if 3 == count:
        print("Step =", count, 'If body')

while run:
    print("Step =", count)
    count += 1
    if count == range_count:
        print("Stop count")
        break

for item in range(for_count, range_count):
    print("Step=", item)

for item in range(0,31):
    print("Step=", item)
    if item == 5:
        print("Item=", item)
    if item == 10:
        print("Item=", item)
    if item < 4:
        print("Item< ", item)
    if item >= 27:
        print("Item >=", item)

for item in range(0,range_count +1):
    print("Step=", item)
    if item == 7:
        inner_count = 0
        print("-- inner_count =", inner_count)
        for inner_item in range(0, item):
            print("-------- Inner_Step =", inner_item)


