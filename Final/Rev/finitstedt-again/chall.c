#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FLAG_LENGTH 1024

// Finite-State-Automata states
typedef enum {
    STATE_0,
    STATE_1,
    STATE_2,
    STATE_3,
    STATE_4,
    STATE_5,
    STATE_6,
    STATE_7,
    STATE_8,
    STATE_9,
    NUM_STATES
} State;

// Transition table for FSA with 10 states
State transition[NUM_STATES][2] = {
    {STATE_7, STATE_3}, // STATE_0 transitions
    {STATE_4, STATE_9}, // STATE_1 transitions
    {STATE_6, STATE_8}, // STATE_2 transitions
    {STATE_1, STATE_5}, // STATE_3 transitions
    {STATE_9, STATE_0}, // STATE_4 transitions
    {STATE_8, STATE_2}, // STATE_5 transitions
    {STATE_0, STATE_7}, // STATE_6 transitions
    {STATE_5, STATE_1}, // STATE_7 transitions
    {STATE_2, STATE_6}, // STATE_8 transitions
    {STATE_3, STATE_4}  // STATE_9 transitions
};

// Function to read binary flag from file
char* read_flag(const char* filename) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        perror("Failed to open flag file");
        exit(EXIT_FAILURE);
    }

    char* flag = (char*)malloc(MAX_FLAG_LENGTH);
    if (flag == NULL) {
        perror("Failed to allocate memory");
        exit(EXIT_FAILURE);
    }

    if (fgets(flag, MAX_FLAG_LENGTH, file) == NULL) {
        perror("Failed to read flag");
        exit(EXIT_FAILURE);
    }

    fclose(file);
    return flag;
}

// Function to shuffle the flag using FSA
void shuffle_flag(char* flag) {
    State current_state = STATE_0;
    size_t len = strlen(flag);
    for (size_t i = 0; i < len; ++i) {
        int bit = flag[i] - '0';
        if (bit != 0 && bit != 1) {
            fprintf(stderr, "Invalid character in flag: %c\n", flag[i]);
            exit(EXIT_FAILURE);
        }
        current_state = transition[current_state][bit];
        flag[i] = '0' + current_state;
    }
}

// Main function
int main(int argc, char* argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <flagfile>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    char* flag = read_flag(argv[1]);
    shuffle_flag(flag);
    printf("Shuffled flag: %s\n", flag);
    free(flag);

    return 0;
}
