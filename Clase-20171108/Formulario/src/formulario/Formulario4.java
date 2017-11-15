package formulario;

import javax.swing.*;
import java.awt.event.*;
import java.awt.event.ItemListener;

public class Formulario4 extends JFrame implements ItemListener {
	JComboBox lista;
	
	public Formulario4() {
		setLayout(null);
		
		lista = new JComboBox();
		lista.setBounds(100, 100, 100, 30);
		add(lista);
		
		lista.addItem("Java");
		lista.addItem("Python");
		lista.addItem("C++");
		lista.addItem("BD");
		
		lista.addItemListener(this);
	}
	
	@Override
	public void itemStateChanged(ItemEvent e) {
		if ( e.getSource() == lista ) {
			String seleccion = (String)lista.getSelectedItem();
			setTitle(seleccion);
		}
	}
	
	public static void main (String[] args) {
		Formulario4 formu4 = new Formulario4();
		formu4.setBounds(0, 0, 500, 500);
		formu4.setVisible(true);
	}
}
