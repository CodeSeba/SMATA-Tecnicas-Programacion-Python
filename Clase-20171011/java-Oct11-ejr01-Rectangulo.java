import java.util.scanner;

public class Rectangulo {
	public static void main (String[] args) {
		double l1 = 0;
		double l2 = 0;
		double perimetro = 0;
		double area = 0;
		Scanner teclado = new Scanner( System.in );

		System.out.println("Ingresar lado 1");
		l1 = teclado.nextDouble();
		System.out.println("Ingresar lado 2");
		l2 = teclado.nextDouble();
		
		perimetro = 2 * ( l1 + l2 );
		area = l1 * l2;

		System.out.println("El perimetro del Rectangulo es: " + perimetro);
		System.out.println("El area del Rectangulo: " + area);
	}
}