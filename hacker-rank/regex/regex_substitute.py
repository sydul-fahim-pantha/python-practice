import re

if __name__ == "__main__":
    N = int(input())
    pat = r'\s(\|\||\&\&)(?=\s)'
    arr = [input() for i in range(N)]
    print(re.sub(pat, lambda x: ' and' if x.group() == ' &&' else ' or', "\n".join(arr)))