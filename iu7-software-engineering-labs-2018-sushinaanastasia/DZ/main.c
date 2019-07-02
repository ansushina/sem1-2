/// \brief Программа для перевода чисел из 2ой в 16ую систему счисления
/** \details
Задан текстовый файл, каждая строка которого может рассматриваться как запись 
целого числа в двоичной системе счисления. На его основе создайте текстовый 
файл, в каждой строке которого записано то же самое число, но в 
шестнадцатеричной системе счисления.
*/

#include "sixteen.h"
#include "in_out.h"

int main(int argc, char ** argv)
{
	FILE *f;
	FILE *f2;
	char a1[N], a2[N];
	int n1,n2;
	int rc;
	int t = 1;
	
	if (argc != 3)
	{
		printf("app.exe <file-name> <file-name>");
		return ERR_PARAM;
	}
	
	f = fopen(argv[1], "r");
	if (f)
	{
		f2 = fopen(argv[2], "w");
		while (t)
		{
			rc = read_number(f, a1, &n1);
			printf("%d n = %d\n",rc,n1);
			if (rc == END)
				t = 0;
			if (rc == OK)
			{
				get_number_in_sixteen(a1, n1, a2, &n2);
				printf("n2 = %d\n",n2);
				print_number(f2, a2, n2);
				printf("DONE\n");
			}
			else
			{
				continue;
			}
		}
		fclose(f2);
		fclose(f);
	}
	else
	{
		printf("File can't be open!");
		rc = ERR_IO;
	}
	
	return rc;
}