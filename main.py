import re


whole_str = ""
comment_regex = "/{1}\*{1}.+\*?/{1}"


if __name__ == '__main__':
    file = open('test.txt', 'r')
    whole_str = file.read()
    file.close()

    print(re.findall(comment_regex, whole_str))
