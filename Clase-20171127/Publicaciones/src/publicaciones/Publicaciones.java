package publicaciones;

public class Publicaciones {
	private int codigo;
	private String titulo;
	private String publicacion;

	public Publicaciones() {}
	
	public Publicaciones(int codigo, String titulo, String publicacion) {
		this.codigo = codigo;
		this.titulo = titulo;
		this.publicacion = publicacion;
	}

	public String getPublicacion() { return publicacion; }

	public void setPublicacion(String publicacion)
		{ this.publicacion = publicacion; }

	public int getCodigo() { return codigo; }

	public void setCodigo(int codigo)
		{ this.codigo = codigo; }

	public String getTitulo() {	return titulo; }

	public void setTitulo(String titulo)
		{ this.titulo = titulo; }
}
