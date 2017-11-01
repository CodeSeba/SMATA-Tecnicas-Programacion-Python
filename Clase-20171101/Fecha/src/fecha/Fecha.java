package fecha;

/*
Crear un clase "Fecha" en Java.
La clase tiene 3 atributos de tipo Int.
-Dia
-Mes
-Año
La clase va a tener el constructor por defecto,
el constructor con parametros, los getter y setter.
El metodo "fechaCorrecta" que devuelve un valor de tipo booleano
si la fecha es correcta o no.
Este metodo utiliza el metodo "esBisiesto",
"esBisiesto" tambien en un metodo booleano.
Un metodo "diaSiguiente" cambia la fecha actual con la del dia siguiente.
Este metodo debe dejar siempre siempre una fecha consistente.
Debe haber un metodo imprimir que muestre las fechas de la forma
"dd-mm-aaaa", si el dia o mes es un digito se agrega un cero delante.
Escribir un programa si la clase fecha funciona correctamente.
*/

import java.util.HashMap;
import java.util.Map;

public class Fecha {
    
    private int dia,mes,año;
    private Map<Integer,Integer> mesesDias = new HashMap<>();
    
    mesesDias.put(1, 31);
    mesesDias.put(2, 28);
    mesesDias.put(3, 31);
    mesesDias.put(4, 30);
    mesesDias.put(5, 31);
    mesesDias.put(6, 30);
    mesesDias.put(7, 31);
    mesesDias.put(8, 31);
    mesesDias.put(9, 30);
    mesesDias.put(10, 31);
    mesesDias.put(11, 30);
    mesesDias.put(12, 31);
    
    public Fecha() {}
    
    public Fecha(int dia, int mes, int año) {
        this.dia = dia;
        this.mes = mes;
        this.año = año;
    }
    
    public int getDia() { return dia; }
    public void setDia(int dia) { this.dia = dia; }
    public int getMes() { return mes; }
    public void setMes(int mes) { this.mes = mes; }
    public int getAño() { return año; }
    public void setAño(int año) { this.año = año; }
    
    public boolean fechaCorrecta(int dia, int mes, int año) {
        boolean fechaOK = true;
        
        if ( esBisiesto(año) ) mesesDias.put(2, 29);
                        
        if (año < 1) fechaOK = false;
        if (mes < 1 || mes > 12) fechaOK = false;
        
        int diasDelMes = mesesDias.get(mes);
        if (dia < 1 || dia > diasDelMes) fechaOK = false;
        
        return fechaOK;
    }
    
    public boolean esBisiesto(int año) {
        boolean bisiesto = false;
        
        if ( (año % 4 == 0) && ((año % 100 != 0) || (año % 400 == 0)) )
            bisiesto = true;
        
        return bisiesto;
    }
    
    public void imprimirFecha() {
        String unDia, unMes;
        
        if (dia < 10) unDia = "0" + String.valueOf(dia);
        else unDia = String.valueOf(dia);
        if (mes < 10) unMes = "0" + String.valueOf(mes);
        else unMes = String.valueOf(mes);
        
        System.out.println(unDia+"-"+unMes+"-"+año);
    }

}
