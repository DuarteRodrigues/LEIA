#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define GENE_NUM 4
#define SEARCH_SPACE_MIN -100.0
#define SEARCH_SPACE_MAX 100.0
#define POPU 120
#define ELITE_RATE 0.3
#define MUTATION_PROB 120

// Declare FUNC_Q with proper argument types
int FUNC_Q(int x1, int x2, int x3, int x4) {
    return ((x1-4)*(x1-4)) + ((x2-3)*(x2-3)) + ((x3-2)*(x3-2)) + (x4*x4);
}

int main(){

    int array[GENE_NUM][POPU];
    int x, y;
    
    srand(time(NULL));
    
    for(x = 0; x < POPU; x++) {
        for(y = 0; y < GENE_NUM; y++) {
            array[y][x] = rand() % (int)(SEARCH_SPACE_MAX - SEARCH_SPACE_MIN + 1) + SEARCH_SPACE_MIN;
        }
        printf("Pop %d: %d | %d | %d | %d |\n", x, array[0][x], array[1][x], array[2][x], array[3][x]);
    }


    //while(True){
        //for(x=0; x <= POPU ;x++){
            //FUNC_Q(array[0][x],array[1][x],array[2][x],array[3][x]);
        //}
    //}
    
    return 0;
}
