import sys

def main():
    s = 'hi'
    print s[1]
    print len(s)
    print s + ' there'
    pi = 3.14
    ##text = 'The value of pi is ' + pi ## No, does not work
    text = 'The value of pi is ' + str(pi) ## yes
    print text
    raw = r'this\t\n and that'
    print raw       ## this\t\n and that
    multi = """It was the best of times.
    It was the worst of times."""
    print multi

if __name__ == '__main__':
    main()
