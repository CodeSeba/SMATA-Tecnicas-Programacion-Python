package formulario;

import javax.swing.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Formulario5 extends JFrame implements ActionListener {
	JLabel etiqueta1;
	JLabel etiqueta2;
	JTextField texto1;
	JComboBox lista1;
	JButton boton1;
	
	public Formulario5() {
		setLayout(null);
		
		etiqueta1 = new JLabel("Nombre:");
		etiqueta1.setBounds(50, 50, 100, 30);
		add(etiqueta1);
		
		etiqueta2 = new JLabel("Nacionalidad:");
		etiqueta2.setBounds(50, 100, 100, 30);
		add(etiqueta2);
		
		texto1 = new JTextField();
		texto1.setBounds(150, 50, 100, 30);
		add(texto1);
		
		lista1 = new JComboBox();
		lista1.setBounds(150, 100, 100, 30);
		lista1.addItem("Argentina");
		lista1.addItem("Bolivia");
		lista1.addItem("Colombia");
		lista1.addItem("Peruana");
		lista1.addItem("Venezuela");
		add(lista1);
		
		boton1 = new JButton("Aceptar");
		boton1.setBounds(300, 400, 100, 30);
		boton1.addActionListener(this);
		add(boton1);
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		if ( e.getSource() == boton1 ) {
			String nombre = texto1.getText();
			String nacion = (String)lista1.getSelectedItem();
			setTitle( "Nombre: "+nombre+" Nacionalidad: "+nacion );
		}
	}
	
	public static void main (String[] args) {
		Formulario5 formu5 = new Formulario5();
		formu5.setBounds(0, 0, 500, 500);
		formu5.setVisible(true);
	}
}
