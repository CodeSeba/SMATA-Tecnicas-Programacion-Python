package publicaciones;

//import publicaciones.Publicaciones;

public class Libro extends Publicaciones implements Prestable{
	private boolean prestado;
	
	public Libro(int codigo, String titulo, String publicacion) {
		super(codigo,titulo,publicacion);
	}
	
	public Libro() { super(); }

	public boolean getPrestado() { return prestado; }

	public void setPrestado(boolean prestado) { this.prestado = prestado; }
	
	@Override
	public boolean esPrestado() { return getPrestado(); }
	
	@Override
	public void prestar() { setPrestado(true); }
	
	@Override
	public void devolver() { setPrestado(true); } 
}
