import re
if __name__ == "__main__":
    
    S = input()
    
    if len(S) < 100 and len(S) > 0: 
        arr = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aeiouAEIUO]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', S)
        if arr: print("\n".join(arr))
        else: print('-1')
    
    
        
    