from pandas.io.clipboard import clipboard_get, clipboard_set
text = clipboard_get() 
print(text)

clipboard_set("http://evil-website.net")

text = clipboard_get() 
print(text)
