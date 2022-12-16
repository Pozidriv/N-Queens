#!/usr/bin/env python3
# Computes number of solutions for the n queens on a chess board

import numpy as np

n=8 # Size of nxn chess board (default is 8, smaller values for debug)
solution_no=0 # Number of solutions (incremented as we find them)

allowed_cells={} # Dictionary of allowed cells
current_board={} # Dictionary of current pieces on the board
# Populate allowed cells (i: rows, j: columns)
for i in range(n):
  for j in range(n):
    allowed_cells.update({n*i + j: "(" + str(i) + "," + str(j) + ")"})
  # End j loop
# End i loop

# Checks that coordiates (row,col) are in range of grid
def check_range(row,col):
  if row>n-1 or row <0 or col>n-1 or col <0:
    return False
  return True

# Recursive backtracking function
def check_position(row=0, col=0):
  global solution_no
  #print(str(row) + "," + str(col))
  #print(allowed_cells)
  if row==n-1: # Found a solution
    solution_no+=1
    for cell in current_board:
      print(current_board[cell], end = " ")
    print(" ")
    return

  # End if

  forbidden_positions={row*n + col: "(" + str(row) + "," + str(col) + ")"} # positions that a piece in cell (row,col) attacks

  # Forbidden positions for a QUEEN
  for i in range(n):
    forbidden_positions.update({i*n + col: "(" + str(i) + "," + str(col) + ")"}) # Row
    forbidden_positions.update({row*n + i: "(" + str(row) + "," + str(i) + ")"}) # Column
    # UL: upper left, DR: down right, etc...
    row_diagUL=row-i
    col_diagUL=col-i
    row_diagUR=row-i
    col_diagUR=row+i
    row_diagDL=row+i
    col_diagDL=col-i
    row_diagDR=row+i
    col_diagDR=col+i
    if check_range(row_diagUL, col_diagUL):
      forbidden_positions.update({row_diagUL*n + col_diagUL: "(" + str(row_diagUL) + "," + str(col_diagUL) + ")"}) # Column
    if check_range(row_diagUR, col_diagUR):
      forbidden_positions.update({row_diagUR*n + col_diagUR: "(" + str(row_diagUR) + "," + str(col_diagUR) + ")"}) # Column
    if check_range(row_diagDL, col_diagDL):
      forbidden_positions.update({row_diagDL*n + col_diagDL: "(" + str(row_diagDL) + "," + str(col_diagDL) + ")"}) # Column
    if check_range(row_diagDR, col_diagDR):
      forbidden_positions.update({row_diagDR*n + col_diagDR: "(" + str(row_diagDR) + "," + str(col_diagDR) + ")"}) # Column
      
  # End row/colum loop
  #for i in range(n- abs(row-col)):
    # Diagonal
    #start_row=row-min(row,col)
    #start_col=col-min(row,col)
    #current_row=start_row+i
    #current_col=start_col+i
    #forbidden_positions.update({current_row*n + current_col: "(" + str(current_row) + "," + str(current_col) + ")"}) # Diagonal
  # End diagonal loop
  #for i in range(min(n-1-row,col) + min(n-1-col, row)+1): # Reverse diagonal
    #start_row=row-min(n-1-row, col)
    #start_col=col+min(n-1-row, col)
    #current_row=start_row+i
    #current_col=start_col+i
    #forbidden_positions.update({current_row*n + current_col: "(" + str(current_row) + "," + str(current_col) + ")"}) # Reverse Diagonal
  # End reverse diagonal loop

  # Remove forbidden cells from allowed positions
  new_forbidden={} # newly forbidden cells by position (row,col)
  for cell in forbidden_positions:
    if cell in allowed_cells:
      new_forbidden.update({cell: allowed_cells[cell]})
      allowed_cells.pop(cell)
    # End if
  # End cell loop
  #print("Forbidden: " + str(new_forbidden))
  
  # if no more allowed cells, backtrack
  if allowed_cells=={}:
    # add newly forbidden cells back before returning
    for cell in new_forbidden:
      allowed_cells.update({cell: new_forbidden[cell]})
    return
  else:
    for i in range(n):
      if (row+1)*n + i in allowed_cells: # iterating over rows
        current_board.update({(row+1)*n + i: "("+str(row+1)+","+str(i)+")" })
        check_position(row+1, i)
        current_board.pop((row+1)*n + i)
      # End if
    # End column loop
  # End else

  # add newly forbidden cells back before returning
  for cell in new_forbidden:
    allowed_cells.update({cell: new_forbidden[cell]})
# End check_position()

print("n = "+str(n))

for i in range(n): # iterating over columns
  #print(str(i) + ": " + str(solution_no))
  current_board.update({i: "(0,"+str(i)+")" })
  check_position(0, i)
  current_board.pop(i)

print("Number of solutions: "+str(solution_no))

