class Solution:

    def try_all_rectangles(self, heights):

        max_area = 0

        n = len(heights)

        for i in range(n):

            min_height = float('inf')

            for j in range(i, n):

                min_height = min(min_height, heights[j])

                max_area = max(max_area, min_height * (j - i + 1))

        return(max_area)

    def divide_and_conquer(self, heights):

        #divide and conquer

        def calculate_area(heights, start, end):

            if start > end:

                return(0)

            min_index = start

            for i in range(start, end + 1):

                if heights[i] < heights[min_index]:

                    min_index = i

            return(max(heights[min_index] * (end - start + 1),
                       calculate_area(heights, start, min_index - 1),
                       calculate_area(heights, min_index + 1, end)))
            
        return(calculate_area(heights, 0, len(heights) - 1))

    def largestRectangleArea(self, heights: List[int]) -> int:
    
      #puedes usar un stack minimizar el runtime

        stack = [-1]

        max_area = 0

        for i in range(len(heights)):

            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:

                current_height = heights[stack.pop()]

                current_width = i - stack[-1] - 1

                max_area = max(max_area, current_height * current_width)
            
            stack.append(i)

        while stack[-1] != - 1:

            current_height = heights[stack.pop()]

            current_width = len(heights) - stack[-1] - 1

            max_area = max(max_area, current_height * current_width)
            
        return(max_area)

        

