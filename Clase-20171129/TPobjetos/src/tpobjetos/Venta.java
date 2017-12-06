package tpobjetos;

public class Venta {
    // int codigo;
	Cliente unCliente;
    Libro unLibro;
    double monto;

    public Venta(Cliente unCliente)
		{ this.unCliente = unCliente; }
    
    public void calcularMonto() {
		int descuento = 100;
		
		if ( unCliente instanceof VIP)
			descuento -= ((VIP)unCliente).getDto();
		
		monto = unLibro.getPrecio() * descuento / 100;
	}
	
	public void venderLibro(){
		// completar
	}
}
