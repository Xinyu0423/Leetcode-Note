# 这个函数print的值为9
# 因为index的值加1为dfs的下一层
# 在递归结束执行时，index的值为上一层index的值

def dfs(index):
    if index==10:
        return
    # print(index)
    dfs(index+1)
    print(index)

dfs(8)

