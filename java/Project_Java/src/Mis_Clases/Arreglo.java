/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Mis_Clases;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Random;

/**
 *
 * @author Mario Salazar
 */
public class Arreglo {
     /**
     * Obtener el arreglo de numeros enteros desde un archivo de texto
     *
     * @param nombreArchivo
     * @param tam
     * @return array de numeros enteros aleatorios
     */
    public int[] ArregloArchivoTexto(String nombreArchivo, int tam) {
        int[] arreglo;
        arreglo = new int[tam];
        try {
            File file = new File(nombreArchivo);
            try (FileReader fileReader = new FileReader(file)) {
                BufferedReader bufferedReader = new BufferedReader(fileReader);
                for (int i = 0; i < tam; i++) {
                    arreglo[i] = Integer.parseInt(bufferedReader.readLine());
                }
            }
        } catch (IOException | NumberFormatException e) {
            System.out.println("Error: " + e.getMessage());
        }
        return arreglo;
    }

    public void LlenarArreglo(int[] arreglo) {
        Random random = new Random();
        for (int i = 0; i < arreglo.length; i++) {
            arreglo[i] = random.nextInt(10000);
        }
    }

    public String ImprimirArreglo(int[] arreglo) {
        String resp = "";
        for (int i = 0; i < arreglo.length; i++) {
            resp = resp + "" + arreglo[i] + "  ";
        }
        return resp;
    }

    /**
     * Ordenamiento de Burbuja de un Arreglo de numeros enteros
     *
     * @param arreglo
     * @return Arreglo ordenado de numeros enteros
     */
    public int[] OrdenamientoBurbuja(int[] arreglo) {
        boolean resp = false;
        int aux;
        while (resp == false) {
            resp = true;
            for (int i = 0; i < arreglo.length - 1; i++) {
                if (arreglo[i] > arreglo[i + 1]) {
                    aux = arreglo[i];
                    arreglo[i] = arreglo[i + 1];
                    arreglo[i + 1] = aux;
                    resp = false;
                }
            }
        }
        return arreglo;
    }

    /**
     * Ordenamiento de Inserccion de un arreglo de numeros
     *
     * @param arreglo
     * @return Arreglo ordenado de numeros enteros
     */
    public int[] OrdenamientoInsercion(int[] arreglo) {
        int aux, a;
        for (int i = 1; i < arreglo.length; i++) {
            aux = arreglo[i];
            a = i - 1;
            while (a >= 0) {
                if (aux < arreglo[a]) {
                    arreglo[a + 1] = arreglo[a];
                    arreglo[a] = aux;
                    a -= 1;
                } else {
                    break;
                }
            }
        }
        return arreglo;
    }

    /**
     * Ordenamiento de Seleccion de un arreglo de numeros enteros
     *
     * @param arreglo
     * @return Arreglo ordenado de numeros enteros
     */
    public int[] OrdenamientoSeleccion(int[] arreglo) {
        int posMax, aux;
        for (int i = arreglo.length - 1; i >= 0; i--) {
            posMax = 0;
            for (int j = 1; j < i + 1; j++) {
                if (arreglo[j] > arreglo[posMax]) {
                    posMax = j;
                }
            }
            aux = arreglo[i];
            arreglo[i] = arreglo[posMax];
            arreglo[posMax] = aux;
        }
        return arreglo;
    }

    /**
     * Divide el arreglo en dos mitades
     *
     * @param arreglo
     * @return Arreglo La mitad del arreglo original, Derecha
     */
    public int[] MitadDerecha(int[] arreglo) {
        int i = 0;
        int j = arreglo.length / 2;
        int[] aux = new int[(arreglo.length - arreglo.length / 2)];
        while (i < aux.length) {
            aux[i] = arreglo[j];
            i++;
            j++;
        }
        return aux;
    }

    /**
     * Ordenamiento por Merge Sort de un arreglo de numeros enteros
     *
     * @param arreglo
     * @return Arreglo ordenado de numeros enteros
     */
    public int[] OrdenamientoMergeSort(int[] arreglo) {
        if (arreglo.length > 1) {
            int mitad, mitadIzquierda[], mitadDerecha[], i, j, k;
            mitad = arreglo.length / 2;
            mitadIzquierda = new int[mitad];
            mitadDerecha = MitadDerecha(arreglo);
            int a = 0;
            while (a < mitad) {
                mitadIzquierda[a] = arreglo[a];
                a++;
            }
            OrdenamientoMergeSort(mitadIzquierda);
            OrdenamientoMergeSort(mitadDerecha);
            i = 0;
            j = 0;
            k = 0;
            while (i < mitadIzquierda.length && j < mitadDerecha.length) {
                if (mitadIzquierda[i] < mitadDerecha[j]) {
                    arreglo[k] = mitadIzquierda[i];
                    i++;
                } else {
                    arreglo[k] = mitadDerecha[j];
                    j++;
                }
                k++;
            }
            while (i < mitadIzquierda.length) {
                arreglo[k] = mitadIzquierda[i];
                i++;
                k++;
            }
            while (j < mitadDerecha.length) {
                arreglo[k] = mitadDerecha[j];
                j++;
                k++;
            }
        }
        return arreglo;
    }

    /**
     * Ordenamiento por Shell de un arreglo de numeros enteros
     *
     * @param arreglo
     * @return Arreglo ordenado de numeros enteros
     */
    public int[] OrdenamientoShell(int[] arreglo) {
        int salto, temp, i;
        boolean cambio;
        for (salto = arreglo.length / 2; salto != 0; salto /= 2) {
            cambio = true;
            while (cambio) {
                cambio = false;
                for (i = salto; i < arreglo.length; i++) {
                    if (arreglo[i - salto] > arreglo[i]) {
                        temp = arreglo[i];
                        arreglo[i] = arreglo[i - salto];
                        arreglo[i - salto] = temp;
                        cambio = true;
                    }
                }
            }
        }
        return arreglo;
    }

