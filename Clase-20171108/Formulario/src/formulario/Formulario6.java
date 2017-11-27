package formulario;

import javax.swing.*;
import java.awt.Color;
import java.awt.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Formulario6 extends JFrame implements ActionListener {
	JLabel etiquetaRojo;
	JLabel etiquetaVerde;
	JLabel etiquetaAzul;
	JComboBox listaRojo;
	JComboBox listaVerde;
	JComboBox listaAzul;
	JButton boton;
	
	public Formulario6() {
		setLayout(null);
		
		etiquetaRojo = new JLabel("Rojo");
		etiquetaRojo.setBounds(50, 50, 100, 30);
		add(etiquetaRojo);
		
		etiquetaVerde = new JLabel("Verde");
		etiquetaVerde.setBounds(50, 100, 100, 30);
		add(etiquetaVerde);
		
		etiquetaAzul = new JLabel("Azul");
		etiquetaAzul.setBounds(50, 150, 100, 30);
		add(etiquetaAzul);
		
		listaRojo = new JComboBox();
		listaRojo.setBounds(150, 50, 100, 30);
		for (int unNro = 0; unNro < 256; unNro++) listaRojo.addItem(unNro);
		add(listaRojo);
		
		listaVerde = new JComboBox();
		listaVerde.setBounds(150, 100, 100, 30);
		for (int unNro = 0; unNro < 256; unNro++) listaVerde.addItem(unNro);
		add(listaVerde);
		
		listaAzul = new JComboBox();
		listaAzul.setBounds(150, 150, 100, 30);
		for (int unNro = 0; unNro < 256; unNro++) listaAzul.addItem(unNro);
		add(listaAzul);
		
		boton = new JButton("Aceptar");
		boton.setBounds(250, 200, 100, 30);
		boton.addActionListener(this);
		add(boton);
		
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		if ( e.getSource() == boton ) {
			int rojo = (int)listaRojo.getSelectedItem();
			int verde = (int)listaVerde.getSelectedItem();
			int azul = (int)listaAzul.getSelectedItem();
			boton.setBackground( new Color(rojo, verde, azul) );
		}
	}
	
	public static void main (String[] args) {
		Formulario6 formu6 = new Formulario6();
		formu6.setBounds(300, 300, 400, 400);
		formu6.setVisible(true);
		formu6.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
