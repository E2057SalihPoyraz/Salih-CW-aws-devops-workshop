def game():
    from random import choice
    weapons = {"rock" : "scissors", "scissors" : "paper", "paper" : "rock"}
    user_score = computer_score = 0
    while computer_score < 3 and user_score < 3:
        while True:
            user = (input("Please enter your weapon: ").lower())
            if user in list(weapons.keys()):
                print(user)
                break
            else:
                print("Your weapon should be one of 'rock', 'paper', and 'scissors'")
        computer = choice(list(weapons.keys()))
        print(computer)
        if weapons[user] == computer:
            user_score += 1
            print('User=', user_score)
        elif weapons[computer] == user:
            computer_score += 1
            print('Computer=', computer_score)
        else:
            print("tie - no one wins")
    if computer_score > user_score:
        winner = "Computer"
    else:
        winner = "User"
    return (f"User won {user_score} time(s) and computer won {computer_score} time(s) \n{winner} has won the game!")
            
print(game())