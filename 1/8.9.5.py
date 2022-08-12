a = set('abracadabra')
b = set("alacazam")
c=(a-b)|(b-a)
d=a^b
print(c)
print(d)
print(c==d)