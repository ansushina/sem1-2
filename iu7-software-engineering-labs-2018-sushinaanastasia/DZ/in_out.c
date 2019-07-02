
#include "in_out.h"
/**
\fn int read_number(FILE *f, char *a, int *n)
Функция считывания числа из файла
\param[in] f Файл с числами
\param[in,out] a строка
\param[out] n длина массива
*/
int read_number(FILE *f, char *a, int *n)
{
	assert(f != NULL);
	assert(a != NULL);
	
	int rc;
	
	rc = fscanf(f, "%s", a);
	if (rc == EOF)
		return END;
	*n = 0;
	
	while (a[*n] != '\0' )
	{
		if (a[*n] != '0' && a[*n] != '1')
			return ERR_IO;
		*n += 1;
	}
	return OK;
}

/**
\fn void print_number(FILE *f, const char *a, int n)
Функция записи в файл
\param[in,out] f Файл с числами
\param[in,out] a строка
\param[in] n длина массива
*/
void print_number(FILE *f, const char *a, int n)
{
	assert(f != NULL);
	assert(a != NULL);
	assert( n >= 0);
	assert( n < N);
	
	fprintf(f,"%s\n", a);
	
}