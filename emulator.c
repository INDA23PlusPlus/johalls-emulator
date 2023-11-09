#include <assert.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

enum Instruction {
    MOVI = 0,
    MOV = 1,
    ADD = 2,
    SUB = 3,
    JMP = 4,
    JZ = 5,
    PUSH = 6,
    POP = 7,
    PRINT = 8,
};

#define STACK_SIZE 1024

int main(int argc, char **argv) {
    if (argc < 2) {
        fputs("no input file provided", stderr);
        return -1;
    }

    FILE *inp = fopen(argv[1], "r");
    assert(inp);
    fseek(inp, 0, SEEK_END);
    assert(!ferror(inp));
    size_t length = ftell(inp);
    assert(!ferror(inp));
    fseek(inp, 0, SEEK_SET);
    assert(!ferror(inp));

    uint8_t *contents = malloc(length);
    fread(contents, length, length, inp);
    assert(!ferror(inp));

    size_t num_instructions = length / 3;

    int64_t variables[26] = {};
    int64_t stack[STACK_SIZE] = {};
    int stack_idx = 0;

    for (size_t i = 0; i < num_instructions; ++i) {
        int instr = contents[3 * i], arg1 = contents[3 * i + 1], arg2 = contents[3 * i + 2];
        switch (instr) {
            case MOVI:
                arg2 -= (arg2 & 128) * 2; // twos complement
                variables[arg1] = arg2;
                break;
            case MOV:
                variables[arg1] = variables[arg2];
                break;
            case ADD:
                variables[arg1] += variables[arg2];
                break;
            case SUB:
                variables[arg1] -= variables[arg2];
                break;
            case JMP:
                arg1 -= (arg1 & 128) * 2; // twos complement
                i += arg1 - 1;
                break;
            case JZ:
                arg2 -= (arg2 & 128) * 2; // twos complement
                if (variables[arg1] == 0) i += arg2 - 1;
                break;
            case PUSH:
                assert(stack_idx < STACK_SIZE);
                stack[stack_idx++] = variables[arg1];
                break;
            case POP:
                assert(stack_idx > 0);
                variables[arg1] = stack[--stack_idx];
                break;
            case PRINT:
                printf("%" PRId64 "\n", variables[arg1]);
                break;
        }
    }

    free(contents);
    fclose(inp);
}