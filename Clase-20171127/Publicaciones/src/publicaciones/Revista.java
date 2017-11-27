package publicaciones;

import publicaciones.Publicaciones;

public class Revista extends Publicaciones {
	private int nroRevista;
	
	public Revista(int codigo, String titulo, String publicacion) {
		super(codigo,titulo,publicacion);
	}
	
	public Revista() { super(); }

	public int getNroRevista() { return nroRevista; }

	public void setNroRevista(int nroRevista)
		{ this.nroRevista = nroRevista; }
}
