def main():
    n = int(input().strip())
    horizontal = []
    vertical = []
    
    # Read and classify lines
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        if y1 == y2:
            # horizontal line, store as (y, x_left, x_right)
            horizontal.append((y1, min(x1, x2), max(x1, x2)))
        elif x1 == x2:
            # vertical line, store as (x, y_bottom, y_top)
            vertical.append((x1, min(y1, y2), max(y1, y2)))

    rect_count = 0

    # For every pair of horizontal lines at different y coordinates
    for i in range(len(horizontal)):
        for j in range(i+1, len(horizontal)):
            y1, x1_l, x1_r = horizontal[i]
            y2, x2_l, x2_r = horizontal[j]
            if y1 == y2:
                continue
            # Find all verticals that connect both horizontals
            x_common = []
            for x, y_bot, y_top in vertical:
                if min(y1, y2) >= y_bot and max(y1, y2) <= y_top:
                    # This vertical can form a rectangle if it intersects both horizontals,
                    # and both horizontals cover this x
                    if x1_l <= x <= x1_r and x2_l <= x <= x2_r:
                        x_common.append(x)
            # Count rectangles formed by all pairs of these verticals
            k = len(x_common)
            rect_count += k*(k-1)//2
    
    print(rect_count)

if __name__ == "__main__":
    main()
