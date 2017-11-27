package formulario;

import javax.swing.JOptionPane;

public class Principal {
	public static void main(String[] args) {
		String nombre;
		int edad;

		nombre = JOptionPane.showInputDialog(null, "Ingresar Nombre:");
		edad = Integer.parseInt(JOptionPane.showInputDialog(null, "Ingresar Edad:"));	
		
		JOptionPane.showMessageDialog(null, "Nombre: "+nombre+"\nEdad: "+edad,
				"Datos de la Persona",JOptionPane.INFORMATION_MESSAGE);
		
		JOptionPane.showConfirmDialog(null, "Nombre: "+nombre+"\nEdad: ",
				"Confirmar Datos", JOptionPane.YES_NO_OPTION);
	}
}
