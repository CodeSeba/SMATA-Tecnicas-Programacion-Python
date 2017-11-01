public class Balacera {
    public static void main (String[] args) {
        
        PuebloDelOeste laFerrere = new PuebloDelOeste();
        
        laFerrere.cantinas = 2;
        laFerrere.comisarios = 1;
        laFerrere.alborotadores = 5;
        
        Villanos unVillano = new Villanos();
        unVillano.colorBigote = "azul";
        unVillano.colorSombrero = "amarillo";
        unVillano.nombreCaballo = "Peña";
        unVillano.marcaWhiskey = "Jack Daniels";
        unVillano.sexo = "hombre";
        unVillano.nombre = "Mauricio";
        
        Humanos unaDamicela = new Humanos();
        unaDamicela.sexo = "mujer";
        unaDamicela.nombreCaballo = "Estrella";
        unaDamicela.marcaWhiskey = "Chivas";
        unaDamicela.nombre = "Maria";
        
        unVillano.tomarWhiskey();
        System.out.println("El nivel de ebriedad de "+unVillano.nombre+" es: "+unVillano.queTanEbrioEsta());
        unVillano.secuestrarDamisela(unaDamicela);
    }
}
