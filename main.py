whole_str = ""
comment_regex = "^\s*#.*$"


if __name__ == '__main__':
    file = open('test.txt', 'r')
    whole_str = file.read()
    file.close()

    print(whole_str)