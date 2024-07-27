class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        ans = []
        prev_char = ''
        prev_cnt = 0

        mx_heap = [(-freq, char) for char, freq in cnt.items()]
        heapq.heapify(mx_heap)

        while mx_heap:
            cnt, char = heapq.heappop(mx_heap)

            if prev_cnt < 0:
                heapq.heappush(mx_heap, (prev_cnt, prev_char))

            ans.append(char)

            prev_char = char
            prev_cnt = cnt + 1  
        if len(ans) == len(s):
            return "".join(ans)
        return ""
    