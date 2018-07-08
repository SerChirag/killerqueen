n = input()
d = {}
d['purple'] = 'Power'
d['red'] = 'Reality'
d['green'] = 'Time'
d['yellow'] = 'Mind'
d['blue'] = 'Space'
d['orange'] = 'Soul'
for i in range(n):
    a = raw_input()
    del d[a]
print len(d)
for i in d:
    print d[i]