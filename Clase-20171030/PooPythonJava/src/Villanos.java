public class Villanos extends Humanos {
    String colorBigote;
    String colorSombrero;
    String aspecto;
    int ebriedad;
    int numeroDamiselas;
    Humanos damisela;
    
    public Villanos() {
        aspecto = "Malo";
        ebriedad = 0;
        numeroDamiselas = 0;
    }
    
    // Setter
    public void tomarWhiskey() {
        ebriedad++;
    }
    
    // Getter
    public int queTanEbrioEsta() {
        return ebriedad;
    }
    
    public void secuestrarDamisela(Humanos damisela) {
        this.damisela = damisela;
        numeroDamiselas++;
        System.out.println("El villano "+nombre+" secuestro a "+damisela.comoTeLlamas());
    }
}