    /**
     * Ordenamiento por QuickSort de un arreglo de numeros enteros
     *
     * @param arreglo
     * @return Arreglo ordenado de numeros enteros
     */
    public int[] OrdenamientoQuickSort(int[] arreglo) {
        QuickSortAuxiliar(arreglo, 0, arreglo.length - 1);
        return arreglo;
    }

    public int Particionar(int[] arreglo, int a, int b) {
        int pivote = arreglo[a], izq = a + 1, der = b, temporal;
        boolean fin = false;
        while (fin == false) {
            while (izq <= der && arreglo[izq] <= pivote) {
                izq++;
            }
            while (arreglo[der] >= pivote && der >= izq) {
                der--;
            }
            if (der < izq) {
                fin = true;
            } else {
                temporal = arreglo[izq];
                arreglo[izq] = arreglo[der];
                arreglo[der] = temporal;
            }
        }
        temporal = arreglo[a];
        arreglo[a] = arreglo[der];
        arreglo[der] = temporal;
        return der;
    }

    public void QuickSortAuxiliar(int[] arreglo, int a, int b) {
        int partida;
        if (a < b) {
            partida = Particionar(arreglo, a, b);
            QuickSortAuxiliar(arreglo, a, partida - 1);
            QuickSortAuxiliar(arreglo, partida + 1, b);
        }
    }

    /**
     * Ordenamiento por RadixSort de un arreglo de numeros enteros
     *
     * @param arreglo
     * @return Arreglo ordenado de numeros enteros
     */
    public int[] OrdenamientoRadixSort(int[] arreglo) {
        int x, i, j;
        int[] auxiliar;
        for (x = Integer.SIZE - 1; x >= 0; x--) {
            auxiliar = new int[arreglo.length];
            j = 0;
            for (i = 0; i < arreglo.length; i++) {
                boolean mover = arreglo[i] << x >= 0; //si x >=0 True agregar al arreglo[i]
                if (x == 0 ? !mover : mover) {
                    auxiliar[j] = arreglo[i];
                    j++;
                } else {
                    arreglo[i - j] = arreglo[i];
                }
            }
            for (i = j; i < auxiliar.length; i++) {
                auxiliar[i] = arreglo[i - j];
            }
            arreglo = auxiliar;
        }
        return arreglo;
    }

    /**
     * Ordenamiento por BuckSort de un arreglo de numeros enteros
     *
     * @param arreglo
     * @return Arreglo ordenado de numeros enteros
     */
    public int[] OrdenamientoBuckSort(int[] arreglo) {
        int[] caja = new int[Maximo(arreglo) + 1];
        for (int i = 0; i < arreglo.length; i++) {
            caja[arreglo[i]] = caja[arreglo[i]] + 1;
        }
        int outPos = 0;
        for (int i = 0; i < caja.length; i++) {
            for (int j = 0; j < caja[i]; j++) {
                arreglo[outPos++] = i;
            }
        }
        return arreglo;
    }

    /**
     * Obtiene el valor maximo de un arreglo
     *
     * @param arreglo
     * @return valor maximo de un array
     */
    public int Maximo(int[] arreglo) {
        int m = 0;
        for (int i = 0; i < arreglo.length; i++) {
            if (arreglo[i] > m) {
                m = arreglo[i];
            }
        }
        return m;
    }

    /**
     * Ordenamiento por Cuentas de un arreglo de numeros enteros
     *
     * @param arreglo
     * @return Arreglo ordenado de numeros enteros
     */
    public int[] OrdenamientoCuentas(int[] arreglo) {
        int maximo = Maximo(arreglo) + 1;
        int[] conteo = new int[maximo];
        for (int i = 0; i < arreglo.length; i++) {
            conteo[arreglo[i]] += 1;
        }
        int i = 0;
        for (int j = 0; j < maximo; j++) {
            for (int k = 0; k < conteo[j]; k++) {
                arreglo[i] = j;
                i++;
            }
        }
        return arreglo;
    }

    /**
     * Ordenamiento por HeapSort(Monticulos) de un arreglo de numeros enteros
     *
     * @param arreglo
     * @return Arreglo ordenado de numeros enteros
     */
    public int[] OrdenamientoHeapSort(int[] arreglo) {
        final int n = arreglo.length;
        for (int nodo = n / 2; nodo >= 0; nodo--) {
            Heapyfy(arreglo, nodo, n - 1);
        }
        for (int nodo = n - 1; nodo >= 0; nodo--) {
            int temp = arreglo[0];
            arreglo[0] = arreglo[nodo];
            arreglo[nodo] = temp;
            Heapyfy(arreglo, 0, nodo - 1);
        }
        return arreglo;
    }

    public void Heapyfy(int[] arreglo, int nodo, int fin) {
        int izquierdo = 2 * nodo + 1;
        int derecho = izquierdo + 1;
        int mayor;
        if (izquierdo > fin) {
            return;
        }
        if (derecho > fin) {
            mayor = izquierdo;
        } else {
            mayor = arreglo[izquierdo] > arreglo[derecho] ? izquierdo : derecho;
        }
        if (arreglo[nodo] < arreglo[mayor]) {
            int temp = arreglo[nodo];
            arreglo[nodo] = arreglo[mayor];
            arreglo[mayor] = temp;
            Heapyfy(arreglo, mayor, fin);
        }
    }
}
