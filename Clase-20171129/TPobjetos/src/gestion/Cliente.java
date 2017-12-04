package gestion;

import java.util.ArrayList;
import java.util.List;

public class Cliente {
    int dni;
    String nombre;
    double saldo;
    List libros;
    
    public Cliente() {
        libros = new ArrayList();
        saldo = 100;
    }
    
    public void aplicarSaldo(double credito) {
        saldo += credito;
    }
    public VIP membresia() {
        int cant=librosComprados.size(); //size es para el tamaño o cuenta la lista, en otros lenguajes es cout
        if (cant>=15){
            VIP auxiliar=new VIP(this);
            return auxiliar;
        }else{
            System.out.println("Cliente no calificado. Membresía normal");;
        }
    }
}    
    /* public Cliente(String nombre, String usuario, int dni){//constructor con parametros
        this.nombre=nombre;
        this.usuario=usuario;
        this.dni=dni;
    
    }
    */
