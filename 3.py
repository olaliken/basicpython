command=""
started = False
while command != 'quit':
    command=input("Please enter your command").lower()
    if command=='start':
        if started:
            print("car already on")
        else:
            started = True
            print('car has started')
    elif command=='stop':
        if not started:
            print("car was already stopped")
        else:
            started= False
            print("car has stopped")
    elif command=='quit':
        break
    elif command=='help':
        print(
        """ 
start  for starting the car
stop  for stoping the car
quit   to end
        """)
    else:
        print("i can't get you please")
