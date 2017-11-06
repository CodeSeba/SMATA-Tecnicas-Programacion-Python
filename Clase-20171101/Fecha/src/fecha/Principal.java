package fecha;
import java.util.Scanner;

public class Principal {
	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		Fecha fecha01 = new Fecha();
		Fecha fecha02 = new Fecha(30, 6, 2015);
		int d,m,a,s;
		boolean fechaOK,listo;
		
		// Uso de esBisiesto()
		a = 1950;
		while ( ! fecha01.esBisiesto(a) ) a++;
		
		// Fecha con año bisiesto
		Fecha fecha03 = new Fecha(28,2,a);
		
		// Ingreso por teclado
		do {
			System.out.println("Ingrese un Dia:");
			d = teclado.nextInt();
			System.out.println("Ingrese un Mes:");
			m = teclado.nextInt();
			System.out.println("Ingrese un Año:");
			a = teclado.nextInt();
			
		// Uso de fechaCorrecta()
			if ( fechaOK = fecha01.fechaCorrecta(d, m, a) ) {
				System.out.println("\nLa fecha ingresada es correcta.\n");
			} else {
				System.out.println("\nLa fecha ingresada NO es correcta.");
				System.out.println("Intente nuevamente.\n");
			}
		} while ( ! fechaOK );
		
		// Uso de setters
		fecha01.setDia(d);
		fecha01.setMes(m);
		fecha01.setAño(a);
		
		// Uso de getters
		System.out.println("Dia: " + fecha01.getDia());
		System.out.println("Mes: " + fecha01.getMes());
		System.out.println("Año: " + fecha01.getAño());
                System.out.println("");
		
		// Uso de imprimrFecha()
		System.out.println("Fecha de ejemplo:");
		fecha02.imprimirFecha();
		System.out.println("\n");
		
		System.out.println("Fecha con año bisiesto: ");
		fecha03.imprimirFecha();
		System.out.println("\n");
		
		// Uso de diaSiguiente()
		System.out.println("Se agrega un dia: ");
		fecha03.diaSiguiente();
		fecha03.imprimirFecha();
		System.out.println("\n");
		
		// Uso de toString()
                System.out.println("Impresion de fecha usando toString:");
                System.out.println( fecha01.toString() );
	}
}