def disemvowel(string):
    v = ['a', 'e', 'i', 'o', 'u']
    V = ['A', 'E', 'I', 'O', 'U']
    for i in string:
        if i in v or i in V:
            string = string.replace(i, '')
    return (string)


print(disemvowel('This website is for losers LOL'))
