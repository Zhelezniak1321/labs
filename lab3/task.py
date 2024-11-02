def is_uppercase(s: str) -> bool:
    if not s:
        return False
    for char in s:
        
        ascii_code = ord(char)
        
        
        if 97 <= ascii_code <= 122:
            return False
    return True


print(is_uppercase("c"))                
print(is_uppercase("C"))                
print(is_uppercase(""))                 
print(is_uppercase("hello I AM DONALD"))   
print(is_uppercase("HELLO I AM DONALD")) 
print(is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ")) 
print(is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ"))