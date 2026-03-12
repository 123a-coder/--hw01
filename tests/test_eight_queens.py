# AI 协作交互日志

## 2026-03-12 八皇后问题工程化实践

### 1. 需求描述
需要完成基于 AI 协作的八皇后问题工程化实践，包括：
- 初始化含 src/ 和 tests/ 的标准 Python 工程
- 实现八皇后问题回溯求解器
- 编写单元测试验证算法正确性
- 故意引入 Bug 并观察 AI 定位修复过程

### 2. 代码实现过程
通过 AI 工具生成了八皇后求解器核心代码，包含 `is_valid`、`backtrack`、`get_all_solutions` 和 `print_board` 函数，实现了 8x8 棋盘所有合法解的计算与可视化。

### 3. 单元测试编写
借助 AI 生成了 pytest 单元测试用例，验证：
- 总解数为 92
- 所有解无同列、对角线冲突
- `is_valid` 函数的边界情况

### 4. Bug 引入与修复过程
#### 4.1 引入 Bug
故意注释掉 `is_valid` 函数中的对角线检查逻辑，代码如下：
```python
def is_valid(board, row, col):
    for r in range(row):
        if board[r] == col:
            return False
    # 注释掉对角线检查
    # for r in range(row):
    #     if abs(r - row) == abs(board[r] - col):
    #         return False
    return True