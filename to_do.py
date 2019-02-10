li = []
print('The TO-DO LIST. PRESS a to ADD, d to DELETE and q TO QUIT')
g = True
while g:
    #Taking User input what do they want to do
    choice = input('choice? ')
    #Adding items to the list
    while choice == 'a':
        n = input('--> ')
        if n == 'q':
            break
        else:
            li.append(n)
    #Sorting the list        
    if choice == 's':
        li.sort()
    #Removing items from the list
    while choice == 'd':
        n = input('--> ')
        if n == 'q':
            break
        else:
            li.remove(n) 
    #Getting out of the loop and finishing the to-do list        
    done = input('continue?(y/n) ')
    if done == 'n':
        g = False
        
count = 0
print('The TO-DO LIST :')
for j in li:
    count += 1
    print(str(count) + '. ' + j)