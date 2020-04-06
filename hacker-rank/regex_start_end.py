import re

if __name__ == "__main__":
    S = input()
    k = input()
    if (len(S) > 0 and len(S) < 100 and len(k) > 0 and len(k) < len(S)):
        print("\n".join([ str((i.start(), i.start() + len(k) - 1)) for i in (re.finditer(r'(?=('+ k + '))', S))]) or '(-1, -1)')
    else:  print('(-1, -1)')