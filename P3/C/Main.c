#include <stdio.h>
#include <limits.h> 	//este no sé para cual, pero para parametros

//#include <stdbool.h>
//#include "Etc.h"
#include "Tabulation.h"
#include "Memoization.h"

int main(void) { 
    int array[] = {1, 2, 3, 4, 5, 6, 7}; 
    int size = sizeof(array)/sizeof(array[0]); 
	printf("Minimum number of multiplications is %d \n",
			Tabulation(array, size)); 
	printf("MEMOI: Minimum number of multiplications is %d \n", Memoization(array, size));

    return 0; 
} 
