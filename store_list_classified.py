import re

r = re.compile("\\((.*)\\)")


def walk_line(filepath):
    with open(filepath, 'r', encoding='UTF-8') as fin:
        for line in fin:
            yield line.strip()


if __name__ == "__main__":
    for line in walk_line('./store_list'):
        if line[0] == '═':
            continue
        if line[0] == '=':
            continue
        m = r.search(line)
        if m:
            print(m.group(1))
            print(line.split('  ')[-1])
