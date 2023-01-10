#include <stdio.h>

int main(void) {
        
	FILE *file;
	int contatore = 0;
	char coppie[contatore][2];
	char mossauno, mossa2;

	file = fopen("strategyGuide.txt", "r");

	while (fscanf(file, "%c%c", &mossauno, &mossa2) != EOF) 
		contatore += 1;

	for (int i = 0; i < contatore; i++) {

		fscanf(file, "%c%c", &mossauno, &mossa2);
		coppie[i][0] = mossauno;
		coppie[i][1] = mossa2;

	}

	fclose(file);

	printf("%d", contatore);
        
	for (int i = 0; i < contatore; i++) {
		printf("%c%c", coppie[i][0], coppie[i][1]);
	}

	return(0);
}
