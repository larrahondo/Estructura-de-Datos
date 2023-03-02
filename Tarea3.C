/*Nombre: Juan Jose Larrahondo Giron*/
/*codigo: 8977454*/

#include <stdio.h>


int main (){
	int caso1;
	int caso2;
	int caso3;
	int i;
	int arreglo[100];
	int mayorTienda;
	int menorTienda;
	int parqueadero;
	
	scanf("%d, &caso1");
	for (i = 0; i < caso1; i++){
		scanf("%d", &caso2);
		for(caso3 = 0; caso3 < caso2; caso3++){
			scanf("%d", &arreglo[i]);
			if(caso3 == 0){
		mayorTienda = arreglo[i];
		menorTienda = arreglo[i];
			}
		if(menorTienda > arreglo[i]){
		menorTienda = arreglo[i];
			}
		if(mayorTienda < arreglo[i]){
		mayorTienda = arreglo[i];
		}
	    }
		parqueadero = (mayorTienda-menorTienda)*2;
	printf("%d\n", parqueadero);	
		}
	return 0;
}
