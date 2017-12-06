package tpobjetos;

public class Libro {
   String autor;
   private String titulo;
   private int codigo;
   private double precio;
   String editorial;

    public Libro(int codigo) {
        this.codigo = codigo;
    }

    public String getTitulo() {
        return titulo;
    }

    public int getCodigo() {
        return codigo;
    }

    public double getPrecio() {
        return precio;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public void setPrecio(float precio) {
        this.precio = precio;
    }
    
   
}
