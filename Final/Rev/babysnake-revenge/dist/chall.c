#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/aes.h>
#include <openssl/rand.h>
#include <openssl/evp.h>

// Define the maze as a constant array
const char *maze[] = {
    "############### welcome to the maze ##############",
    "##################################################",
    "#...#.........#...#.....#...#.....#.....#.........",
    "###.#.#####.###.#.#.#.###.#.#.#.#.#####.#.#######.",
    "#...#...#...#...#.#.#.#...#...#.#.......#.#...#...",
    "#.#######.###.###.#.#.#.#######.#######.#.#.#.#.#.",
    "#.......#.......#...#...#.....#...#...#.#.#.#.#.#.",
    "#######.#############.#######.###.#.#.###.#.#.#.##",
    "#...#...#.....#.....#.........#...#.#.......#.#...",
    "#.###.###.###.#.###.#########.#.###.#############.",
    "#.....#...#...#.#.#.#.....#...#...#.#.....#.....#.",
    "#.#######.#.###.#.#.#.###.#.#####.#.#.#####.###.#.",
    "#...#.....#.....#...#.#...#...#.#...#.#...#...#.#.",
    "###.###.#########.###.#######.#.#####.#.#.###.#.#.",
    "#.#...#...#...#.#.#.#.........#.......#.#...#.#...",
    "#.###.#.#.#.#.#.#.#.#.#########.#####.#.###.#.####",
    "#.#...#.#...#.#...#.#.#.....#...#.....#...#.#.....",
    "#.#.###.#####.###.#.#.#.###.#####.###.###.#.#####.",
    "#...#.#.#...#...#.#...#.#.........#.....#.#.......",
    "#.###.#.#.#.#.#.#.###.#.###.#########.###.#.#####.",
    "#...#.#.#.#.#.#.#...#.#...#.#.......#.#...#.#...#.",
    "###.#.#.#.#.###.###.#.###.#.#.#####.#.#.#####.#.##",
    "#...#.#.#.#.....#...#.....#.#...#...#.#.......#...",
    "#.###.#.#.#######.#######.#####.#.###.###########.",
    "#...#...#...#.....#...#...#.....#...#.#.......#...",
    "###.#.#####.#.#####.#.#####.#######.###.#####.#.##",
    "#.#.#.#.....#...#...#.#...#...#.......#...#...#...",
    "#.#.###.#######.#.###.#.#.###.#.#####.###.#.#####.",
    "#.#.#...#.......#.#...#.#.#...#.#...#.....#.......",
    "#.#.#.###.#######.#.###.#.#.###.#.#.#############.",
    "#.#.#.#...........#.#...#...#...#.#.#...........#.",
    "#.#.#.#############.###.#########.#.#########.###.",
    "#...#.............#...#...#.......#.#.......#.....",
    "#.###############.###.###.#.#######.#.#####.###.##",
    "#.#.....#.....#...#.#...#.........#.#.#...#...#...",
    "#.#.###.#.###.#.###.###.#######.###.#.###.###.####",
    "#...#...#.#.#...#.....#...#.#...#...#.......#.#...",
    "#####.###.#.#########.###.#.#.###.#########.#.#.#.",
    "#...#.....#.......#...#...#.#...#.........#.#...#.",
    "#.#########.#####.#.#.#.###.###.#####.#####.#####.",
    "#.............#.#...#.#.#.#...#.#...#.......#...#.",
    "#####.#######.#.#.#####.#.#.#.#.#.#.#########.#.#.",
    "#...#.#.....#.#.#.#.....#...#.....#...#...#.#.#...",
    "#.#.###.###.#.#.#.#.###########.#####.#.#.#.#.###.",
    "#.#.....#.....#...#.#.........#.#...#...#...#.#...",
    "#.###.#####.#######.#.###.###.###.#.#####.###.#.##",
    "#.#...#...#.#.......#.#...#.#.#...#...#...#...#.#.",
    "#.#.###.#.###.#########.###.#.#.#####.#.###.###.#.",
    "#.#.#...#...#.#.........#.#...#.#.#...#.#...#...#.",
    "#.###.#####.#.#####.#####.#.###.#.#.#####.###.##..",
    "#.........#.........#...........#.........#.......",
    "################ good luck #######################"
};

