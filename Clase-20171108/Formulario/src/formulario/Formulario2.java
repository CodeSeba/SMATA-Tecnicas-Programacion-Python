package formulario;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Formulario2 extends JFrame implements ActionListener {
	JLabel etiqueta1;
	JButton botonRojo;
	JButton botonAzul;
	JButton botonVerde;
	
	public Formulario2() {
		setLayout(null);
		
		etiqueta1 = new JLabel("RGB");
		etiqueta1.setBounds(100, 50, 100, 30);
		add(etiqueta1);
		
		botonRojo = new JButton("Rojo");
		botonRojo.setBounds(50, 120, 100, 80);
		add(botonRojo);
		botonRojo.addActionListener(this);
		
		botonAzul = new JButton("Azul");
		botonAzul.setBounds(170, 120, 100, 80);
		add(botonAzul);
		botonAzul.addActionListener(this);
		
		botonVerde = new JButton("Verde");
		botonVerde.setBounds(290, 120, 100, 80);
		add(botonVerde);
		botonVerde.addActionListener(this);
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		if ( e.getSource() == botonRojo ) setTitle("Rojo");
		
		if ( e.getSource() == botonAzul ) setTitle("Azul");
		
		if ( e.getSource() == botonVerde ) setTitle("Verde");
	}

	
	public static void main (String[] args) {
		Formulario2 formu2 = new Formulario2();
		formu2.setBounds(0, 0, 600, 400);
		formu2.setVisible(true);
	}
}
