class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0:
            _n = n
        else:
            # 浮點數溢位陷阱：先取倒數 x = 1/x vs 最後 1/ans
            # LeetCode 50 有一個著名的邊界測資：2^2147483648 遠超 IEEE 754 雙精度浮點數上限會直接 OverflowError 崩潰
            _n = -n
            x = 1/x
        binary = [int(i) for i in reversed(bin(_n)[2:])]

        ele = [x]
        while len(ele) < len(binary):
            ele.append(ele[-1] * ele[-1])

        ans = 1
        for idx, i in enumerate(binary):
            if i == 0:
                continue
            ans *= ele[idx]

        return ans