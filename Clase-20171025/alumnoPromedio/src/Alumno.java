/*
Ingresar el nombre de un alumno y sus tres notas por teclado.
Generar los metodos que:
-Carguen los datos.
-Imprimir los datos.
-Calcular el promedio.
-Imprimir nombre, promedio y si aprobo o no.
*/

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Alumno {
    private String nombre;
    private List<Integer> notas;
    private Integer promedio = 0;
    private Scanner teclado;
    
    public void cargarDatos() {
        teclado = new Scanner(System.in);
        notas = new ArrayList();
        
        System.out.println("Ingresar Nombre:");
        nombre = teclado.next();
        
        for (int i=1; i<4; i++) {
            System.out.println("Ingresar Nota " + i + ":");
            notas.add( teclado.nextInt() );
        }
        
        System.out.println("");
    }
    
    public void imprimirDatos() {
        System.out.println("Nombre: " + nombre);
        System.out.print("Notas: ");
        
        for ( Integer unaNota : notas ) System.out.print(unaNota + ", ");
        
        System.out.println("\n");
    }
    
    public void calcularPromedio() {
        Integer cant_notas = notas.size();
        
        for ( Integer unaNota : notas ) promedio += unaNota;
        
        promedio /= cant_notas;
    }
    
    public void imprimirInforme() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Promedio: " + promedio);
        
        if ( promedio > 4 ) System.out.println("Alumno Aprobado");
        else System.out.println("Alumno a Marzo");
        
        System.out.println("");
    }
    
    public static void main(String[] args) {
        Alumno unAlumno = new Alumno();
        
        unAlumno.cargarDatos();
        unAlumno.imprimirDatos();
        unAlumno.calcularPromedio();
        unAlumno.imprimirInforme();
    }
}