// Function to generate the key from the path
void genKey(const int path[][2], size_t path_len, unsigned char *key) {
    memset(key, 0, AES_BLOCK_SIZE); // Initialize key with zeros
    for (size_t i = 0; i < path_len; i++) {
        key[i % AES_BLOCK_SIZE] ^= (path[i][0] + path[i][1]) % 256;
    }
}

// Function to decrypt the ciphertext using AES
void getFlag(const unsigned char *key, const unsigned char *iv, const unsigned char *ct, size_t ct_len, unsigned char *decrypted) {
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    int len;
    
    EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv);
    EVP_DecryptUpdate(ctx, decrypted, &len, ct, ct_len);
    int plaintext_len = len;
    EVP_DecryptFinal_ex(ctx, decrypted + len, &len);
    plaintext_len += len;
    decrypted[plaintext_len] = '\0'; // Null-terminate the decrypted string

    EVP_CIPHER_CTX_free(ctx);
}

int validate_path(const char *maze[], const int path[][2], size_t path_len) {
    for (size_t i = 0; i < path_len; i++) {
        int x = path[i][0];
        int y = path[i][1];
        if (maze[x][y] != '.') {
            return 0; // Invalid path
        }
    }
    return 1; // Valid path
}

int main() {
    // Initialization of the IV and ciphertext
    unsigned char iv[16] = {0x6d, 0x4a, 0x6b, 0x6c, 0x2f, 0x78, 0x35, 0x78, 0x4a, 0x31, 0x76, 0x69, 0x4c, 0x33, 0x34, 0x56}; // Base64-decoded IV
    unsigned char ct[] = {0x54, 0x62, 0x61, 0x76, 0x56, 0x2f, 0x6d, 0x48, 0x62, 0x6e, 0x43, 0x34, 0x4d, 0x59, 0x66, 0x35, 0x52, 0x30, 0x41, 0x34, 0x36, 0x64, 0x43, 0x37, 0x77, 0x77, 0x45, 0x39, 0x4c, 0x47, 0x2f, 0x65, 0x6d, 0x69, 0x76, 0x4f, 0x61, 0x65, 0x68, 0x58, 0x5a, 0x68, 0x6c, 0x72, 0x35, 0x58, 0x64, 0x39, 0x48, 0x71, 0x56, 0x43, 0x49, 0x51, 0x75, 0x48, 0x73, 0x63, 0x43, 0x56, 0x37, 0x6a}; // Base64-decoded ciphertext
    size_t ct_len = sizeof(ct);

    int path[100][2]; // Array to store user path
    size_t path_len = 0;
    unsigned char key[AES_BLOCK_SIZE];
    unsigned char decrypted[128]; // Buffer to store decrypted flag

    printf("well, its not a snake, but just pretend that you are the SNAKE lol. \n");
    printf("Navigate through the maze and find the correct path to unlock the key to get the flag.\n");
    printf("Use (row, col) to mark your path.\n");
    printf("\n");
    
    while (1) {
        // Display the maze
        for (int i = 0; i < sizeof(maze) / sizeof(maze[0]); i++) {
            printf("%s\n", maze[i]);
        }
        
        printf("\n");
        printf("Enter your move as 'row,col' (or type 'done' to finish): ");
        char input[50];
        fgets(input, sizeof(input), stdin);

        if (strncmp(input, "done", 4) == 0) {
            break;
        }

        int row, col;
        if (sscanf(input, "%d,%d", &row, &col) != 2) {
            printf("Invalid input. Enter coordinates as 'row,col'.\n");
            continue;
        }

        if (row < 0 || row >= sizeof(maze) / sizeof(maze[0]) || col < 0 || col >= strlen(maze[row]) || maze[row][col] != '.') {
            printf("Invalid move. Try again.\n");
            continue;
        }

        path[path_len][0] = row;
        path[path_len][1] = col;
        path_len++;
    }

    genKey(path, path_len, key);

    if (validate_path(maze, path, path_len)) {
        getFlag(key, iv, ct, ct_len, decrypted);
        printf("Decrypted flag: %s\n", decrypted);
    } else {
        printf("Please try again.\n");
    }

    return 0;
}
