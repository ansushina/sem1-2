/*
Подзадача find_bigger, которая сравнивает два числа
*/

#include <stdio.h>

#define N 20
#define OK 0
#define ERR_IO 1
#define ERR_PARAM 2 


int read_array(FILE *f, char *a, int *n)
{
	int i = 0;
	char b;
	
	*n = 0;
	while (fscanf(f, "%c", &a[i]) == 1 && a[i] != '\n' && *n < N)
	{
		printf("%d %c\n", *n, a[i]);
		*n += 1;
		i++;
	}
	if (*n == N && fscanf(f, "%c", &b) == 1 )
		return ERR_IO;
	if (a[i] == '\n')
		*n -= 1;
	return OK;
}

void print_array(FILE *f, const char *a,  int n)
{
	for (int i = 0; i < n; i++)
	{
		fprintf(f, "%c", a[i]);
	}
}

void find_bigger(const char *a, int n1, char *b, int *n2)
{
	if (n1 > *n2)
	{
		*n2 = n1;
		for (int i = 0; i < *n2; i++)
		{
			b[i] = a[i];
		}
	}
	else if (n1 == *n2)
	{
		for (int i = 0; i < *n2; i--)
		{
			if (a[i] > b[i])
			{
				*n2 = n1;
		        for (int i = 0; i < *n2; i++)
		        {
			        b[i] = a[i];
		        }
				break;
			}
		}
	}
}

int main(int argc, char ** argv)
{
	FILE *f;
	int rc;
	int n1, n2;
	char a[N], b[N];
	
	if (argc != 3)
	{
		printf("main.exe <file-name> <file-name>");
		return ERR_PARAM;
	}
	
	f = fopen(argv[1], "r");
	
	if (f)
	{
		rc = read_array(f, a, &n1);
		if (rc != OK)
		{
			printf("Too big number");
			fclose(f);
			return rc;
		}
		rc = read_array(f, b, &n2);
		if (rc != OK)
		{
			printf("Too big number");
			fclose(f);
			return rc;
		}
		fclose(f);
		
		find_bigger(a, n1, b, &n2);
		
		f = fopen(argv[2], "w");
		if (f)
		{
		    print_array(f, b, n2);
			fclose(f);
		}
		else
		{
			rc = ERR_IO;
			printf("File 2 can't be open");
		}
	}
	else
	{
		printf("File 1 can't be open!");
		rc = ERR_IO;
	}
	
	
	return rc;
}