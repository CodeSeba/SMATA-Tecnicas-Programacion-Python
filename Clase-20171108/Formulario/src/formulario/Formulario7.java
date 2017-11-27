package formulario;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ItemListener;
import java.awt.event.ItemEvent;
import java.util.Arrays;

public class Formulario7 extends JFrame implements ItemListener {
	JLabel lenguajes;
	JCheckBox java;
	JCheckBox python;
	JCheckBox javascript;
	JCheckBox cpp;
	
	public Formulario7 () {
		setLayout(null);
		
		lenguajes = new JLabel("Lenguajes:");
		lenguajes.setBounds(50, 50, 100, 30);
		add(lenguajes);
		
		java = new JCheckBox("Java");
		java.setBounds(150, 50, 100, 30);
		java.addItemListener(this);
		add(java);
		
		python = new JCheckBox("Python");
		python.setBounds(150, 100, 100, 30);
		python.addItemListener(this);
		add(python);
		
		javascript = new JCheckBox("Javascript");
		javascript.setBounds(150, 150, 100, 30);
		javascript.addItemListener(this);
		add(javascript);
		
		cpp = new JCheckBox("C++");
		cpp.setBounds(150, 200, 100, 30);
		cpp.addItemListener(this);
		add(cpp);
	}
	
	@Override
	public void itemStateChanged(ItemEvent e) {
		
		for ( JCheckBox unaOpcion : Arrays.asList(java,python,javascript,cpp) ) {
			
			if ( e.getSource() == unaOpcion ) {
				
				setTitle( unaOpcion.getText() );
			}
		}
	}
	
	public static void main (String[] args) {
		Formulario7 formu7 = new Formulario7();
		formu7.setBounds(300, 300, 400, 400);
		formu7.setVisible(true);
		formu7.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
