package formulario;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Formulario1 extends JFrame implements ActionListener {
	JLabel etiqueta1;
	JButton boton1;
	
	public Formulario1() {
		setLayout(null);
		
		etiqueta1 = new JLabel("Hola Mundo");
		etiqueta1.setBounds(50, 50, 100, 30);
		add(etiqueta1);
		
		boton1 = new JButton("Aceptar");
		boton1.setBounds(50, 120, 200, 100);
		add(boton1);
		boton1.addActionListener(this);
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		if ( e.getSource() == boton1 ) setTitle("Hola Mundo.");
	}
	
	public static void main (String[] args) {
		Formulario1 formu1 = new Formulario1();
		formu1.setBounds(0, 0, 600, 400);
		formu1.setVisible(true);
	}
}
