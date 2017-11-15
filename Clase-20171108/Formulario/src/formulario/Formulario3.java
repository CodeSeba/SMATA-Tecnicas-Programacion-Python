package formulario;

import javax.swing.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Formulario3 extends JFrame implements ActionListener {
	JLabel etiqueta1;
	JButton boton1;
	JTextField texto1;
	
	public Formulario3() {
		setLayout(null);
		
		etiqueta1 = new JLabel("Nombre:");
		etiqueta1.setBounds(100, 50, 100, 30);
		add(etiqueta1);
		
		boton1 = new JButton("Aceptar");
		boton1.setBounds(50, 120, 100, 30);
		add(boton1);
		boton1.addActionListener(this);
		
		texto1 = new JTextField("unNombre");
		texto1.setBounds(200, 50, 100, 30);
		add(texto1);
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		if ( e.getSource() == boton1 ) setTitle( texto1.getText() );
	}
	
	public static void main (String[] args) {
		Formulario3 formu3 = new Formulario3();
		formu3.setBounds(0, 0, 500, 500);
		formu3.setVisible(true);
	}
}
