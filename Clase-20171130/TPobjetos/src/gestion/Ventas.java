package gestion;
public class Ventas {
    Cliente comprador;
    Libro item;
    int fecha;
    double monto;

    public Ventas(Cliente comprador, Libro item) {
        this.comprador = comprador;
        this.item = item;
        this.monto=item.getPrecio();
    }
    
    public double getMonto(){
    return monto;
    }
    public void aplicarDesc(){
        VIP unvip=new VIP();
        if (comprador.equals(unvip)){ //equals es para comparar dos obj de clases diferentes
          monto=item.getPrecio() * 0.8;
        }
    }
}
