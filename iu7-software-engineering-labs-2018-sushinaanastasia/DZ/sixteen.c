#include "sixteen.h"
#include "math.h"

#define FOUR 4
/**
\fn void get_number_in_sixteen(const char *a1, int n1, char *a2, int *n2)
 Функция перевода числа из 2ой в 16ную систему счисления
\param[in] a1 строка
\param[in,out] a2 строка
\param[in] n1 длина строки 1
\param[out] длина строки 2
*/
void get_number_in_sixteen(const char *a1, int n1, char *a2, int *n2)
{
	assert(a1 != NULL);
	assert(a2 != NULL);
	assert(n1 >= 0);
	assert(n1 < N);
	
	char b[FOUR];
	char x;
	int first; 
	int i,j;
	
	j = 0;
	first = n1 % FOUR;
	*n2 = 0;
	if (first != 0)
	{
		i = 0;
		while ( i < FOUR - first)
		{
			b[i] = 0;
			i++;
		}
		while (i < FOUR)
		{
			b[i] = a1[j];
			i++;
			j++;
		}
		go_in_sixteen(b, &x);
		a2[*n2] = x;
		*n2 += 1;
	}
	
	while (j < n1)
	{
		for (i = 0; i < FOUR; i++)
		{
			b[i] = a1[j];
			j++;
		}
		go_in_sixteen(b, &x);
		a2[*n2] = x;
		*n2 += 1;
	}
}

/**
\fn void go_in_sixteen(const char *b, char *x)
Функция перевода блока и 4 цифр из 2ой в 16ную систему счисления
\param[in] b блок из 4 цифр
\param[out] x цифра в 16ой системе счисления
*/
void go_in_sixteen(const char *b, char *x)
{
	assert(b != NULL);
	
	int k = 0;
	
	for (int i = 0; i < FOUR; i++)
	{
		if (b[i] == '1')
			k += pow(2, 3 - i);
	}
	printf("k = %d\n", k);
	if (k < 10)
		*x = k + '0';
	else if (k == 10)
		*x = 'A';
	else if (k == 11)
		*x = 'B';
	else if (k == 12)
		*x = 'C';
	else if (k == 13)
		*x = 'D';
	else if (k == 14)
		*x = 'E';
	else if (k == 15)
		*x = 'F';
	
}