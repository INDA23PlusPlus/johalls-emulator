import sys, string, time

variables = {a: 0 for a in string.ascii_lowercase}

program = [line.strip().split() for line in sys.stdin.readlines() if line.strip()]

labels = {}

for i, parts in enumerate(program):
    if parts[0][-1] == ':':
        labels[parts[0][:-1]] = i

idx = 0
while idx < len(program):
    parts = program[idx]
    
    match parts[0]:
        case "mov":
            variables[parts[1]] = variables[parts[2]]
            pass
        case "movi":
            variables[parts[1]] = int(parts[2])
            pass
        case "add":
            variables[parts[1]] += variables[parts[2]]
        case "print":
            print(variables[parts[1]])
        case "jmp":
            idx = labels[parts[1]]
        case "jz":
            if variables[parts[1]] == 0:
                idx = labels[parts[2]]
    idx += 1
    