class Solution(object):
    def gcdOfOddEvenSums(self, n):
        even = []
        odd = []

        for i in range(n):
            odd.append(2*i+1)
            even.append(2*i+2)
            
        sumOdd = sum(odd)
        sumEven = sum(even)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        return gcd(sumOdd, sumEven)