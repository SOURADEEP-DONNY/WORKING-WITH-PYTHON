string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
letter_counts={}
for i in string1:
    p=i.lower()
    if p not in letter_counts:
        letter_counts[p]=0
    letter_counts[p]=letter_counts[p]+1
print(letter_counts)
