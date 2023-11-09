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
    FILE *inp = fopen(argv[1], "r");
    fseek(inp, 0, SEEK_END);
    size_t length = ftell(inp);
    fseek(inp, 0, SEEK_SET);

    uint8_t *contents = malloc(length);
    fread(contents, length, length, inp);

    size_t num_instructions = length / 3;

    int64_t variables[26] = {};
    int64_t stack[STACK_SIZE] = {};
    int stack_idx = 0;

    for (size_t i = 0; i < num_instructions; ++i) {
        int instr = contents[3 * i], arg1 = contents[3 * i + 1], arg2 = contents[3 * i + 2];
        switch (instr) {
            case MOVI:
                if (arg2 >= 128) arg2 -= 256;
                // fprintf(stderr, "movi %c %d\n", (char) arg1, (int) arg2);
                variables[arg1 - 'a'] = arg2;
                break;
            case MOV:
                // fprintf(stderr, "mov %c %c\n", (char) arg1, (char) arg2);
                variables[arg1 - 'a'] = variables[arg2 - 'a'];

                break;
            case ADD:
                // fprintf(stderr, "add %c %c\n", (char) arg1, (char) arg2);
                variables[arg1 - 'a'] += variables[arg2 - 'a'];

                break;
            case SUB:
                // fprintf(stderr, "sub %c %c\n", (char) arg1, (char) arg2);
                variables[arg1 - 'a'] -= variables[arg2 - 'a'];

                break;
            case JMP:
                if (arg1 >= 128) arg1 -= 256;
                // fprintf(stderr, "jmp %d\n", arg1);
                i += arg1 - 1;

                break;
            case JZ:
                if (arg2 >= 128) arg2 -= 256;
                // fprintf(stderr, "jz %c %d\n", (char) arg1, (int) arg2);
                if (variables[arg1 - 'a'] == 0) i += arg2 - 1;

                break;
            case PUSH:
                assert(stack_idx < STACK_SIZE);
                // fprintf(stderr, "push %c\n", (char) arg1);
                stack[stack_idx++] = variables[arg1 - 'a'];

                break;
            case POP:
                assert(stack_idx > 0);
                // fprintf(stderr, "pop %c\n", (char) arg1);
                variables[arg1 - 'a'] = stack[--stack_idx];

                break;
            case PRINT:
                // fprintf(stderr, "print %c\n", (char) arg1);
                printf("%" PRId64 "\n", variables[arg1 - 'a']);
                break;
        }
    }

    free(contents);
    fclose(inp);
}