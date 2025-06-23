#loop control statements

fruits = ['Guava','Cherry','Kiwi','Pea']

for fruit in fruits:
    if fruit == 'Kiwi':
        break #exit the loop if the kiwi is found
    print(fruit)

print()

for fruit in fruits:
    if fruit == 'Kiwi':
        continue #continue the loop if the kiwi is found
    print(fruit)

print()

for fruit in fruits:
    if fruit == 'Kiwi':
        pass#placeholder no action is needed for kiwi
    print(fruit)

#while loop

count= 0
while count < 5:
    print(count)
    count +-1

    if count == 3:
        break # exit the loop when the count is reached