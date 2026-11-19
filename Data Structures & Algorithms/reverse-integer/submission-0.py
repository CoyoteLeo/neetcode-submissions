class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT32 = 0x7FFFFFFF
        CAP = MAX_INT32 // 10
        ONES = MAX_INT32 % 10
        is_negative = x < 0
        if is_negative:
            x = -x
        
        ans = 0
        while x > 0:
            new_digit = x % 10 
            if ans > CAP or (ans == CAP and new_digit > ONES):
                return 0
            ans = ans * 10 + x % 10 
            x //= 10
        return ans if not is_negative else -ans