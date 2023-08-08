phrase = str(input("Input phrase "))
def count (phrase_splitted):
    return (phrase_splitted.count('а'))
phrase_splitted = phrase.split()
counted = map (count, phrase_splitted)
list_counted = list(counted)
x = list_counted[0]
flag = True
for i in list_counted:
    if i != x:
        flag = False
if flag == True: 
    print("Парам пам-пам")
else:
    print("Пам парам")



