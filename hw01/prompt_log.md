# AI 协作日志：八皇后问题工程化实践

## 1. 项目初始化阶段

### 1.1 需求描述
> **用户 Prompt**：
> 我需要创建一个标准的 Python 工程目录结构，用于解决八皇后问题。请帮我生成一个包含 `src/`（源码目录）和 `tests/`（测试目录）的项目骨架，并创建必要的 `__init__.py` 文件和 `README.md` 模板。

### 1.2 AI 响应
> **AI 输出**：
> 好的，这是一个标准的 Python 项目结构，你可以直接使用：
> ```
> hw01/
> ├── src/
> │   ├── __init__.py
> │   └── queens.py
> ├── tests/
> │   ├── __init__.py
> │   └── test_queens.py
> ├── README.md
> └── requirements.txt
> ```
> 我还为你生成了 `README.md` 的模板内容，你可以根据需要修改。

---

## 2. 算法实现阶段

### 2.1 需求描述
> **用户 Prompt**：
> 请用 Python 实现一个 N 皇后问题的求解器，使用回溯法。函数名定义为 `solve_n_queens(n: int) -> list[list[str]]`，输入是棋盘大小 `n`，输出是所有合法的棋盘布局，每个布局是一个字符串列表，其中 'Q' 代表皇后，'.' 代表空位。代码需要符合 PEP8 规范，并包含详细的类型注解和注释。

### 2.2 AI 响应
> **AI 输出**：
> 这是一个使用回溯法实现的 N 皇后求解器：
> ```python
> def solve_n_queens(n: int) -> list[list[str]]:
>     """
>     求解 N 皇后问题，返回所有合法的棋盘布局
>     :param n: 棋盘大小
>     :return: 所有合法布局的列表，每个布局是一个字符串列表
>     """
>     result = []
>     board = [['.' for _ in range(n)] for _ in range(n)]
> 
>     def is_valid(row: int, col: int) -> bool:
>         # 检查列
>         for i in range(row):
>             if board[i][col] == 'Q':
>                 return False
>         # 检查左上到右下对角线
>         i, j = row - 1, col - 1
>         while i >= 0 and j >= 0:
>             if board[i][j] == 'Q':
>                 return False
>             i -= 1
>             j -= 1
>         # 检查右上到左下对角线
>         i, j = row - 1, col + 1
>         while i >= 0 and j < n:
>             if board[i][j] == 'Q':
>                 return False
>             i -= 1
>             j += 1
>         return True
> 
>     def backtrack(row: int) -> None:
>         if row == n:
>             solution = [''.join(row) for row in board]
>             result.append(solution)
>             return
>         for col in range(n):
>             if is_valid(row, col):
>                 board[row][col] = 'Q'
>                 backtrack(row + 1)
>                 board[row][col] = '.'  # 回溯
> 
>     backtrack(0)
>     return result
> ```

---

## 3. 单元测试阶段

### 3.1 需求描述
> **用户 Prompt**：
> 请为上面的 `solve_n_queens` 函数编写单元测试，使用 `unittest` 框架。需要验证 N=4 时有 2 种解，N=8 时有 92 种解。

### 3.2 AI 响应
> **AI 输出**：
> 这是对应的单元测试代码：
> ```python
> import unittest
> from src.queens import solve_n_queens
> 
> class TestNQueens(unittest.TestCase):
>     def test_4_queens(self):
>         solutions = solve_n_queens(4)
>         self.assertEqual(len(solutions), 2)
> 
>     def test_8_queens(self):
>         solutions = solve_n_queens(8)
>         self.assertEqual(len(solutions), 92)
> 
> if __name__ == '__main__':
>     unittest.main()
> ```

---

## 4. Bug 引入与修复阶段

### 4.1 引入 Bug
> **用户操作**：
> 我故意修改了 `is_valid` 函数，注释掉了右上到左下对角线的检查代码，以引入一个 Bug。
> ```python
> def is_valid(row: int, col: int) -> bool:
>     # 检查列
>     for i in range(row):
>         if board[i][col] == 'Q':
>             return False
>     # 检查左上到右下对角线
>     i, j = row - 1, col - 1
>     while i >= 0 and j >= 0:
>         if board[i][j] == 'Q':
>             return False
>         i -= 1
>         j -= 1
>     # 故意注释掉右上到左下对角线的检查
>     # i, j = row - 1, col + 1
>     # while i >= 0 and j < n:
>     #     if board[i][j] == 'Q':
>     #         return False
>     #     i -= 1
>     #     j += 1
>     return True
> ```

### 4.2 测试失败
> **用户操作**：
> 运行测试后，测试失败，错误信息如下：
> ```
> AssertionError: 12 != 2
> ```
> 这表明 N=4 时错误地找到了 12 种解，而不是正确的 2 种。

### 4.3 需求描述（Bug 修复）
> **用户 Prompt**：
> 我的 N 皇后求解器在测试时失败了。当 N=4 时，它返回了 12 种解，而不是预期的 2 种。错误代码和测试失败的日志如下... 请帮我定位 Bug 并修复。

### 4.4 AI 响应（Bug 定位）
> **AI 输出**：
> 我分析了你的代码，发现 Bug 出在 `is_valid` 函数中。你注释掉了对右上到左下对角线的检查，这导致算法无法检测到斜线上的皇后冲突，从而产生了大量错误的解。

### 4.5 AI 响应（Bug 修复）
> **AI 输出**：
> 这是修复后的代码：
> ```python
> def is_valid(row: int, col: int) -> bool:
>     # 检查列
>     for i in range(row):
>         if board[i][col] == 'Q':
>             return False
>     # 检查左上到右下对角线
>     i, j = row - 1, col - 1
>     while i >= 0 and j >= 0:
>         if board[i][j] == 'Q':
>             return False
>         i -= 1
>         j -= 1
>     # 检查右上到左下对角线
>     i, j = row - 1, col + 1
>     while i >= 0 and j < n:
>         if board[i][j] == 'Q':
>             return False
>         i -= 1
>         j += 1
>     return True
> ```

### 4.6 验证修复
> **用户操作**：
> 应用修复后的代码，重新运行测试，测试通过。
> ```
> test_4_queens ... ok
> test_8_queens ... ok
> ```

---

## 5. 代码重构阶段（可选）

### 5.1 需求描述
> **用户 Prompt**：
> 请帮我重构一下 `solve_n_queens` 函数，让它的性能更好，同时保持代码的可读性。

### 5.2 AI 响应
> **AI 输出**：
> 我可以通过使用集合来跟踪已占用的列和对角线，从而将 `is_valid` 函数的时间复杂度从 O(n) 降低到 O(1)，以下是重构后的代码...
