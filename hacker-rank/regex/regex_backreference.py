
import re 

if __name__ == "__main__":
    S = input()
    output = "-1"
    if (len(S) < 100 and len(S) > 0): 
        matcher = re.search(r'([0-9a-zA-Z])\1', S)
        if (matcher): output = matcher.group(1)
    print(output)    