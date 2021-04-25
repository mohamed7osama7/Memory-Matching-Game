import random
N = 4
grid = [["?" for i in range(N)] for j in range(N)]
uncovered = [[0 for i in range(N)] for j in range(N)]
score = [0, 0]


def print_grid():
    print('-' * ((N + 4) * N + N + 1))
    for i in range(N):
        print(end='|')
        for j in range(N):
            str_len = len(str(grid[i][j]))
            r1 = ((N + 4) - str_len + 1) // 2
            r2 = ((N + 4) - str_len) - r1
            e = (' ' * r1) + str(grid[i][j]) + (' ' * r2)
            print(e, end='|')
        print()
        print('-' * ((N + 4) * N + N + 1))


def generate_cell():
    score[0]=0
    score[1]=0
    my_list = ["A", "A", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F", "G", "G", "H", "H"]
    for i in range(N):
        for j in range(N):
            rand_index = random.randint(0, len(my_list)-1)
            uncovered[i][j] = my_list[rand_index]
            del my_list[rand_index]

def check_tie():
    if score[0]==4 and score[1]==4:
        return True
    return False

def is_valid_position(i,j,k,l):
    if (0>i or i>3):
        return False
    if (0>j or j>3):
        return False
    if (0>k or k>3):
        return False
    if (0>l or l>3):
        return False
    return True


def uncover_cells(i, j, k, l):
    grid[i][j] = uncovered[i][j]
    grid[k][l] = uncovered[k][l]
    print_grid()
    if uncovered[i][j] != uncovered[k][l]:
        grid[i][j] = "?"
        grid[k][l] = "?"
        print("sorry... your guess is wrong \n")
        return False
    else:
        print("your guess is right")
        return True

def grid_clear():
    for i in range (N):
        for j in range (N):
            grid [i][j]='?'


def play_game():
    print("memory Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:

        print("player %s turn" % player)
        print_grid()

        i, j = map(int, input('Enter the row index and column index for the first cell: ').split())
        k, l = map(int, input('Enter the row index and column index for the second cell: ').split())

        while not is_valid_position(i,j,k,l) or grid[i][j] != "?" or grid[k][l] != "?" or ((i==k) and (j==l)) :
            print("enter valid cells")
            i, j = map(int, input('Enter the row index and column index for the first cell: ').split())
            k, l = map(int, input('Enter the row index and column index for the second cell: ').split())


        if uncover_cells(i, j, k, l):
            score[player] += 1
            print("player %s score is %s\n" % (player, score[player]))

        if score[player] == 5:
            print("player %s won" % player)
            break

        if check_tie():
            print("its a tie")
            break

        player = 1 - player


while True:
    grid_clear()
    generate_cell()
    play_game()
    c = input('Play Again [Y/N] ')
    if c not in 'yY':
        break



