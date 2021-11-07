import requests
import json
import operator
from collections import Counter
l=[]
#εύρεση winning numbers για πρώτες δέκα μέρες
for i in range (1,10):
    day=i
#σελίδα όπου παίρνουμε κληρώσεις για κάυε μερα    
    a=requests.get(f"https://api.opap.gr/draws/v3.0/1100/draw-date/2021-02-0{day}/2021-02-0{day}")
    b=json.loads(a.content)
#εύρεση winning numbers πρώτης κλήρωσης
    c=(b["content"][0]["winningNumbers"]["list"])
    print(b["content"][0]["winningNumbers"]["list"])
#εισχώρηση των winning numbers σε λίστα για τις 10 μέρες
    l.extend(c)
#εύρεση winning numbers για υπόλοιπες μέρες
for i in range (10,27):
    day=i
    a=requests.get(f"https://api.opap.gr/draws/v3.0/1100/draw-date/2021-02-{day}/2021-02-{day}")
    b=json.loads(a.content)
    c=(b["content"][0]["winningNumbers"]["list"])
    print(b["content"][0]["winningNumbers"]["list"])
#εισχώρηση των winning numbers υπόλοιπων μερών στην ίδια λίστα με  τις 10 μέρες
    l.extend(c)
print(l)
len(l)
#μετατροπή λίστας σε λεξικό και εύρεση συχνότερου αριθμού
d = Counter(l)
print(d)
print("most used number is:", max(d, key=d.get))
