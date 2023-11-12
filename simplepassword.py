while True: ## making the loop
    password = 'password' ## the password

    userpwd = input('password? > ') ## prompt to enter password
    if userpwd==password: # pass if correct 
        print('correct!')
        break
    if userpwd!=password: # loop if incorrect
        print('incorrect, try again!')

#github.com/