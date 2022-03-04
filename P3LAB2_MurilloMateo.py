user_service = (input('Enter desired auto service:\n'))

print ('You entered:', user_service)


if user_service == 'Oil change':
    
    print ('Cost of oil change: $35')

elif user_service == 'Tire rotation':
    
    print ('Cost of tire rotation: $19')
    
elif user_service == 'Car wash':
    
    print ('Cost of car wash: $7')
    
else:
    print ('Error: Requested service is not recognized')