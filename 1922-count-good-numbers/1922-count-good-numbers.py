class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def power(x, y, mod):
            result = 1
            base = x % mod
            while y > 0:
                if y % 2 == 1:  
                    result = (result * base) % mod
                y = y // 2
                base = (base * base) % mod
            return result

        even_positions = (n + 1) // 2  
        odd_positions = n // 2  

        total_good_numbers = (power(5, even_positions, MOD) * power(4, odd_positions, MOD)) % MOD

        return total_good_numbers