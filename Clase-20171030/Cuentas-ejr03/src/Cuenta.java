/*
Crear una clase "Cuenta" con el constructor por defecto,
el constructor con paramatros, los metodos getter y setter,
y ademas los metodos "deposito", "extraccion" y "transferencia".

La clase cuenta tiene los siguientes datos:
-String, Nombre de cliente
-String, Numero de cuenta
-Saldo de la cuenta

El metodo deposito aumenta el saldo en la cantidad que se indique.
La cantidad no puede ser negativo.

El metodo extraccion disminuye el saldo de la cuenta en la cantidad
indicada. Pero antes se debe verificar que haya saldo suficiente.
La cantidad no puede ser negativa.

Los metodos deposito y extraccion devuelven True o False si se pudo
realizar la operacion.

El metodo transferencia permite pasar saldo de una cuenta a otra,
siempre que en la cuenta origen haya saldo suficiente.
*/

public class Cuenta {
    private String nombre;
    private String nroCuenta;
    private double saldo;

    // Constructor por defecto
    public Cuenta() {}

    // Constructor con parametros
    public Cuenta(String nombre, String nroCuenta, double saldo) {
        this.nombre = nombre;
        this.nroCuenta = nroCuenta;
        this.saldo = saldo;
    }
    
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNroCuenta() {
        return nroCuenta;
    }

    public void setNroCuenta(String nroCuenta) {
        this.nroCuenta = nroCuenta;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }
    
    public boolean deposito(double unMonto) {
        if ( unMonto > 0 ) {
            saldo += unMonto;
            return true;
        }
        else return false;
    }
    
    public boolean extraccion(double unMonto) {
        if ( unMonto <= saldo) {
            saldo -= unMonto;
            return true;
        }
        else return false;
    }
    
    public boolean transferencia(Cuenta cuentaDestino, double unMonto) {
        if ( saldo >= unMonto) {
            extraccion(unMonto);
            cuentaDestino.deposito(unMonto);
            return true;
        }
        else return false;
    }
}
