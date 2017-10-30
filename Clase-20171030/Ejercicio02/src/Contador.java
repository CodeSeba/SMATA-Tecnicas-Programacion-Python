/*
Crear una clase "Contador" con los metodos para
incrementar y decrementar el contador.

La clase contendra un consultor por defecto (sin parametros),
un constructor con parametros y los metodos
getter y setter.
*/

public class Contador {
    private int contador;

    public Contador() {
    }
    
    public Contador(int contador) {
        if ( contador < 0 ) { this.contador = 0; }
        else { this.contador = contador; }
    }

    public int getContador() {
        return contador;
    }

    public void setContador(int contador) {
        if ( contador < 0 ) { this.contador = 0; }
        else { this.contador = contador; }
    }
    
    public void incrementar() {
        contador++;
    }
    
    public void decrementar() {
        contador--;
        if ( contador < 0 ) { contador = 0; }
    }
}

