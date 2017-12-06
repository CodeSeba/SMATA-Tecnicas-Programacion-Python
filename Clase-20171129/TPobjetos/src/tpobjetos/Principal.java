package tpobjetos;

import java.util.Arrays;

public class Principal {
    
	public static void main(String[] args) {
		Cliente unCliente = new Cliente();
		
		unCliente.setDni(12345678);
		unCliente.setNombre("Pepe");
		unCliente.setLibros(Arrays.asList("libro1","libro2","libro3"));
		
		VIP unVip = new VIP(unCliente);
		
		System.out.println("DNI: "+unVip.getDni());
		System.out.println("Nombre: "+unVip.getNombre());
		System.out.println("Libros: "+unVip.getLibros());
		System.out.println("Saldo: "+unVip.getSaldo());
		System.out.println("Dto: "+unVip.getDto());
	}
}
