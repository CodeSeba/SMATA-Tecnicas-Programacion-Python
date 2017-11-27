package formulario;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class Formulario9 extends JFrame implements ActionListener {
	JLabel lNombre;
	JTextField tfNombre;
	
	JLabel lSexo;
	ButtonGroup bgSexo;
	JRadioButton rbFemenino, rbMasculino;
	
	JLabel lNacionalidad;
	JComboBox cobNacionalidad;
	
	JLabel lNacimiento, lDia, lMes, lAnio;
	JComboBox cobDia, cobMes, cobAnio;
	
	JLabel lIdiomas;
	JCheckBox chbIdioma1, chbIdioma2, chbIdioma3, chbIdioma4;
	
	JButton bLimpiar, bGuardar;
	
	private List<String> listaNac;
	
	private void cargarListaNac() {
		listaNac = new ArrayList();
		for ( String nac : Arrays.asList(	"Argentina",
											"Bolivia",
											"Colombia",
											"Peru",
											"Venezuela") )
			listaNac.add(nac);
	}
	
	public Formulario9 () {
		setLayout(null);
		int x, y = x = 10;
		int w = 150, h = 24;
		int pad = 10;
		
		lNombre = new JLabel("Nombre");
		lNombre.setBounds(x, y, w, h);
		add(lNombre);
		
		tfNombre = new JTextField();
		tfNombre.setBounds(x+w, y, w, h);
		add(tfNombre);
		
		lSexo = new JLabel("Genero");
		y += h + pad;
		lSexo.setBounds(x, y, w, h);
		add(lSexo);
		
		rbFemenino = new JRadioButton("Femenino");
		y += h + pad;
		rbFemenino.setBounds(x, y, w, h);
		rbMasculino = new JRadioButton("Masculino");
		y += h + pad;
		rbMasculino.setBounds(x, y, w, h);
		
		bgSexo = new ButtonGroup();
		for ( JRadioButton rb : Arrays.asList(rbFemenino,rbMasculino) ) {
			add(rb);
			bgSexo.add(rb);
		}
		
		lNacionalidad = new JLabel("Nacionalidad");
		y += h + pad;
		lNacionalidad.setBounds(x, y, w, h);
		add(lNacionalidad);
		
		cobNacionalidad = new JComboBox();
		y += h + pad;
		cobNacionalidad.setBounds(x, y, w-pad, h);
		cargarListaNac();
		for ( String nac : listaNac ) cobNacionalidad.addItem(nac);
		add(cobNacionalidad);
		
		lNacimiento = new JLabel("Fecha de Nacimiento");
		y += h + pad;
		lNacimiento.setBounds(x, y, w, h);
		add(lNacimiento);
		
		lDia = new JLabel("Dia");
		y += h + pad;
		lDia.setBounds(x, y, w, h);
		add(lDia);
		
		cobDia = new JComboBox();
		cobDia.setBounds(x+w, y, w, h);
		for ( int i=1 ; i<32 ; i++ ) cobDia.addItem(i);
		add(cobDia);
		
		lMes = new JLabel("Mes");
		y += h + pad;
		lMes.setBounds(x, y, w, h);
		add(lMes);
		
		cobMes = new JComboBox();
		cobMes.setBounds(x+w, y, w, h);
		for ( int i=1 ; i<13 ; i++ ) cobMes.addItem(i);
		add(cobMes);
		
		lAnio = new JLabel("Año");
		y += h + pad;
		lAnio.setBounds(x, y, w, h);
		add(lAnio);
		
		cobAnio = new JComboBox();
		cobAnio.setBounds(x+w, y, w, h);
		for ( int i=1950 ; i<2017 ; i++ ) cobAnio.addItem(i);
		add(cobAnio);
		
		bLimpiar = new JButton("Limpiar");
		x += w*2 + pad*2;
		y += h + pad*5;
		bLimpiar.setBounds(x, y, w, h);
		bLimpiar.addActionListener(this);
		add(bLimpiar);
		
		bGuardar = new JButton("Guardar");
		bGuardar.setBounds(x+w+pad, y, w, h);
		bGuardar.addActionListener(this);
		add(bGuardar);
		
		lIdiomas = new JLabel("Idiomas");
		y = 10;
		lIdiomas.setBounds(x, y, w, h);
		add(lIdiomas);
		
		chbIdioma1 = new JCheckBox("Ingles");
		y += h + pad;
		chbIdioma1.setBounds(x, y, w, h);
		add(chbIdioma1);
		
		chbIdioma2 = new JCheckBox("Frances");
		y += h + pad;
		chbIdioma2.setBounds(x, y, w, h);
		add(chbIdioma2);
		
		chbIdioma3 = new JCheckBox("Italiano");
		y += h + pad;
		chbIdioma3.setBounds(x, y, w, h);
		add(chbIdioma3);
		
		chbIdioma4 = new JCheckBox("Aleman");
		y += h + pad;
		chbIdioma4.setBounds(x, y, w, h);
		add(chbIdioma4);
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		if ( e.getSource() == bLimpiar ) {
			setTitle("Limpiado");
		}
		else if ( e.getSource() == bGuardar ) {
			setTitle("Guardado");
		}
	}
	
	public static void main (String[] args) {
		Formulario9 formu9 = new Formulario9();
		
		formu9.setBounds(300, 300, 660, 460);
		formu9.setVisible(true);
		formu9.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
