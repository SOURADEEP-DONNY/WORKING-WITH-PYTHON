punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(s):
    for i in s:
        if i in punctuation_chars:
            s=s.replace(i,'')
    return s

print(strip_punctuation('wounderful'))
print(strip_punctuation('wow!'))
print(strip_punctuation('inc...re..dible!'))



