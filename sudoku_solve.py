import numpy as np

# csv形式の数独を読み込み、空白部分は0としてnumpy配列に格納して返す関数


def read_sudoku(filename):
    # 欠損値(空白)を含むcsvファイルを読み込み、欠損値を0としてnumpy配列に格納する
    sudoku = np.genfromtxt(filename, delimiter=',', dtype=int, filling_values=0)
    return sudoku

# 最初の段階で空白であるセルを探す関数


def find_blank_cell_by_initial_state(sudoku):
    return(list(zip(*np.where(sudoku == 0))))

# セルの座標を受け取り、そのセルの数字が同じ行/列/ブロックの他の数字と被っていないか判定する関数 被っていなければTrue


def check_cell(sudoku, cell, written_number):
    if (written_number not in sudoku[cell[0]]) \
        and (written_number not in sudoku[:, cell[1]]) \
            and (written_number not in sudoku[cell[0]//3*3:cell[0]//3*3+3, cell[1]//3*3:cell[1]//3*3+3]):
        return True
    else:
        return False

# 総当たりを行い、セルに書き込める数字を探す関数

def solve_sudoku_brute_force(sudoku, unsolved_cells_tf):
    if len(unsolved_cells_tf) == 0:
        # すべてのセルが解決済みならば、数独パズルを表示して終了
        print(sudoku)
        return True

    # 未解決のセルのリストから次のセルを選択
    cell = unsolved_cells_tf[0]
    row, col = cell

    for num in range(1, 10):
        if check_cell(sudoku, cell, num):
            # セルに数字を書き込む
            sudoku[row, col] = num

            # 次の未解決のセルを解く
            if solve_sudoku_brute_force(sudoku, unsolved_cells_tf[1:]):
                return True

            # 解が見つからない場合、セルの数字をリセット
            sudoku[row, col] = 0

    return False



# メイン関数
def main():
    sudoku = read_sudoku("sudoku_sample.csv")
    print(sudoku)
    unsolved_cells_tf =find_blank_cell_by_initial_state(sudoku)  # まだ解かれていないセルのリスト
    if len(unsolved_cells_tf) == 0:
        print("この数独には空白のセルがありません")
        return
    solve_sudoku_brute_force(sudoku, unsolved_cells_tf)


if __name__ == '__main__':
    main()
