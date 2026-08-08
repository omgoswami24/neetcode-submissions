class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        heap = []

        for num,frq in freq.items():
            heapq.heappush(heap, (frq,num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        final = []

        for frq,num in heap:
            final.append(num)
        
        return final
        

        