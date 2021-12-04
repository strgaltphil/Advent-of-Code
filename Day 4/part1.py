class Field:
    def __init__(self, number: int, checked: bool):
        self.number = number
        self.checked = checked

    def check(self):
        self.checked = True

    def __str__(self):
        if self.checked:
            return f"({self.number})"
        else:
            return str(self.number)


class Board:
    def __init__(self, board_data: list[Field]):
        self.board = board_data

    def get_board(self):
        return self.board

    def try_check_field(self, number: int):
        for i in range(len(self.board)):
            if self.board[i].number == number:
                self.board[i].check()
                break

    def get_unchecked_fields(self):
        return [b.number for b in self.board if not b.checked]

    def get_checked_fields(self):
        return [b.number for b in self.board if b.checked]

    def check_bingo(self):
        def check_lines_horizontal():
            for i in range(board_dimension): # row
                for j in range(board_dimension): # column
                    if not self.board[i * board_dimension + j].checked:
                        return False                    
            return True

        # def check_lines_vertical():
        #     for i in range(board_dimension): # column
        #         for j in range(board_dimension): # row
        #             if not self.board[i + j * board_dimension].checked:
        #                 return False
        #     return True

        # def check_lines_diagonal():
        #     for i in range(board_dimension): # top left to bottom right
        #         if not self.board[i * board_dimension + i].checked:
        #             return False

        #     for i in range(board_dimension): # bottom left to top right
        #         if not self.board[(board_dimension - i - 1) + i * board_dimension].checked:
        #             return False

        #     return True

        return check_lines_horizontal() #or check_lines_vertical() or check_lines_diagonal()

with open('/Users/philipp/Desktop/Advent of Code/Day 4/input_test.txt', 'r') as file:
    data = [line for line in file.read().split('\n')]

board_dimension = 5

# remove whitespace lines
data = [d for d in data if str(d) != '']

# split drawing and board data
drawing = [int(d) for d in data[0].split(',')]
raw_boards = data[1:]

boards = []

for i in range(len(raw_boards) // 5):
    tmp_board = []
    for j in range(board_dimension):
        # One single Field includes first the field vaule, second if it got checked already
        tmp_board.extend([Field(int(rb), False) for rb in raw_boards[i * board_dimension + j].split()])

    boards.append(Board(tmp_board))

winner_board: Board = None

def get_score(draw):
    for d in draw:
        for board in boards:
            board.try_check_field(d)
            if board.check_bingo():
                print(board.get_checked_fields())
                return "Bingo"

            print(board.get_checked_fields())

        print("-----------------------------------------------")
print(f"score: {get_score(drawing)}")






# test = [('23', False), ('1', False), ('53', False), ('65', False), ('30', False), ('45', False), ('15', False), ('9', False), ('26', False), ('28', False), ('2', False), ('21', False), ('42', False), ('27', False), ('12', False), ('84', False), ('68', False), ('71', False), ('19', False), ('13', False), ('58', False), ('57', False), ('35', False), ('77', False), ('14', False)]

# print((boards))