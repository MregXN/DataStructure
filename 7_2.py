# 根据前序、中序推断出后序的结果
# pre  123456
# in  324165
# post 342651
import numpy as np

Pre = [1, 2, 3, 4, 5, 6]
In = [3, 2, 4, 1, 6, 5]
Post = [0] * 6


def solve(prel, inl, postl, n):  # prel inl postl 各自第一个节点的位置
    if n == 0:
        return

    if n == 1:
        Post[postl] = Pre[prel]

    root = Pre[prel]
    Post[postl + n - 1] = root
    for i in np.arange(0, 6, 1):
        if In[inl + i] == root:
            L = i
            R = n - L - 1
            break
    solve(prel + 1, inl, postl, L)
    solve(prel + L + 1, inl + L + 1, postl + L, R)


if __name__ == "__main__":
    solve(0, 0, 0, 6)
    print(Post)
