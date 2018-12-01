package P3_entrega_3;
import static P3_entrega_3.Etc.*;
import P3_entrega_3.Tabulation;
public class Main {
    public static void main(String[] args) {
        /*
        GetParam(args);
        if(di_flag)Input(); // debug input
        if(!do_flag && !t_flag)System.exit(0);
        
        prepareReader();
        int[] matrix;
        while((matrix = readMatrix())!= null){
            if(t_flag)ComienzaTimer(); // comenzamos a contar el tiempo de ejecucion
            long min_operations = Tabulation.MatrixChainOrder(matrix, matrix.length); // algoritmo tabulacion/memoization
            if(t_flag)ParaTimer(); // calculamos el tiempo de ejecucion
            if(!do_flag)Output(matrix, min_operations); // debug output
            if(t_flag)T_Output(); // se muestran los tiempos de ejecucion
        }
        */int [] p = new int[] {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
        System.out.println(Tabulation.MatrixChainOrder(p, p.length));
        System.out.println(Memoization.MatrixChainOrder(p, p.length));
    }
}
