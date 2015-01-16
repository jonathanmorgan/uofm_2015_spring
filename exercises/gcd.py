def gcd_iter(u, v):
    while v:
        print( "v = " + str( v ) )
        u, v = v, u % v
    return abs(u)
