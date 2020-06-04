import re

if __name__ == "__main__":
    print("\n".join([ 'YES' if re.match(r'^[789]\d{9,9}$', input()) else 'NO' for i in range(int(input()))]))
    