N, K = map(int, input().split())
place = 1

l = []

for i in range(N) :
    c, gold, silver, bronze = map(int, input().split())
    l.append((c, gold, silver, bronze))

l.sort(key=lambda x:(-x[1], -x[2], -x[3]))
p_g, p_s, p_b = l[0][1], l[0][2], l[0][3]
if l[0][0] == K :
    print(place)

else :
    for tuple in l[1:] :
        c, gold, silver, bronze = tuple
        if c == K :
            if gold == p_g and silver == p_s and bronze == p_b:
                print(place)
            else :
                place += 1
                print(place)
            break

        else :
            if gold == p_g or silver == p_s or bronze == p_b :
                continue
                p_g, p_s, p_b = gold, silver, bronze
            
            else :
                place += 1
            



