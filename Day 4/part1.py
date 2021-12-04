class Field:
    def __init__(self, number: int, checked: bool):
        self.number = number
        self.checked = checked

    def check(self):
        self.checked = True
class Board:
    def __init__(self, board_data: list[Field]):
        self.board = board_data

    def get_board(self):
        return [b.number for b in self.board]

    def try_check_field(self, number: int):
        for i in range(len(self.board)):
            if self.board[i].number == number:
                self.board[i].check()
                break

    def get_unchecked_fields(self):
        return [b.number for b in self.board if not b.checked]

    def check_bingo(self):
        for i in range(board_dimension):
            correct_in_row, correct_in_column = 0, 0
            for j in range(board_dimension):
                if self.board[i * board_dimension + j].checked:
                    correct_in_row += 1
                if self.board[i + j * board_dimension].checked:
                    correct_in_column += 1
            if correct_in_row == board_dimension or correct_in_column == board_dimension:
                return True
        return False

def get_score():
    for d in drawing:
        for board in boards:
            board.try_check_field(d)
            if(board.check_bingo()):
                return sum(board.get_unchecked_fields()) * d

with open('input.txt', 'r') as file:
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

print(f"Score: {get_score()}")