# Two-dimensional list ttt_board represents a 3x3 tic-tac-toe game board read from input. List ttt_board contains three lists, each representing a row. Each list has three elements representing the three columns on the board. Each element in the tic-tac-toe game board is 'x', 'o', or '-'.

# If all the elements at column index 2 are 'x', output 'Player x wins at column 2.' Otherwise, output 'Player x does not win at column 2.'

# Click here for examples
# Ex 1 (win): If the input is:
# o - x
# - - x
# - o x
# then the output is:

# Player x wins at column 2.
# Ex 2 (lose): If the input is:

# x o o
# - - x
# - - x
# then the output is:

# Player x does not win at column 2.
# Note: The logical test (a == 'x' and b == 'x' and c == 'x') returns True if a, b, and c are equal to 'x'. The logical test returns False otherwise.
game_board = [
  input().split(),
  input().split(),
  input().split()
]

if game_board[2][0] == "o" and game_board[2][1] == "o" and game_board[2][2] == "o":
    print('A win at row 2.')
else:
    print('No win at row 2.')

