package fraccion;

/*
Crear una clase "Fraccion" para sumar, restar,
multiplicar y dividir fracciones.
La clase tiene dos atributos de tipo entero.
-Numerador
-Denominador
La clase "Fraccion" debe tener los constructores
y los metodos adecuados para funcionar en "Main".
*/

public class Fraccion {
	private int numerador;
	private int denominador;
	
	public Fraccion () {
		numerador = 0;
		denominador = 1;
	}

	public Fraccion(int numerador, int denominador) {
		this.numerador = numerador;
		this.denominador = denominador;
	}
	
	private boolean validarDenominador(int unDenominador) {
		if ( unDenominador == 0 ) {
			System.out.println("ERROR: Denominaodr igual a cero.");
			return false;
		}
		else return true;
	}
	
	public int getNumerador() { return numerador; }
	public int getDenominador() { return denominador; }
	public void setNumerador(int numerador) { this.numerador = numerador; }
	public void setDenominador(int denominador) { this.denominador = denominador; }
	
	
	
	private int maximoComunDenominador(int denominador1, int denominador2) {
		
	}
	
	public Fraccion simplifica() {
		
	}
	
	public Fraccion suma(Fraccion otraFraccion) {
		int operando1 = numerador;
		int operando2 = otraFraccion.getNumerador();
		int denominadorComun = maximoComunDenominador(operando1, operando2);
		
		int suma = (operando1 + operando2) * denominadorComun;
		
		Fraccion resultado = new Fraccion(suma,denominadorComun);
		
		return resultado.simplifica();
	}
	
	public Fraccion resta(Fraccion otraFraccion) {
		int numerador = otraFraccion.getNumerador();
		
		otraFraccion.setNumerador(-1 * numerador);
		
		return suma(otraFraccion);
	}
	
	public Fraccion multiplica(Fraccion otraFraccion) {
		int numerador2 = otraFraccion.getNumerador();
		int denominador2 = otraFraccion.getDenominador();
		
		Fraccion resultado = new Fraccion(numerador * numerador2, denominador * denominador2);
		
		return resultado.simplifica();
	}
	
	public Fraccion divide(Fraccion otraFraccion) {
		int numerador2 = otraFraccion.getNumerador();
		int denominador2 = otraFraccion.getDenominador();
		
		otraFraccion.setNumerador(denominador2);
		otraFraccion.setDenominador(numerador2);
		
		return multiplica(otraFraccion);
	}
}