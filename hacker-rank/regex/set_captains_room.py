

if __name__ == "__main__":
    k = int(input())
    list_k = list(input().split(" "))
    
    dict_k = dict.fromkeys(set(list_k), 0)
    for i in list_k: dict_k[i] += 1
    
    for i in dict_k.keys():
        if dict_k[i] == 1:
            print(i)
            break
