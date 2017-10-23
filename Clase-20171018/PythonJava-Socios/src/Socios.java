/*
Se realiza la inscripcion de socios en un club.
La carga de datos finaliza cuando se ingresa
como nombre "pepe".

Los datos a ingresar son:
-Nombre
-Apellido
-Edad
-Sexo
-Deporte

Los deportes son:
-Futbol
-Hockey
-Handball
-Tenis
-Natacion

Para calcular la Categoria se usa
la siguiente tabla:
-Menor - 0 a 3 años.
-Infantil - 3 a 6 años.
-PreMini - 6 a 9 años.
-Mini - 9 a 12 años.
-Cadete - 12 a 15 años.
-Juvenil - 15 a 18 años.
-Activo - 18 a 60 años.
-Vitalicio - Mayores a 60 años.

1. Imprimir Nombre, Categoria y Deporte.

(Ejercicios Agregados el 23 de Oct.)
2. Total de socios con categoria "Activo".
3. Total de socios con categoria "Juvenil" y sexo "Femenino".
4. Total de socios con categoria "Mini", sexo "Masculino" y
   deporte "Futbol".
5. Promedio de mujeres inscriptos en "Hockey".
6. Total de socios con sexo "Femenino" y deporte "Hockey".
7. Total de socios con categoria "Mini" y deporte "Tenis".
8. Total de socios que practican "Natacion".
9. Pocentaje de socios que practican "Natacion".
10. Pocentaje de socios con sexo "Femenino".
11. Total de socios discriminados por:
    -Genero
    -Deporte
    -Categoria
*/

