import sys, string, time

variables = {a: 0 for a in string.ascii_lowercase}

program = [line.strip().split() for line in sys.stdin.readlines() if line.strip()]

labels = {}

for i, parts in enumerate(program):
    if parts[0][-1] == ':':
        label_name = parts[0][:-1]
        for c in label_name:
            assert c in string.ascii_lowercase
        labels[label_name] = i

idx = 0
while idx < len(program):
    parts = program[idx]
    
    match parts[0]:
        case "mov":
            assert -2 ** 63 <= variables[parts[1]] < 2 ** 63
            assert -2 ** 63 <= variables[parts[2]] < 2 ** 63
            variables[parts[1]] = variables[parts[2]]
            pass
        case "movi":
            assert -2 ** 63 <= variables[parts[1]] < 2 ** 63
            assert 0 <= int(parts[2]) < 128
            variables[parts[1]] = int(parts[2])
            pass
        case "add":
            assert -2 ** 63 <= variables[parts[1]] < 2 ** 63
            assert -2 ** 63 <= variables[parts[2]] < 2 ** 63
            variables[parts[1]] += variables[parts[2]]
        case "sub":
            assert -2 ** 63 <= variables[parts[1]] < 2 ** 63
            assert -2 ** 63 <= variables[parts[2]] < 2 ** 63
            variables[parts[1]] -= variables[parts[2]]
        case "print":
            assert -2 ** 63 <= variables[parts[1]] < 2 ** 63
            print(variables[parts[1]])
        case "jmp":
            idx = labels[parts[1]]
        case "jz":
            assert -2 ** 63 <= variables[parts[1]] < 2 ** 63
            if variables[parts[1]] == 0:
                idx = labels[parts[2]]
    idx += 1
    