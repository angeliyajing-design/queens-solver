def solve_n_queens(n: int) -> list[list[str]]:
    """
    求解 N 皇后问题，返回所有合法的棋盘布局
    :param n: 棋盘大小
    :return: 所有合法布局的列表，每个布局是一个字符串列表
    """
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]

    def is_valid(row: int, col: int) -> bool:
        # 检查列
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # 检查左上到右下对角线
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 检查右上到左下对角线
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def backtrack(row: int) -> None:
        if row == n:
            solution = [''.join(row) for row in board]
            result.append(solution)
            return
        for col in range(n):
            if is_valid(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'  # 回溯

    backtrack(0)
    return result
