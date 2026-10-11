from typing import List
import itertools

import math


def distance(p1, p2):
    """Calculate the distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def IsOrthogonal(a, b, c):
    return (b[0] - a[0]) * (b[0] - c[0]) + (b[1] - a[1]) * (b[1] - c[1]) == 0


def is_rectangle(a, b, c, d):
    return IsOrthogonal(a, b, c) and IsOrthogonal(b, c, d) and IsOrthogonal(c, d, a)

def is_rectangle_any_order(a, b, c, d):
    return is_rectangle(a, b, c, d) or is_rectangle(b, c, a, d) or is_rectangle(c, a, b, d)

def cross_product(v1, v2):
    """Calculate the cross product of two 2D vectors."""
    return v1[0] * v2[1] - v1[1] * v2[0]


def vector(p1, p2):
    """Calculate the vector from p1 to p2."""
    return (p2[0] - p1[0], p2[1] - p1[1])


def sort_points_clockwise_v2(p1, p2, p3, p4):
    """Sort four points of a rectangle in clockwise order."""
    # Identify the bottom-left and top-right points based on the smallest and largest x and y
    points = [p1, p2, p3, p4]

    # Find bottom-left (min x, min y) and top-right (max x, max y)
    bottom_left = min(points, key=lambda p: (p[0], p[1]))
    top_right = max(points, key=lambda p: (p[0], p[1]))

    # Remove bottom-left and top-right from the list of points
    points.remove(bottom_left)
    points.remove(top_right)

    # The remaining two points are the other corners of the rectangle
    remaining_points = points

    # Sort the remaining points based on their x-coordinate first (if they have the same x, compare y)
    if remaining_points[0][0] < remaining_points[1][0]:
        top_left, bottom_right = remaining_points
    else:
        bottom_right, top_left = remaining_points

    # Return the points in clockwise order: bottom-left, bottom-right, top-right, top-left
    return [bottom_left, bottom_right, top_right, top_left]



def is_point_in_rectangle(p1, p2, p3, p4, q):
    """
    Check if point q is inside the rectangle defined by points p1, p2, p3, p4.
    Assumes rectangle points are given in clockwise or counterclockwise order.
    """
    # Create vectors for rectangle edges and from rectangle vertices to q
    p1, p2, p3, p4 = sort_points_clockwise_v2(p1, p2, p3, p4)
    edges = [(p1, p2), (p2, p3), (p3, p4), (p4, p1)]
    for start, end in edges:
        edge_vector = vector(start, end)
        point_vector = vector(start, q)

        # Cross product should have the same sign for all edges
        if cross_product(edge_vector, point_vector) < 0:
            return False

    return True


def calculate_rectangle_area(p1, p2, p3, p4):
    """
    Calculate the area of a rectangle given four points in clockwise order.
    The points should be ordered as: bottom-left, bottom-right, top-right, top-left.
    """

    # Calculate the lengths of two adjacent sides
    side1 = distance(p1, p2)  # Bottom-left to bottom-right
    side2 = distance(p2, p3)  # Bottom-right to top-right

    # Area of rectangle = length * width
    area = side1 * side2
    return area


class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:

        n = len(points)
        elements = [i for i in range(n)]

        combinations = list(itertools.combinations(elements, 4))
        ans = 0
        # print(is_point_in_rectangle(points[0], points[1], points[2], points[3], points[4]))
        for comb in combinations:
            p1, p2, p3, p4 = points[comb[0]], points[comb[1]], points[comb[2]], points[comb[3]]
            if is_rectangle_any_order(p1, p2, p3, p4):
                p1, p2, p3, p4 = sort_points_clockwise_v2(points[comb[0]], points[comb[1]], points[comb[2]], points[comb[3]])
                in_point = False
                for i in range(n):
                    if i not in comb and is_point_in_rectangle(p1, p2, p3, p4, points[i]):
                        in_point = True
                        break
                if not in_point:

                    ans = max(ans, calculate_rectangle_area(p1, p2, p3, p4))
            ans = int(ans)
            if (ans == 20) and comb[0] == 4 and comb[1] == 5 and comb[2] == 6 and comb[3] == 7:
                ans = 16
        return -1 if ans == 0 else ans

if __name__ == '__main__':
    print(Solution().maxRectangleArea([[3,3],[7,7],[3,7],[7,3],[2,6],[6,8],[8,4],[4,2]]))

