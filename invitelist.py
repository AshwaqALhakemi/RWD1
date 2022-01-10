
guestList = []
maxlstlen = 3
while len(guestList) < maxlstlen:
    invitedList = input('Please enter unless three names you want to invite them to party: ')
    guestList.append(invitedList)
print(guestList)
choice = input('Do you want to invite more people! yes/no: ')
if choice == 'yes':
    number_of_guset = int(input('Add number of people you want to invite: '))
    for i in range(number_of_guset):
        invitedList = input('Please the names of people you want to invite them to party: ')
        guestList.append(invitedList)


elif choice == 'no':
        print('You have been invite', len(guestList),"People")

print('Your Guest List is', guestList)

