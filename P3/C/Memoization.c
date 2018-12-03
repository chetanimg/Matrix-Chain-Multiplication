#include <stdio.h> 
#include <stdlib.h>
#include <string.h>
#include <limits.h> 
#include <glib.h>
int i, j, k, L, q;

GHashTable* map = NULL;

/*
int LOOKUPCHAIN (int array[], int i, int j, int m[][]) {

	if (m[i][j] < INT_MAX)	return m[i][j];
	if (i == j) {
		m[i][j] = 0;
	} 
	for (k = i; k < j-1; k++) {
		q = LOOKUPCHAIN(array,i,k) + LOOKUPCHAIN(array,k+1,j) + array[i-1]*array[k]*array[j]; 
		if (q < m[i][j]) m[i][j] = q; 

	}
	return m[i][j];
}
*/
int Memoization(int array[], int size)  { 
	char i_str[12];
	char j_str[12];
	char * key = NULL;
   	int * value = NULL;
	char * old_key = NULL;
   	int * old_value = NULL;
	size_t ilen, jlen;
	char *keystring;
    map = g_hash_table_new (g_int_hash, g_int_equal);
	key = malloc(sizeof(*key));
	
   	for (i = 1; i < size; i++) {
		sprintf(i_str, "%d", i);
		ilen = strlen(i_str);
		for (j = i; j < size; j++  ) {
			sprintf(j_str, "%d", j);
			jlen = strlen(j_str);
			keystring = malloc(ilen + jlen + 2);
			strcpy(keystring, i_str);
			keystring[ilen] = ",";
			strcat(i_str,j_str);
			
			//Esto crea un pointer...
			key = strdup(keystring);
			
			if (g_hash_table_lookup_extended (table, key, &old_key, &old_value)){
            	/* Insert the new value */
            	g_hash_table_insert (table, g_strdup (key), g_strdup (value));
            	/* Just free the key and value */
            	g_free (old_key);
            	g_free (old_value);
        	} else {
            	/* Insert into our hash table it is not a duplicate. */
            	g_hash_table_insert (table, g_strdup (key), g_strdup (value));
			} 
		}
    }

	LOOKUPCHAIN (array, 1, size-1, m[0]);
}
