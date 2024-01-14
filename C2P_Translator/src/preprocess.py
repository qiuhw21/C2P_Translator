def pre_process(data):
    lines = data.split('\n')
    index=0
    while index < len(lines):
        line = lines[index]
        line = line.strip(' ')
        line = line.strip('\t')
        line = line.strip('\r')
        line = line.strip('\n')
        if len(line) <= 0:
            lines.pop(index)
            continue
        if line[0] == '#':
            lines.pop(index)
            continue
        index += 1
    data='\n'.join(lines)
    return data
def add_main(output):
    output+="if __name__ == '__main__':\n\tmain()\n"
    return output