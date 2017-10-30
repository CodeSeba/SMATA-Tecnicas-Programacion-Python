import java.util.Scanner;

public class Principal {
    public static void main (String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        Contador conta = new Contador();
        int nro;
        
        System.out.println("Ingresar Nro.:");
        nro = teclado.nextInt();
        conta.setContador(nro);
        
        System.out.println("El valor de conta es: "+conta.getContador());
        
        conta.incrementar();
        System.out.println("El valor de conta es: "+conta.getContador());
        
        conta.decrementar();
        conta.decrementar();
        System.out.println("El valor de conta es: "+conta.getContador());
    }
}
