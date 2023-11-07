# Specification

## Registers

registers are letters 'a' through 'z' and are 64 bit integers

## Labels

`[name]:` where name is two lowercase letters

## Instructions

`movi [register] [integer literal]` sets the register to the integer specified, where the integer has to be on [0, 254]
`mov [register] [register]` copies the second register to the first one
`add [register] [register]` adds the value of the second register to the first register
`sub [register] [register]` subtracts the value of the second register from the first register
`jmp [label]` jumps to the line after the label
`jz [register] [label]` jumps to the label if the variable is zero, otherwise noop
`print [register]` prints the value of the register to standard out

## Binary encoding

Each instruction is 3 bytes, where the first byte encodes the instruction and the two others encoding the arguments

`movi = 1`
`mov = 2`
`add = 3`
`sub = 4`
`jmp = 5`
`jz = 6`
`print = 7`
`labels = 8`

Registers are encoded with ascii.
Integer literals are encoded as the value + 1 (to avoid null bytes)
The arguments to a label are its name, encoded with ascii
