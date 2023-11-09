# Specification

## Registers

registers are letters 'a' through 'z' and are 64 bit integers

## Labels

`[name]:` where name is some non-empty sequence of lowercase letters

## Instructions

`movi [register] [integer literal]` sets the register to the integer specified, where the integer has to be on [0, 255]
`mov [register] [register]` copies the second register to the first one
`add [register] [register]` adds the value of the second register to the first register
`sub [register] [register]` subtracts the value of the second register from the first register
`jmp [label]` jumps to the line after the label
`jz [register] [label]` jumps to the label if the variable is zero, otherwise noop
`push [register]` pushes value of register onto the stack
`pop [register]` removes the top value from the stack and puts it in the register specified
`print [register]` prints the value of the register to standard out

## Binary encoding

Each instruction is 3 bytes, where the first byte encodes the instruction and the two others encoding the arguments

`movi = 0`
`mov = 1`
`add = 2`
`sub = 3`
`jmp = 4`
`jz = 5`
`push = 6`
`pop = 7`
`print = 8`

Registers are encoded as 8 bit indices on [0-25].
Integer literals are encoded as 8 bit twos complement integers.
Jump destinations are encoded as 8 bit twos complement instruction offsets in the code (this means you can't jump more than 128 instructions back, or more than 127 instructions forward).
Any instructions that take one argument are encoded as having a second argument of zero.
