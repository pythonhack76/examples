#strip, len, lower, upper, split about string operators

valore = "      ******parole - sconnesse - di - seguito"
print(valore)
l_valore = len(valore)
print(l_valore)
if l_valore <= 5:
    print(valore.upper())
stripper = valore.strip() 
print(stripper)
splitter = valore.split('*')
print(splitter)
for i in splitter:
    print(i)
