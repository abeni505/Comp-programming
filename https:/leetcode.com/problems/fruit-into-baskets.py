class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        t1 = fruits[0]
        t2 = None
        last = (fruits[0], 0)
        i, j = 0, 0
        maximum = 1
        for i in range(1, len(fruits)):
            if t2 is None and fruits[i] != t1 : t2 = fruits[i]
            if fruits[i] != t1 and fruits[i] != t2:
                j, t1, t2 = last[1], last[0], fruits[i]
            if fruits[i] != last[0]: last = (fruits[i], i)
            maximum = max(maximum, i-j + 1)   
        return maximum
