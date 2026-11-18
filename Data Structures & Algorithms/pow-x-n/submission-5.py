class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0:
            _n = n
        else:
            _n = -n
        binary = [int(i) for i in reversed(bin(_n)[2:])]

        ele = [x]
        while len(ele) < len(binary):
            ele.append(ele[-1] * ele[-1])

        ans = 1
        for idx, i in enumerate(binary):
            if i == 0:
                continue
            ans *= ele[idx]

        return ans if n > 0 else 1/ans