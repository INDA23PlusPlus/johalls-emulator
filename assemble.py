import sys
import string
import time

with open(sys.argv[1], "r") as input_file:
    program = [line.strip().split() for line in input_file.readlines() if line.strip()]

labels = {}
filtered = []

i = 0
for parts in program:
    if parts[0][-1] == ':':
        label_name = parts[0][:-1]
        for c in label_name:
            assert c in string.ascii_lowercase
        labels[label_name] = i
    else:
        filtered.append(parts)
        i += 1

encoded_program = []
for i, parts in enumerate(filtered):
    match parts[0]:
        case "movi":
            val = int(parts[2])
            assert -128 <= val < 128
            if val < 0: val += 256
            assert parts[1].isalpha()
            assert len(parts[1]) == 1
            encoded_program.append((0, ord(parts[1].lower()) - ord('a'), int(parts[2])))
        case "mov":
            assert parts[1].isalpha()
            assert len(parts[1]) == 1
            assert parts[2].isalpha()
            assert len(parts[2]) == 1
            encoded_program.append((1, ord(parts[1].lower()) - ord('a'), ord(parts[2].lower()) - ord('a')))
        case "add":
            assert parts[1].isalpha()
            assert len(parts[1]) == 1
            assert parts[2].isalpha()
            assert len(parts[2]) == 1
            encoded_program.append((2, ord(parts[1].lower()) - ord('a'), ord(parts[2].lower()) - ord('a')))
        case "sub":
            assert parts[1].isalpha()
            assert len(parts[1]) == 1
            assert parts[2].isalpha()
            assert len(parts[2]) == 1
            encoded_program.append((3, ord(parts[1].lower()) - ord('a'), ord(parts[2].lower()) - ord('a')))
        case "jmp":
            assert parts[1].isalpha()
            offs = labels[parts[1]] - i
            assert -128 <= offs < 128
            if offs < 0: offs += 256
            encoded_program.append((4, offs, 0))
        case "jz":
            assert parts[1].isalpha()
            assert len(parts[1]) == 1
            assert parts[2].isalpha()
            offs = labels[parts[2]] - i
            assert -128 <= offs < 128
            if offs < 0: offs += 256
            encoded_program.append((5, ord(parts[1].lower()) - ord('a'), offs))
        case "push":
            assert parts[1].isalpha()
            assert len(parts[1]) == 1
            encoded_program.append((6, ord(parts[1].lower()) - ord('a'), 0))
        case "pop":
            assert parts[1].isalpha()
            assert len(parts[1]) == 1
            encoded_program.append((7, ord(parts[1].lower()) - ord('a'), 0))
        case "print":
            assert parts[1].isalpha()
            assert len(parts[1]) == 1
            encoded_program.append((8, ord(parts[1].lower()) - ord('a'), 0))


with open(sys.argv[2], "wb") as output_file:
    flattened = []
    for instr in encoded_program:
        flattened.append(instr[0])
        flattened.append(instr[1])
        flattened.append(instr[2])
    output_file.write(bytes(flattened))

