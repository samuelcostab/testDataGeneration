def triang(i, j, k):
    tri = 0

    if ((i <= 0) | (j <= 0) | (k <= 0)):
        return 4

    tri = 0
    if (i == j):
        tri += 1
    if (i == k):
        tri += 2
    if (j == k):
        tri += 3
    if (tri == 0):
        if ((i+j <= k) | (j+k <= i) | (i+k <= j)):
            tri = 4
        else:
            tri = 1
        return tri

    if (tri > 3):
        tri = 3
    elif ((tri == 1) & (i+j > k)):
        tri = 2
    elif ((tri == 2) & (i+k > j)):
        tri = 2
    elif ((tri == 3) & (j+k > i)):
        tri = 2
    else:
        tri = 4

    return tri
