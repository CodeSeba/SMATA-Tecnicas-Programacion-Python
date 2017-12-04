package gestion;

public class Digital extends Libro{
    private int licencia;
    String formato;

    public Digital(int codigo) {
        super(codigo);
    }

    public int getLicencia() {
        return licencia;
    }

    public void setLicencia(int licencia) {
        this.licencia = licencia;
    }
}
