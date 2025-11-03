from math import gcd
from collections import defaultdict
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        max_points = 0

        for i in range(n):
            slope_count = defaultdict(int)
            same_point = 0
            cur_max = 0

            xi, yi = points[i]

            for j in range(i + 1, n):
                xj, yj = points[j]
                dx = xj - xi
                dy = yj - yi

                if dx == 0 and dy == 0:
                    same_point += 1
                    continue

                # Handle vertical and horizontal explicitly to avoid sign splits
                if dx == 0:
                    slope = (1, 0)   # canonical vertical
                elif dy == 0:
                    slope = (0, 1)   # canonical horizontal
                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g
                    # normalize so dx is positive (unique representation)
                    if dx < 0:
                        dx, dy = -dx, -dy
                    slope = (dy, dx)

                slope_count[slope] += 1
                cur_max = max(cur_max, slope_count[slope])

            max_points = max(max_points, cur_max + same_point + 1)

        return max_points
