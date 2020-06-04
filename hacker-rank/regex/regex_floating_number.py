import re


if __name__ == "__main__":
    arr = [input() for i in range(int(input()))]

    print("\n".join([ "True" if (re.search(r"^[+-]?\d*\.\d+$", st)) else "False" for st in arr]))