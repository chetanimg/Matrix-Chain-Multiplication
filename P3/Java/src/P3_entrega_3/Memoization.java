package P3_entrega_3;

import java.util.HashMap;
import java.util.Map;

public class Memoization {
    // Matrix Ai has dimension p[i-1] x p[i] for i = 1..n 
    static int MatrixChainOrder(int p[], int n) 
    { 
        /* For simplicity of the program, one extra row and one 
        extra column are allocated in m[][].  0th row and 0th 
        column of m[][] are not used */
        Map<String, Integer> dict = new HashMap<>();
        
        
        int i, j, k, L, q; 
  
        /* m[i,j] = Minimum number of scalar multiplications needed 
        to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where 
        dimension of A[i] is p[i-1] x p[i] */
  
        // cost is zero when multiplying one matrix. 
        for (i = 1; i < n; i++) 
            dict.put(i+","+i, 0);
  
        // L is chain length. 
        for (L=2; L<n; L++) 
        { 
            for (i=1; i<n-L+1; i++) 
            { 
                j = i+L-1; 
                if(j == n) continue;
                dict.put(i+","+j, Integer.MAX_VALUE);
                for (k=i; k<=j-1; k++) 
                { 
                    // q = cost/scalar multiplications 
                    q = dict.get(i+","+k) + dict.get((k+1)+","+j) + p[i-1]*p[k]*p[j]; 
                    if (q < dict.get(i+","+j)) 
                        dict.put(i+","+j, q);
                } 
            } 
        } 
  
        return dict.get(1+","+(n-1)); 
    }
}
