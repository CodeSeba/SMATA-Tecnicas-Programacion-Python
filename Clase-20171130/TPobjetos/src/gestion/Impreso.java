package gestion;

public class Impreso extends Libro{
    private int copias;
    int paginas;
    String tapa;

    public Impreso(int codigo) {
        super(codigo);
    }

    public int getCopias() {
        return copias;
    }

    public void setCopias(int copias) {
        this.copias = copias;
    }
	
	public int consultarStock() {
		return getCopias();
	}
}
