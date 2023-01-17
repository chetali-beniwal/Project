'''You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0], then grid[2][0], and so on,
 up to grid[8][0]. This will finish the first row, so then print a newline. Then your program should print grid[0][1], 
 then grid[1][1], then grid[2][1], and so on. The last thing your program will print is grid[8][5]'''
grid=[['.', '.', '.', '.', '.', '.'],['.', 'O', 'O', '.', '.', '.'],['O', 'O', 'O', 'O', '.', '.'],
 ['O', 'O', 'O', 'O', 'O', '.'],['.', 'O', 'O', 'O', 'O', 'O'],['O', 'O', 'O', 'O', 'O', '.'],['O', 'O', 'O', 'O', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],['.', '.', '.', '.', '.', '.']]
for a in range(6):
    for b in range(9):
        print(grid[b][a],end='')
    print()