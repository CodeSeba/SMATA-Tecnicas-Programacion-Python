import java.util.Scanner;
import java.util.Arrays;

public class Principal {
    public static void main (String[] args) {
        
        Cuenta cuenta01 = new Cuenta();
        Cuenta cuenta02 = new Cuenta("Ana", "002", 3500.59);
        Scanner teclado = new Scanner(System.in);
        
        System.out.println("Ingresar un Nombre del Cliente:");
        String nombre = teclado.next();
        System.out.println("Ingresar un Nro de Cuenta:");
        String nro = teclado.next();
        
        System.out.println("Ingresar un Saldo de la cuenta:");
        double monto = teclado.nextDouble();
        
        cuenta01.setNombre(nombre);
        cuenta01.setNroCuenta(nro);
        cuenta01.setSaldo(monto);
        
        System.out.println("\nLista de Cuentas:\n");
        
        for ( Cuenta unaCuenta : Arrays.asList(cuenta01,cuenta02) ) {
            System.out.println("Nro de Cuenta: "+unaCuenta.getNroCuenta());
            System.out.println("Nombre: "+unaCuenta.getNombre());
            System.out.println("Saldo: "+unaCuenta.getSaldo());
            System.out.println("----------------------");
        }
        
        System.out.println("\nSe deposita 100 en Cuenta01:");
        cuenta01.deposito(100);
        System.out.println("Saldo Cuenta01: "+cuenta01.getSaldo());
        
        System.out.println("\nSe extrae 200 en Cuenta01:");
        cuenta01.extraccion(200);
        System.out.println("Saldo Cuenta01: "+cuenta01.getSaldo());
        
        System.out.println("\nSe transfiere 500.55 de Cuenta01 a Cuenta02");
        if ( cuenta01.transferencia(cuenta02, 500.55) ) {
            System.out.println("La Transferencia se ha realizado correctamente.");
        } else {
            System.out.println("No hay saldo suficiente para realizar la transferencia.");
        }
        
        System.out.println("\nLista de Cuentas:\n");
        
        for ( Cuenta unaCuenta : Arrays.asList(cuenta01,cuenta02) ) {
            System.out.println("Nro de Cuenta: "+unaCuenta.getNroCuenta());
            System.out.println("Nombre: "+unaCuenta.getNombre());
            System.out.println("Saldo: "+unaCuenta.getSaldo());
            System.out.println("----------------------");
        }
    }
}
