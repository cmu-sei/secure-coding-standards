
#include <stdio.h>
#include <limits.h>

int main(void) {
	int si1 = 4;
	int si2 = 2;
	unsigned int ui1 = 4;
	unsigned int ui2 = 2;

	/*-------------------------------------------------------------------------------------------------*\
	| Signed left shift
	\*-------------------------------------------------------------------------------------------------*/

	// 4 << 2 = 16
	if ( (si1 < 0) || (si2 < 0) || (si2 >= sizeof(int)*CHAR_BIT) || (si1 > (INT_MAX / (1 << si2))) ) {
		fprintf(stderr, "error processing %d << %d = %d.\n", si1, si2, si1 << si2);
	}
	else {
		fprintf(stdout, "%d << %d = %d.\n", si1, si2, si1 << si2);
	}

	// error processing 4 << 32 = 4.
	si1 = 4;
	si2 = 32; // error
	if ( (si1 < 0) || (si2 < 0) || (si2 >= sizeof(int)*CHAR_BIT) || (si1 > (INT_MAX / (1 << si2))) ) {
		fprintf(stderr, "error processing %d << %d = %d.\n", si1, si2, si1 << si2);
	}
	else {
		fprintf(stdout, "%d << %d = %d.\n", si1, si2, si1 << si2);
	}

	// error processing 1 << 32 = 1.
	si1 = 1;
	si2 = 32; 
	if ( (si1 < 0) || (si2 < 0) || (si2 >= sizeof(int)*CHAR_BIT) || si1 > (INT_MAX >> si2) ) {
		fprintf(stderr, "error processing %d << %d = %d.\n", si1, si2, si1 << si2);
	}
	else {
		fprintf(stdout, "%d << %d = %d.\n", si1, si2, si1 << si2);
	}

	// error processing 1 << 31 = -2147483648.
	si1 = 1;
	si2 = 31; 
	if ( (si1 < 0) || (si2 < 0) || (si2 >= sizeof(int)*CHAR_BIT) || si1 > (INT_MAX >> si2) ) {
		fprintf(stderr, "error processing %d << %d = %d.\n", si1, si2, si1 << si2);
	}
	else {
		fprintf(stdout, "%d << %d = %d.\n", si1, si2, si1 << si2);
	}

	// 1 << 30 = 1073741824
	si1 = 1;
	si2 = 30; 
	if ( (si1 < 0) || (si2 < 0) || (si2 >= sizeof(int)*CHAR_BIT) || si1 > (INT_MAX >> si2) ) {
		fprintf(stderr, "error processing %d << %d = %d.\n", si1, si2, si1 << si2);
	}
	else {
		fprintf(stdout, "%d << %d = %d.\n", si1, si2, si1 << si2);
	}

	// error processing -1 << 30 = -1073741824.
	si1 = -1;
	si2 = 30; 
	if ( (si1 < 0) || (si2 < 0) || (si2 >= sizeof(int)*CHAR_BIT) || si1 > (INT_MAX >> si2) ) {
		fprintf(stderr, "error processing %d << %d = %d.\n", si1, si2, si1 << si2);
	}
	else {
		fprintf(stdout, "%d << %d = %d.\n", si1, si2, si1 << si2);
	}

	// error processing 4 << -2 = 0.
	si1 = 4;
	si2 = -2; 
	if ( (si1 < 0) || (si2 < 0) || (si2 >= sizeof(int)*CHAR_BIT) || si1 > (INT_MAX >> si2) ) {
		fprintf(stderr, "error processing %d << %d = %d.\n", si1, si2, si1 << si2);
	}
	else {
		fprintf(stdout, "%d << %d = %d.\n", si1, si2, si1 << si2);
	}

	/*-------------------------------------------------------------------------------------------------*\
	| Unsigned left shift
	\*-------------------------------------------------------------------------------------------------*/

	// 4 << 2 = 16
	if ( (ui2 >= sizeof(int)*CHAR_BIT) || (ui1 > (UINT_MAX / (1 << ui2))) ) {
		fprintf(stderr, "error procesuing %u << %u = %u.\n", ui1, ui2, ui1 << ui2);
	}
	else {
		fprintf(stdout, "%u << %u = %u.\n", ui1, ui2, ui1 << ui2);
	}

	// error processing 4 << 32 = 4.
	ui1 = 4;
	ui2 = 32; // error
	if ( (ui2 >= sizeof(int)*CHAR_BIT) || (ui1 > (UINT_MAX / (1 << ui2))) ) {
		fprintf(stderr, "error processing %u << %u = %u.\n", ui1, ui2, ui1 << ui2);
	}
	else {
		fprintf(stdout, "%u << %u = %u.\n", ui1, ui2, ui1 << ui2);
	}

	// error processing 1 << 32 = 1.
	ui1 = 1;
	ui2 = 32; 
	if ( (ui2 >= sizeof(int)*CHAR_BIT) || ui1 > (UINT_MAX >> ui2) ) {
		fprintf(stderr, "error processing %u << %u = %u.\n", ui1, ui2, ui1 << ui2);
	}
	else {
		fprintf(stdout, "%u << %u = %u.\n", ui1, ui2, ui1 << ui2);
	}

	// error processing 1 << 31 = -2147483648.
	ui1 = 1;
	ui2 = 31; 
	if ( (ui2 >= sizeof(unsigned int)*CHAR_BIT) || ui1 > (UINT_MAX >> ui2) ) {
		fprintf(stderr, "error processing %u << %u = %u.\n", ui1, ui2, ui1 << ui2);
	}
	else {
		fprintf(stdout, "%u << %u = %u.\n", ui1, ui2, ui1 << ui2);
	}

	// 1 << 30 = 1073741824
	ui1 = 1;
	ui2 = 30; 
	if ( (ui2 >= sizeof(int)*CHAR_BIT) || ui1 > (UINT_MAX >> ui2) ) {
		fprintf(stderr, "error processing %u << %u = %u.\n", ui1, ui2, ui1 << ui2);
	}
	else {
		fprintf(stdout, "%u << %u = %u.\n", ui1, ui2, ui1 << ui2);
	}

	// error processing -1 << 30 = -1073741824.
	ui1 = UINT_MAX;
	ui2 = 30; 
	if ( (ui2 >= sizeof(int)*CHAR_BIT) || ui1 > (UINT_MAX >> ui2) ) {
		fprintf(stderr, "error processing %u << %u = %u.\n", ui1, ui2, ui1 << ui2);
	}
	else {
		fprintf(stdout, "%u << %u = %u.\n", ui1, ui2, ui1 << ui2);
	}

	// error processing 4 << -2 = 0.
	ui1 = 4;
	ui2 = UINT_MAX; 
	if ( (ui2 >= sizeof(int)*CHAR_BIT) || ui1 > (UINT_MAX >> ui2) ) {
		fprintf(stderr, "error processing %u << %u = %u.\n", ui1, ui2, ui1 << ui2);
	}
	else {
		fprintf(stdout, "%u << %u = %u.\n", ui1, ui2, ui1 << ui2);
	}

	/*-------------------------------------------------------------------------------------------------*\
	| Signed right shift
	\*-------------------------------------------------------------------------------------------------*/

	// ok 
	// 2 >> 4 = 0.
	si1 = 2;
	si2 = 4;
	if ( (si1 < 0) || (si2 < 0) || (si2 >= sizeof(int)*CHAR_BIT) ) {
		fprintf(stderr, "error processing %d >> %d = %d.\n", si1, si2, si1 >> si2);
	}
	else {
		fprintf(stdout, "%d >> %d = %d.\n", si1, si2, si1 >> si2);
	}

	// error processing -4 >> 4 = -1.
	si1 = -4;
	si2 = 4;
	if ( (si1 < 0) || (si2 < 0) || (si2 >= sizeof(int)*CHAR_BIT) ) {
		fprintf(stderr, "error processing %d >> %d = %d.\n", si1, si2, si1 >> si2);
	}
	else {
		fprintf(stdout, "%d >> %d = %d.\n", si1, si2, si1 >> si2);
	}

	// error processing 4 >> -4 = 0.
	si1 = 4;
	si2 = -4;
	if ( (si1 < 0) || (si2 < 0) || (si2 >= sizeof(int)*CHAR_BIT) ) {
		fprintf(stderr, "error processing %d >> %d = %d.\n", si1, si2, si1 >> si2);
	}
	else {
		fprintf(stdout, "%d >> %d = %d.\n", si1, si2, si1 >> si2);
	}

	// error processing 4 >> 32 = 4.
	si1 = 4;
	si2 = 32;
	if ( (si1 < 0) || (si2 < 0) || (si2 >= sizeof(int)*CHAR_BIT) ) {
		fprintf(stderr, "error processing %d >> %d = %d.\n", si1, si2, si1 >> si2);
	}
	else {
		fprintf(stdout, "%d >> %d = %d.\n", si1, si2, si1 >> si2);
	}

	// 32 >> 2 = 8.
	si1 = 32;
	si2 = 2;
	if ( (si1 < 0) || (si2 < 0) || (si2 >= sizeof(int)*CHAR_BIT) ) {
		fprintf(stderr, "error processing %d >> %d = %d.\n", si1, si2, si1 >> si2);
	}
	else {
		fprintf(stdout, "%d >> %d = %d.\n", si1, si2, si1 >> si2);
	}

	/*-------------------------------------------------------------------------------------------------*\
	| Unsigned right shift
	\*-------------------------------------------------------------------------------------------------*/

	// 4 >> 2 = 1.
	ui1 = 4;
	ui2 = 2;
	if (ui2 >= sizeof(unsigned int)*CHAR_BIT) {
		fprintf(stderr, "error processing %u >> %u = %u.\n", ui1, ui2, ui1 >> ui2);
	}
	else {
		fprintf(stdout, "%u >> %u = %u.\n", ui1, ui2, ui1 >> ui2);
	}

	// error processing 4 >> 32 = 4.
	ui1 = 4;
	ui2 = 32;
	if (ui2 >= sizeof(unsigned int)*CHAR_BIT) {
		fprintf(stderr, "error processing %u >> %u = %u.\n", ui1, ui2, ui1 >> ui2);
	}
	else {
		fprintf(stdout, "%u >> %u = %u.\n", ui1, ui2, ui1 >> ui2);
	}

	return 0;
}

