class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        vals = []
        for i, row in enumerate(mat):
            count = 0
            for j in row:
                if j == 1:
                    count = count + 1
            vals.append((count, i))
        vals.sort()
        return [i[1] for i in vals[:k]]
