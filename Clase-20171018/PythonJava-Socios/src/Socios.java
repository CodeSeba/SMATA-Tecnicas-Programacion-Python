import java.util.Scanner;
import java.util.ArrayList;

public class Socios {
    public static void main (String[] args) {
        
        int nombre = 0;
        int apellido = 1;
        int edad = 2;
        int sexo = 3;
        int deporte = 4;
        int categoria = 5;
                
        ArrayList<ArrayList<String>> lista_socios = new ArrayList<ArrayList<String>>();
        
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
        
        lista_socios.forEach( (unSocio) -> {
            System.out.println( "Nombre: " + unSocio.get(nombre) );
            System.out.println( "Categoria: " + unSocio.get(categoria) );
            System.out.println( "Deporte: " + unSocio.get(deporte) );
            System.out.println( "------------------------------" );
        });
    }
}
