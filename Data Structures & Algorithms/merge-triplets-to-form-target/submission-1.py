class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid_pos = [False, False, False]
        for idx, triplet in enumerate(triplets):
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            for i in range(3):
                if triplet[i] == target[i]:
                    valid_pos[i] = True
            
            if all(valid_pos):
                return True

        return all(valid_pos)