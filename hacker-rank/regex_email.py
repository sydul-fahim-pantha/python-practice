import re

if __name__ == "__main__":
    pattern = r'^.+ <[a-zA-Z][a-zA-Z0-9-_\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>$'
    print("\n".join([s for s in [input() for i in range(int(input()))] if re.match(pattern, s)]))
    
        
    