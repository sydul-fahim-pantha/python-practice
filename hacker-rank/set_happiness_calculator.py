

if __name__ == "__main__":
    n, m = map(int, input().split())
    set_n = list(map(int, input().split(" ", n)))
    
    set_a = set(map(int, input().split(" ", m)))
    set_b = set(map(int, input().split(" ", m)))
    
    happy = 0
    for i in set_a: 
        if i in set_n: happy += 1

    for i in set_b: 
        if i in set_n: happy -= -1

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