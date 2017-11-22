package formulario;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ItemListener;
import java.awt.event.ItemEvent;
import java.util.Arrays;

public class Formulario8 extends JFrame implements ItemListener {
	JLabel estadocivil;
	JRadioButton
			casado,
			soltero,
			viudo,
			separado,
			concuvinato,
			masculino,
			femenino;
	ButtonGroup bg1, bg2;
	
	public Formulario8 () {
		setLayout(null);
		setBackground(Color.magenta);
		
		estadocivil = new JLabel("Estado Civil:");
		estadocivil.setBounds(50, 50, 100, 30);
		add(estadocivil);
		
		casado = new JRadioButton("Casado");
		casado.setBounds(150, 50, 100, 30);
		casado.addItemListener(this);
		add(casado);
		
		soltero = new JRadioButton("Soltero");
		soltero.setBounds(150, 100, 100, 30);
		soltero.addItemListener(this);
		add(soltero);
		
		viudo = new JRadioButton("Viudo");
		viudo.setBounds(150, 150, 100, 30);
		viudo.addItemListener(this);
		add(viudo);
		
		concuvinato = new JRadioButton("Concuvinato");
		concuvinato.setBounds(150, 200, 150, 30);
		concuvinato.addItemListener(this);
		add(concuvinato);
		
		masculino = new JRadioButton("Masculino");
		masculino.setBounds(200, 50, 150, 30);
		masculino.addItemListener(this);
		add(masculino);
		
		femenino = new JRadioButton("Femenino");
		femenino.setBounds(200, 100, 150, 30);
		femenino.addItemListener(this);
		add(femenino);
		
		bg1 = new ButtonGroup();
		bg1.add(casado);
		bg1.add(soltero);
		bg1.add(viudo);
		bg1.add(concuvinato);
	}
	
	@Override
	public void itemStateChanged(ItemEvent e) {
		
		for ( JRadioButton unaOpcion : Arrays.asList(casado,soltero,viudo,concuvinato) ) {
			
			if ( e.getSource() == unaOpcion ) {
				
				setTitle( unaOpcion.getText() );
			}
		}
	}
	
	public static void main (String[] args) {
		Formulario8 formu8 = new Formulario8();
		System.out.println(formu8.getBackground());
		formu8.setBounds(300, 300, 400, 400);
		formu8.setVisible(true);
		formu8.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
