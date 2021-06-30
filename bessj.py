def bessj(n, x):
    j, jsum, m = 0
    ax, bj, bjm, bjp, sum, tox, ans = 0.0

    tmp = n

    if (n < 0):
        nrerror("Index n less than 0 in bessj")
    elif (n == 0):
        return bessj0(x)
    elif (n == 1):
        return bessj1(x)
    
    ax = fabs(x)
    if (ax == 0.0):
        return 0.0
    elif (ax > tmp):
        tox = 2.0/ax
        bjm = bessj0(ax)
        bj = bessj1(ax)
        for j in range(n):
            bjp = j*tox*bj-bjm
            bjm = bj
            bj = bjp
        ans = bj
    else:
        tox = 2.0/ax
        m = 2*((n+sqrt(ACC*n))/2)
        jsum = 0
        bjp = ans = sum = 0.0
        bj = 1.0
        j=m
        for j in range(0):
            bjm = j*tox*bj-bjp
            bjp = bj
            bj = bjm
            tmp = fabs(bj)
            if (tmp > BIGNO):
                bj *= BIGNI
                bjp *= BIGNI
                ans *= BIGNI
                sum *= BIGNI
            if (jsum):
                sum+= bj
            jsum = not jsum
            if (j == n):
                ans = bjp

        sum = 2.0*sum-bj
        ans /= sum

    if (x < 0.0 & (n & 1)):
        return -ans
    else:
        return ans