import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Socios {
    public static void main (String[] args) {
        
        // Nombres de los indices
        int nombre = 0;
        int apellido = 1;
        int edad = 2;
        int sexo = 3;
        int deporte = 4;
        int categoria = 5;
        
        ArrayList<ArrayList<String>> lista_socios = new ArrayList<ArrayList<String>>();
        
        int cant_activos = 0;
        int cant_juv_fem = 0;
        int cant_min_mas_fut = 0;
        int cant_fem_hoc = 0;
        int cant_min_ten = 0;
        int cant_natacion = 0;
        int cant_femeninos = 0;

        double prom_fem_hoc = 0;
        double porc_natacion = 0;
        double porc_femeninos = 0;
        
        /*
        Scanner teclado = new Scanner( System.in );
        ArrayList<String> unSocio = new ArrayList<>();
        String nombre;
        
        System.out.println("Ingresar Nombre");
        unNombre = teclado.next();
        
        while ( !unNombre.equals("pepe") ) {
            
            unSocio.add( unNombre );
            System.out.println("Ingresar Apellido");
            unSocio.add( teclado.next() );
            System.out.println("Ingresar Edad");
            unSocio.add( teclado.next() );
            System.out.println("Ingresar Genero");
            unSocio.add( teclado.next() );
            System.out.println("Ingresar Deporte");
            unSocio.add( teclado.next() );
            
            lista_socios.add( unSocio );
            unSocio = new ArrayList<>();
            
            System.out.println("Ingresar Nombre");
            unNombre = teclado.next();
        }
        */
        
        String[] lista_datos = new String[] {
            "Gregoire,Kropach,3,Masculino,Hockey",
            "Braden,MacDavitt,5,Masculino,Futbol",
            "Giorgia,Oattes,7,Femenino,Futbol",
            "Skippy,Gullefant,10,Masculino,Hockey",
            "Vito,Titterell,15,Masculino,Natacion",
            "Esteban,Griston,16,Masculino,Hockey",
            "Rupert,Rutley,20,Masculino,Hockey",
            "Niles,Dobey,66,Masculino,Futbol",
            "Stanleigh,Oluwatoyin,2,Masculino,Hockey",
            "Lena,Kift,17,Femenino,Handball",
            "Raoul,DeZuani,20,Masculino,Natacion",
            "Brooky,Espinheira,9,Femenino,Tenis"
        };
        
        for (String datos : lista_datos) {
            String[] datos_separados = datos.split(",");
            ArrayList<String> unSocio = new ArrayList<String>(datos_separados.length);
            
            for (String unDato : datos_separados) {
                unSocio.add(unDato);
            }

            lista_socios.add(unSocio);
        }
        
        lista_socios.forEach( (unSocio) -> {
            String stEdad = unSocio.get(edad);
            int unaEdad = Integer.parseInt(stEdad);
            String unaCategoria = "";
            
            if (unaEdad > 0 && unaEdad < 3) {
                unaCategoria = "Menor";
            } else
            if (unaEdad >= 3 && unaEdad < 6) {
                unaCategoria = "Infantil";
            } else
            if (unaEdad >= 6 && unaEdad < 9) {
                unaCategoria = "PreMini";
            } else
            if (unaEdad >= 9 && unaEdad < 12) {
                unaCategoria = "Mini";
            } else
            if (unaEdad >= 12 && unaEdad < 15) {
                unaCategoria = "Cadete";
            } else
            if (unaEdad >= 15 && unaEdad < 18) {
                unaCategoria = "Juvenil";
            } else
            if (unaEdad >= 18 && unaEdad < 60) {
                unaCategoria = "Activo";
            } else
            if (unaEdad >= 60) {
                unaCategoria = "Vitalicio";
            }
            
            unSocio.add(unaCategoria);
        });
        
        // 1.
        System.out.println("Lista de Socios");
        System.out.println( "==============================" );
        System.out.println("");
        
        lista_socios.forEach( (unSocio) -> {
            System.out.println( "Nombre: " + unSocio.get(nombre) );
            System.out.println( "Categoria: " + unSocio.get(categoria) );
            System.out.println( "Deporte: " + unSocio.get(deporte) );
            System.out.println( "------------------------------" );
        });
        
        // 2. 3. 4. 6. 7. 8.
        for ( ArrayList<String> unSocio : lista_socios ) {

            String unaCategoria = unSocio.get(categoria);
            String unSexo = unSocio.get(sexo);
            String unDeporte = unSocio.get(deporte);
            
            
            if (unaCategoria.equals("Activo")) cant_activos ++;
                        
            if (unSexo.equals("Femenino")) {
                cant_femeninos ++;
                
                if (unaCategoria.equals("Juvenil")) cant_juv_fem ++;

                if (unDeporte.equals("Hockey")) cant_fem_hoc ++;
            }
            
            if (unaCategoria.equals("Mini")) {
                if (unSexo.equals("Masculino"))
                    if (unDeporte.equals("Futbol")) cant_min_mas_fut ++;
                
                if (unDeporte.equals("Tenis")) cant_min_ten ++;
            }
                        
            if (unDeporte.equals("Natacion")) cant_natacion ++;
        };
        
        // 9. 10.
        int cant_socios = lista_socios.size();
        
        porc_natacion = cant_natacion * 100 / cant_socios;
        
        porc_femeninos = cant_femeninos * 100 / cant_socios;
        
        System.out.println("");
        System.out.println("Total de socios Activos: " + cant_activos);
        System.out.println("Total de socios Juvenil y Femenino: " + cant_juv_fem);
        System.out.println("Total de socios Mini, Masculino y Futbol: " + cant_min_mas_fut);
        System.out.println("Total de socios Femenino y Hockey: " + cant_fem_hoc);
        System.out.println("Total de socios Mini y Tenis: " + cant_min_ten);
        System.out.println("Total de socios Natacion: " + cant_natacion);
        System.out.println("Porcentaje de Natacion: " + porc_natacion + " %");
        System.out.println("Porcentaje de Femeninos: " + porc_femeninos + " %");
        
        Map<String, Integer> dicc_genero = new HashMap<>();
        Map<String, Integer> dicc_deporte = new HashMap<>();
        Map<String, Integer> dicc_categoria = new HashMap<>();
        
        for (ArrayList<String> unSocio : lista_socios) {
            
            Integer unValor = 0;
            
            String unSexo = unSocio.get(sexo);
            if (dicc_genero.containsKey(unSexo)) {
                unValor = dicc_genero.get(unSexo);
                dicc_genero.put(unSexo, unValor + 1);
            } else {
                dicc_genero.put(unSexo, 1);
            }
                
            String unDeporte = unSocio.get(deporte);
            if (dicc_deporte.containsKey(unDeporte)) {
                unValor = dicc_deporte.get(unDeporte) ;
                dicc_deporte.put(unDeporte, unValor + 1);
            } else {
                dicc_deporte.put(unDeporte, 1);
            }
            
            String unaCategoria = unSocio.get(categoria);
            if (dicc_categoria.containsKey(unaCategoria)) {
                unValor = dicc_categoria.get(unaCategoria) ;
                dicc_categoria.put(unaCategoria, unValor + 1);
            } else {
                dicc_categoria.put(unaCategoria, 1);
            }
        }
        System.out.println("");
        System.out.println("Total Socios por Genero");
        System.out.println( "==============================" );
        for (String key : dicc_genero.keySet()) {
            System.out.println(key + " : " + dicc_genero.get(key));
        }
        
        System.out.println("");
        System.out.println("Total Socios por Deporte");
        System.out.println( "==============================" );
        for (String key : dicc_deporte.keySet()) {
            System.out.println(key + " : " + dicc_deporte.get(key));
        }
        
        System.out.println("");
        System.out.println("Total Socios por Categoria");
        System.out.println( "==============================" );
        for (String key : dicc_categoria.keySet()) {
            System.out.println(key + " : " + dicc_categoria.get(key));
        }
    }
}
