

if __name__ == "__main__":
    test_cases = int(input())
    results = []
    for i in range(test_cases):
        set_a_number_of_elements = int(input())
        set_a = set(input().split(None, set_a_number_of_elements))
        
        set_b_number_of_elements = int(input())
        set_b = set(input().split(None, set_b_number_of_elements))

        results.append(str(set_a.issubset(set_b)))
    print("\n".join(results)) 