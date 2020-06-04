

if __name__ == "__main__":
    set_a = set(input().split())
    len_set_a = len(set_a)

    is_strict_super_set = True
    for i in range(int(input())):
        set_b = set(input().split())
        is_strict_super_set &= (set_a.issuperset(set_b) and (len_set_a > len(set_b)))
        
    print(is_strict_super_set) 