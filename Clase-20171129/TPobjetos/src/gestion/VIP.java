package gestion;
public class VIP extends Cliente{
    int descuento;

    public VIP () {}
    
	public VIP(int descuento) {
        this.descuento = descuento;
    }
	
    public VIP (Cliente unCliente){
        dni = unCliente.dni;
        libros = unCliente.libros;
        saldo = unCliente.saldo;
        descuento = 20;
    }

}
