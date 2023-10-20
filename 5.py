secret = "alloys"
guess_count = 1
guess_limit = 4
while guess_count < guess_limit:
    guess = input('guess my password : ')

    guess_count +=1
    if guess == secret.lower():
        print("you won")
        break
    else:
        print('sorry  try again')
else:
        print('sorry you failed')