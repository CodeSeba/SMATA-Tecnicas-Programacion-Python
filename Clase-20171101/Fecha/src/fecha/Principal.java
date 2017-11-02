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
		
		// Uso de imprimrFecha()
		System.out.println("\nFecha de ejemplo:");
		fecha02.imprimirFecha();
		System.out.println("");
		
		System.out.println("\nFecha con año bisiesto: ");
		fecha03.imprimirFecha();
		System.out.println("");
		
		// Uso de diaSiguiente()
		System.out.println("Se agrega un dia: ");
		fecha03.diaSiguiente();
		fecha03.imprimirFecha();
		System.out.println("");
		
		System.out.println("\nMini juego.");
		System.out.println("Ingresar un año y el sistema mostrara la fechas");
		System.out.println("hasta que llegue al siguiente 29-02-AAAA.\n");
		
		do {
			System.out.println("Ingrese un Año:");
			a = teclado.nextInt();
			if ( a < 1 ) {
				System.out.println("\nEl año ingresado NO es correcto.");
				System.out.println("Intente nuevamente.\n");
			}
		} while ( a < 1 );
		
		fecha02.setDia(1);
		fecha02.setMes(1);
		fecha02.setAño(a);
		listo = false;
		s = 1000;
		System.out.println("");
		
		do {
			fecha02.imprimirFecha();
			fecha02.diaSiguiente();
						
			d = fecha02.getDia();
			m = fecha02.getMes();
			a = fecha02.getAño();
			listo = ( d == 29 && m == 2 && fecha02.esBisiesto(a) );
			
			// Sleep, para pausar la ejecucion
			try {
				Thread.sleep(s);
				s -= 25;
				if ( s < 0 ) s = 25;
			} catch (InterruptedException e) {}
			
			System.out.print("\n");
			
		} while ( ! listo );
		
		fecha02.imprimirFecha();
		System.out.println("\n\nGAME OVER\n");
	}
}