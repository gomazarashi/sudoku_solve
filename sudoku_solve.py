import numpy as np

#csv形式の数独を読み込み、空白部分は0としてnumpy配列に格納して返す関数
def read_sudoku(filename):
    sudoku = np.genfromtxt(filename, delimiter=',', dtype=int,filling_values=0)#欠損値(空白)を含むcsvファイルを読み込み、欠損値を0としてnumpy配列に格納
    return sudoku

#最初の段階で空白であるセルを探す関数
def find_blank_cell_by_initial_state(sudoku):
    return(list(zip(*np.where(sudoku == 0))))

def main():
    sudoku=read_sudoku("sudoku_sample.csv")
    print(sudoku)
    """unsolved_cells_tf=[[cell,True] for cell in list(find_blank_cell_by_initial_state(sudoku))] #まだ解かれていないセルのリスト 数字が0でなければTrue
    print(unsolved_cells_tf)"""


if __name__ == '__main__':
    main()