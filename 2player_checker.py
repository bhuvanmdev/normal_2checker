from os import system
class Checkers:
    def __init__(self):
        self.board = [[' * ', 'w09', ' * ', 'w10', ' * ', 'w11', ' * ', 'w12'],
                      ['w05', ' * ', 'w06', ' * ', 'w07', ' * ', 'w08', ' * '],
                      [' * ', 'w01', ' * ', 'w02', ' * ', 'w03', ' * ', 'w04'],
                      [' * ' for _ in range(8)],
                      [' * ' for _ in range(8)],
                      ['b01', ' * ', 'b02', ' * ', 'b03', ' * ', 'b04', ' * '],
                      [' * ', 'b05', ' * ', 'b06', ' * ', 'b07', ' * ', 'b08'],
                      ['b09', ' * ', 'b10', ' * ', 'b11', ' * ', 'b12', ' * ']]
        self.wpos = {'w01': [2, 1], 'w02': [2, 3], 'w03': [2, 5], 'w04': [2, 7],
                     'w05': [1, 0], 'w06': [1, 2], 'w07': [1, 4], 'w08': [1, 6],
                     'w09': [0, 1], 'w10': [0, 3], 'w11': [0, 5], 'w12': [0, 7]}
        self.bpos = {'b01': [5, 0], 'b02': [5, 2], 'b03': [5, 4], 'b04': [5, 6],
                     'b05': [6, 1], 'b06': [6, 3], 'b07': [6, 5], 'b08': [6, 7],
                     'b09': [7, 0], 'b10': [7, 2], 'b11': [7, 4], 'b12': [7, 6]}
        self.mov = 0

    def print_board(self):
        print('   ', end='')
        [print(f' {x}    ', end='') for x in range(8)]
        print()
        for num, x in enumerate(self.board):
            print(num, ' ', end='')
            print(' | '.join(x), '-' * 50, sep='\n')

    def remover(self, color, loc):
        pos = self.wpos if color in ('b', 'B') else self.bpos
        if loc in pos.values():
            _ = [(pawn := x) for x, y in pos.items() if pos[x] == loc]
            pos.pop(pawn)
            self.board[loc[0]][loc[1]] = ' * '
            return True
        return False

    def mover(self, name, to):
        pos = self.bpos if name[0] in ('b', 'B') else self.wpos
        fx, fy = pos[name]
        tx, ty = to
        if (tx == 7 and name[0] == 'w') or (tx == 0 and name[0] == 'b'):
            pos[(name := name[0].upper() + name[1:])] = pos.pop(name)
            k.mov -= 1
        pos[name] = to
        self.board[fx][fy] = ' * '
        self.board[tx][ty] = name
        return True

    def pawn(self, name, to):
        color = name[0]
        sign, pos, opp_pos = (-1, self.bpos, self.wpos) if color in ('b', 'B') else (1, self.wpos, self.bpos)
        fx, fy = pos.get(name, [-1, -1])
        tx, ty = to
        if fx == fy == -1 or not (0 <= tx <= 7 and 0 <= ty <= 7):
            return False
        tot = [sign] if color in ('b', 'w') else [sign, -sign]
        for sign in tot:
            if tx == fx + sign and (ty == fy - 1 or ty == fy + 1):
                if to not in (tuple(opp_pos.values()) + tuple(pos.values())):
                    return self.mover(name, to)
            elif tx == fx + 2 * sign and (ty == fy - 2 or ty == fy + 2):
                if [(tx+fx)//2,(ty+fy)//2 ] in opp_pos.values() and self.remover(color,[(tx+fx)//2,(ty+fy)//2]) and self.mover(name,to):
                    return self.surround_checker(name)
        return False

    def sorter(self, name, to):
        if len(name) != 3:
            return False
        if name[0] in ('w', 'b', 'W', 'B'):
            return self.pawn(name, to)
        else:
            return False

    def surround_checker(self, pawn):
        mul = 0
        color = pawn[0]
        sign, opp_pos, pos = (-1, self.wpos, self.bpos) if color in ('b', 'B') else (1, self.bpos, self.wpos)
        fx, fy = pos.get(pawn, [-1, -1])
        to = -1
        # if king is there
        if fx == fy == -1:
            fx, fy = pos[(pawn := pawn[0].upper() + pawn[1:])]
        opp_val = opp_pos.values()
        li = [[fx + sign, fy - 1], [fx + sign, fy + 1]]
        li = li if color in ('b', 'w') else li + [[fx - sign, fy - 1], [fx - sign, fy + 1]]
        for x, y in li:
            if [x, y] in opp_val:
                tx, ty = [fx + 2 * (x - fx), fy + 2 * (y - fy)]
                if 0 <= tx <= 7 and 0 <= ty <= 7 and self.board[tx][ty] == ' * ':
                    mul += 1
                    to = [tx, ty]
        if mul == 0:
            return True
        elif mul != 1:
            to = input(f'there are {mul} ways give the pos: ').split()
            while len(to) != 2 or len(to[0]) != len(to[1]) != 1 or (to[0] and to[1]) not in map(str, range(
                    8)):
                to = input(f'there are {mul} ways give the pos: ').split()
            to = list(map(int, to))
        return self.pawn(pawn,to)

    def game_over(self,color):
        pos = self.wpos if color in ('b','B') else self.bpos
        return f'{color} wins' if len(pos) == 0 else False

if __name__ == '__main__':
    game = Checkers()
    chance = ['b','w']
    while True:
        game.print_board()
        if len(name:=input('name: ')) == 3 and name[0].lower() == chance[game.mov%2]:
            to = input('pos: ').split()
            if len(to) != 2 or len(to[0]) != len(to[1]) != 1 or (to[0] and to[1]) not in map(str, range(8)):
                continue
            to = list(map(int, to))
            if k.sorter(name, to):
                res = game.game_over(name[0])
                game.mov += 1
                system('cls')
                if res:
                    game.print_board()
                    print(res)
                    break
            else:
                print('illegal move brotohoror')
        else:
            print(f'give a valid name boother\n its {chance[game.mov%2]} chance')

def spare_comments():pass
'''
#                 if [fx + sign, fy - 1] in opp_pos.values():
#                     if self.remover(color, [fx + sign, fy - 1]) and self.mover(name, to):
#                         return self.surround_checker(name)
#                 elif [fx + sign, fy + 1] in opp_pos.values():
#                     if self.remover(color, [fx + sign, fy + 1]) and self.mover(name,to):
#                         return self.surround_checker(name)
'''
