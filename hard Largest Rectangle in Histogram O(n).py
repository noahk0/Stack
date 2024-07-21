def largestRectangleArea(self, heights: List[int]) -> int:
    large, stack = heights[0], [(heights[0], 0)]

    for i in range(1, len(heights)):
        leng = i

        while stack and heights[i] < stack[-1][0]:
            pre, leng = stack.pop()
            large = max(large, pre * (i - leng))

        stack.append((heights[i], leng))

    for pre in stack:
        large = max(large, pre[0] * (len(heights) - pre[1]))

    return large
