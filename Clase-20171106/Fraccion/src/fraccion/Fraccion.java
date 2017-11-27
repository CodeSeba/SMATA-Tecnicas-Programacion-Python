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
			System.out.println("ERROR: Denominador igual a cero.");
			return false;
		}
		else return true;
	}
	
	public int getNumerador() { return numerador; }
	public int getDenominador() { return denominador; }
	public void setNumerador(int numerador) { this.numerador = numerador; }
	public void setDenominador(int denominador) { this.denominador = denominador; }
	
	
	
	private int maximoComunDivisor() {
		int u,v,r;
		
		if (numerador < 0) u= -1 * numerador;
		else u = numerador;
		
		if (denominador < 0) v= -1 * denominador;
		else v = denominador;
		
		if ( v == 0 ) return u;
		
		while ( v != 0 ) {
			r = u % v;
			u = v;
			v = r;
		}
		
		return u;
	}
	
	public Fraccion simplifica() {
		int mcd = maximoComunDivisor();
		
		numerador /= mcd;
		denominador /= mcd;
		
		return this;
	}
	
	public Fraccion suma(Fraccion otraFraccion) {
		int num1 = numerador;
		int num2 = otraFraccion.getNumerador();
		int den1 = denominador;
		int den2 = otraFraccion.getDenominador();
		
		
		int sumaNum = num1 * den2 + num2 * den1;
		int sumaDen = den1 * den2;
		
		setNumerador(sumaNum);
		setDenominador(sumaDen);
		simplifica();
		
		return this;
	}
	
	public Fraccion resta(Fraccion otraFraccion) {
		int num2 = otraFraccion.getNumerador();
		
		otraFraccion.setNumerador(-1 * num2);
		
		return suma(otraFraccion);
	}
	
	public Fraccion multiplica(Fraccion otraFraccion) {
		int num1 = numerador;
		int num2 = otraFraccion.getNumerador();
		int den1 = denominador;
		int den2 = otraFraccion.getDenominador();
		
		setNumerador(num1 * num2);
		setDenominador(den1 * den2);
		simplifica();
		
		return this;
	}
	
	public Fraccion divide(Fraccion otraFraccion) {
		int num2 = otraFraccion.getNumerador();
		int den2 = otraFraccion.getDenominador();
		
		otraFraccion.setNumerador(den2);
		otraFraccion.setDenominador(num2);
		
		return multiplica(otraFraccion);
	}
}