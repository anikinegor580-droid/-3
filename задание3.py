def anagram1(s1, s2):
    if len(s1) != len(s2):
        return False
    s2_list = list(s2)
    for c in s1:
        if c in s2_list:
            s2_list.remove(c)
        else:
            return False
    return True

print(anagram1('heart', 'earth'))
print(anagram1('python', 'typhon'))
print(anagram1('hello', 'world'))


def anagram2(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    return s1_sorted == s2_sorted

print(anagram2('heart', 'earth'))
print(anagram2('python', 'typhon'))
print(anagram2('hello', 'world'))


def anagram3(s1, s2):
    if len(s1) != len(s2):
        return False
    count1 = {}
    count2 = {}
    
    for char in s1:
        count1[char] = count1.get(char, 0) + 1
    for char in s2:
        count2[char] = count2.get(char, 0) + 1
        
    return count1 == count2

print(anagram3('heart', 'earth'))
print(anagram3('python', 'typhon'))
print(anagram3('hello', 'world'))
