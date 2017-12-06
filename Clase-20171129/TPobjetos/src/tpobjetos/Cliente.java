package tpobjetos;

import java.util.ArrayList;
import java.util.List;

public class Cliente {
    private int dni;
    private String nombre;
    private double saldo;
    private List libros;
    
    public Cliente() {
        libros = new ArrayList();
        saldo = 100;
    }
    
    public void aplicarSaldo(double credito) {
        saldo += credito;
    }

	public int getDni() {
		return dni;
	}

	public void setDni(int dni) {
		this.dni = dni;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public double getSaldo() {
		return saldo;
	}

	public void setSaldo(double saldo) {
		this.saldo = saldo;
	}

	public List getLibros() {
		return libros;
	}

	public void setLibros(List libros) {
		this.libros = libros;
	}
    
}