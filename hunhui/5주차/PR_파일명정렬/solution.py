def fileSplit(file):
    head = ''
    num = ''
    for i, c in enumerate(file):
        if c.isnumeric():
            break
        head += c
    for i in range(len(head), len(file)):
        n = file[i]
        if not n.isnumeric():
            break
        num += n
    return head, num, file[len(head+num):]

def solution(files):
    fileList = []
    for i, file in enumerate(files):
        head, num, tail = fileSplit(file)
        fileList.append((head.lower(), int(num), file))
    fileList.sort(key=lambda e: e[1])
    fileList.sort(key=lambda e: e[0])
    return [e[2] for e in fileList]