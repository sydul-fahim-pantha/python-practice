

if __name__ == "__main__":
    n, m = map(int, input().split())
    set_n = set(map(int, input().split(" ", n)))
    
    dict_set_n = dict.fromkeys(set_n, 0)
    for i in set_n: dict_set_n[i] += 1

    set_a = set(map(int, input().split(" ", m)))
    set_b = set(map(int, input().split(" ", m)))
    
    #set_n_a_b_intersection = set(dict_set_n.keys()).intersection(set_a.union(set_b))) 
    
    happy = 0
    for i in set_a: 
        if dict_set_n.get(i): happy += dict_set_n[i]

    for i in set_b: 
        if dict_set_n.get(i): happy -= dict_set_n[i]

    print(happy)

    '''
     n, m = map(int, input().split())
    set_n = set(map(int, input().split(" ", n)))
    set_a = set(map(int, input().split(" ", m)))
    set_b = set(map(int, input().split(" ", m)))

    happy = 0
    for i in set_n:
        set_i = set([i])
        if set_i.issubset(set_a):  happy += 1
        elif set_i.issubset(set_b): happy -= 1
    print(happy)
    '''