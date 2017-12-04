package gestion;
import java.util.ArrayList;
import java.util.List;
public class Libreria {
    String nombre;
    String direccion;
    int telefono;
    private List clientes;
    private List libros;
    float caja;

    public Libreria() {
        clientes=new ArrayList();
        libros=new ArrayList();
    }

    public List getClientes() {
        return clientes;
    }

    public List getLibros() {
        return libros;
    }

    public void setClientes(List clientes) {
        this.clientes = clientes;
    }

    public void setLibros(List libros) {
        this.libros = libros;
    }
    public void agregarCliente(Cliente c){
        clientes.add(c);
    }
    public void agregarLibro(Libro l){
        libros.add(l);
    }
}

