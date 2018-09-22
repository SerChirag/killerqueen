from sys import *
t = int(stdin.readline())
loda = []
for pogo in range(t):
    n = int(stdin.readline())
    for cn in range(n):
        m = {}
        input = stdin.readline()
        for i in range(8):
            input = stdin.readline().split('=')
            input[1] = input[1].strip('\n')
            input[1] = input[1].strip(',')
            input[1] = input[1].strip('{')
            input[1] = input[1].strip('}')
            m[input[0]] = input[1]
        input = stdin.readline()
        s = ""
        name = m["author"].split(', ')
        for j in range(len(name)):
            i = name[j]
            namos = i.split(' ')
            s+= namos[0][:2]
            s+=". "
            s+= namos[1][0]
            if(j == len(name)-1):
                s+= ". "
            else:
                s+= ", "
        s += m['title']
        s+= ". "
        s += m['journal']
        s+= ". "
        s += m['year']
        s+= ";"
        s += m['volume']
        s+= "("
        s += m['number']
        s+= "):"
        s += m['pages']
        s += "."
        loda.append(s)

            
stdout.write("\n".join(loda))

