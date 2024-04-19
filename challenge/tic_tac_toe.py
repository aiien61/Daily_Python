# Game of noughts and crosses
import pprint
import random
import copy

board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

moves = copy.deepcopy(list(board.keys()))

def print_board():
    print(f"{board['top-L']}|{board['top-M']}|{board['top-R']}")
    print('-+-+-')
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']}")
    print('-+-+-')
    print(f"{board['low-L']}|{board['low-M']}|{board['low-R']}")


def setting() -> dict:
    roles = ['O', 'X']
    while True:
        try:
            player = input('Choose your role [O/X]: ')
            player = player.upper()
            if player not in roles:
                raise ValueError

            roles.remove(player)
            computer = roles.pop()
            break
        except ValueError:
            print(f'{player} is not accepted. Please choose again.')
    return {'player': player, 'computer': computer}


def check_balance(roles_setting) -> bool:
    counter = {}
    for role in board.values():
        if role == ' ':
            continue
        counter.setdefault(role, 0)
        counter[role] += 1

    if not counter:
        return True

    if counter[roles_setting['player']] == counter[roles_setting['computer']]:
        return True
    else:
        return False


def is_game_set(role) -> bool:
    if board['top-L'] == board['top-M'] == board['top-R'] == role:
        return True
    elif board['mid-L'] == board['mid-M'] == board['mid-R'] == role:
        return True
    elif board['low-L'] == board['low-M'] == board['low-R'] == role:
        return True
    elif board['top-L'] == board['mid-L'] == board['low-L'] == role:
        return True
    elif board['top-M'] == board['mid-M'] == board['low-M'] == role:
        return True
    elif board['top-R'] == board['mid-R'] == board['low-R'] == role:
        return True
    elif board['top-L'] == board['mid-M'] == board['low-R'] == role:
        return True
    elif board['low-L'] == board['mid-M'] == board['top-R'] == role:
        return True
    else:
        False


def play(roles_setting: dict):
    while True:
        if check_balance(roles_setting):
            print(f'Turn for {roles_setting["computer"]}')
            computer_move = random.choice(moves)
            moves.remove(computer_move)
            board[computer_move] = roles_setting['computer']
            print_board()
            if is_game_set(roles_setting['computer']):
                print("You lose!")
                break

        player_move = input(f'Your turn for {roles_setting["player"]}. Your move [top-/mid-/low- + L/M/R]? ')
        if player_move not in moves:
            print("You can't move on an occipied space!")
            continue
        moves.remove(player_move)
        board[player_move] = roles_setting['player']
        print_board()
        if is_game_set(roles_setting['player']):
            print("You win!")
            break
        

if __name__ == "__main__":
    player_setting = setting()
    play(player_setting)
