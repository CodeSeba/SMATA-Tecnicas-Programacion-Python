package tpobjetos;

public class VIP extends Cliente{
    int descuento;

    public VIP () {}
    
	public VIP(int descuento) {
        this.descuento = descuento;
    }
	
    public VIP (Cliente unCliente){
		super.setDni(unCliente.getDni());
		super.setNombre(unCliente.getNombre());
		super.setSaldo(unCliente.getSaldo());
		super.setLibros(unCliente.getLibros());
		descuento = 20;
    }
	
	public int getDto() { return descuento; }
	public void setDto(int dto) { descuento = dto; }
	
}
