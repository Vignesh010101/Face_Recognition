input_str=input().strip()

vowels="aeiouAEIOU"
rslt=""
for char in input_str:
    if char not in vowels:
        rslt+=char
        
print(rslt)
