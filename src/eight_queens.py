# -*- coding: utf-8 -*-
"""
八皇后问题求解器
使用回溯法求解8x8棋盘的所有合法解
"""

def is_valid(board, row, col):
    """
    检查在(row, col)位置放置皇后是否合法
    :param board: 列表，索引为行，值为列（-1表示该行未放置）
    :param row: 当前要放置的行
    :param col: 当前要放置的列
    :return: 布尔值，是否合法
    """
    # 检查同列
    for r in range(row):
        if board[r] == col:
            return False
    # 检查对角线
    for r in range(row):
        if abs(r - row) == abs(board[r] - col):
            return False
    return True

def backtrack(board, row, solutions):
    """
    回溯法求解八皇后
    :param board: 列表，索引为行，值为列
    :param row: 当前处理到的行
    :param solutions: 存储所有解的列表
    """
    n = len(board)
    if row == n:
        solutions.append(board.copy())
        return
    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            backtrack(board, row + 1, solutions)
            board[row] = -1  # 回溯

def get_all_solutions():
    """
    获取八皇后问题的所有解
    :return: 列表，每个解是长度为8的列表，索引代表行，值代表列
    """
    n = 8
    board = [-1] * n
    solutions = []
    backtrack(board, 0, solutions)
    return solutions

def print_board(solution):
    """
    可视化打印棋盘
    :param solution: 单个解（长度为8的列表）
    """
    n = len(solution)
    for row in range(n):
        line = []
        for col in range(n):
            if solution[row] == col:
                line.append("♛")
            else:
                line.append(".")
        print(" ".join(line))

if __name__ == "__main__":
    solutions = get_all_solutions()
    print(f"总解数: {len(solutions)}")
    if solutions:
        print_board(solutions[0])