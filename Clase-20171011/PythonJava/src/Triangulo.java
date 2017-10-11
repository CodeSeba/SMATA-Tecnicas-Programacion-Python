import java.util.Scanner;

public class Triangulo {
	public static void main (String[] args) {
		double l1 = 0;
		double l2 = 0;
		double l3 = 0;
		double perimetro = 0;
		double area = 0;
		double semisuma = 0;
		Scanner teclado = new Scanner( System.in );

		System.out.println("Ingresar lado 1");
		l1 = teclado.nextDouble();
		System.out.println("Ingresar lado 2");
		l2 = teclado.nextDouble();
		System.out.println("Ingresar lado 3");
		l3 = teclado.nextDouble();

		perimetro = l1 + l2 +l3;
		semisuma = perimetro / 2;
		area = Math.sqrt(semisuma * (semisuma - l1) * (semisuma - l2) * (semisuma -l3));

		System.out.println("El perimetro del Triangulo es: " + perimetro);
		System.out.println("El area del Triangulo: " + area);
	}
}