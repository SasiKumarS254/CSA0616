def convex_hull(points):
    hull = []
    for p in points:
        for q in points:
            if p == q:
                continue
            is_valid = True
            for r in points:
                if r == p or r == q:
                    continue
                # Check orientation using the cross product
                cross_product = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
                if cross_product > 0:  # If any point is on the left, this line is invalid
                    is_valid = False
                    break
            if is_valid:
                if p not in hull:
                    hull.append(p)
                if q not in hull:
                    hull.append(q)
    return sorted(hull)  # Sorting ensures the result is in order

# Example points
points = [(0, 0), (4, 0), (4, 4), (0, 4), (2, 2)]
print("Convex Hull:", convex_hull(points))
