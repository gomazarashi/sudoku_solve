import numpy as np

#最初の段階で空白であるセルを探す関数
def find_blank_cell_by_initial_state(sudoku):
    return(list(zip(*np.where(sudoku == 0))))

def main():
    sudoku=np.zeros((9,9),dtype=int)
    unsolved_cells_tf=[[cell,True] for cell in list(find_blank_cell_by_initial_state(sudoku))] #まだ解かれていないセルのリスト 数字が0でなければTrue
    print(unsolved_cells_tf)


if __name__ == '__main__':
    main()