#Nathan Li - Tic Tac Toe - 5/2/2021
#Adapted from https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874

gameBoard = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' ',}

board_keys = []

for key in gameBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def play():
    turn = 'X'
    count = 0

    for i in range(9): #The game can only ever take a max of 9 turns to complete
        printBoard(gameBoard)
        print("It's your turn, " + turn + ". Choose your move:")

        move = input()

        if gameBoard[move] == ' ':
            gameBoard[move] = turn
            count += 1
        else:
            print("That move is already taken. Choose your move:")
            continue

        if count >= 5: #Only possible to win on/after the fifth turn
            if gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ': #Top row win
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ': #Middle row win
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ': #Bottom row win
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['7'] == gameBoard['4'] == gameBoard['1'] != ' ': #Left column win
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['8'] == gameBoard['5'] == gameBoard['2'] != ' ': #Middle column win
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['9'] == gameBoard['6'] == gameBoard['3'] != ' ': #Right column win
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['7'] == gameBoard['5'] == gameBoard['3'] != ' ': #L->R diagonal win
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif gameBoard['9'] == gameBoard['5'] == gameBoard['1'] != ' ': #:L<-R diagonal win
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        if count == 9:
            print("\nGame Over\n")
            print("It's a Tie!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do you want to play Again?(y/n):")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            gameBoard[key] = " "

        play()

if __name__ == "__main__":
    play()