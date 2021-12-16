def minimoinc(a):
    s = 0;
    i = 0
    while i < len(a)-1:
        if a[i+1]<=a[i]:
            t = abs(a[i] - a[i+1]) + 1
            a[i + 1] += t
            s += t
        i += 1
    return s


print(minimoinc([1,1,1]))
print(minimoinc([2,1,10,1]))
print(minimoinc([-1000,0,-2,0]))

