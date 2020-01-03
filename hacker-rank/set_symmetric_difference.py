

if __name__ == "__main__":
    len_set_a = int(input())
    set_a = set(map(int, input().split(" ", len_set_a)))

    len_set_b = int(input())
    set_b = set(map(int, input().split(" ", len_set_b)))
    
    print("\n".join(map(str,sorted(set_a.symmetric_difference(set_b)))))