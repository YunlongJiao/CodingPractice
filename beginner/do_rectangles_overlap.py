# NOTE:
# Create Point class!
# Easier to code for when two rectangles do NOT overlap!


class Point:
    """
    2d point with (x,y) coordinates.

    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


# def do_rectangles_overlap(l1, r1, l2, r2):
#     """
#     Returns true if two rectangles (l1, r1) and (l2, r2) overlap (topleft, bottomright).
#
#     https://www.geeksforgeeks.org/find-two-rectangles-overlap/
#
#     """
#
#     o1 = l1.x <= l2.x < r1.x and l1.y >= l2.y > r1.y
#     o2 = l2.x <= l1.x < r2.x and l2.y >= l1.y > r2.y
#
#     if o1 or o2:
#         return True
#     else:
#         return False


def do_rectangles_overlap(l1, r1, l2, r2):
    """
    Returns true if two rectangles (l1, r1) and (l2, r2) overlap (topleft, bottomright).

    https://www.geeksforgeeks.org/find-two-rectangles-overlap/

    """

    o1 = l1.x > r2.x or l2.x > r1.x
    o2 = l1.y < r2.y or l2.y < r1.y

    if o1 or o2:
        return False
    else:
        return True


if __name__ == '__main__':

    l1, r1 = Point(0, 10), Point(10, 0)
    l2, r2 = Point(5, 5), Point(15, 0)

    overlap = do_rectangles_overlap(l1, r1, l2, r2)
    print(overlap)
