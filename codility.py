def solution(n):
    d = [0] * 30
    l = 0
    # need to monitor 'l' not '0'
    while (n > l):
        d[l] = n % 2
        n //= 2
        l += 1
    for p in xrange(1, l):
        ok = True
        # range should be 'l' not 'l+1'
        for i in xrange(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1

