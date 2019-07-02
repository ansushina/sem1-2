/*
Модульные тесты 
*/

#include <stdio.h>

#define N 20
#define OK 0
#define ERR_IO 1
#define ERR_PARAM 2 

#define YES 1
#define NO 0

void find_bigger(const char *a, int n1, char *b, int *n2);

int is_eq(const char *a, int n1,const char *b, int n2)
{
	if (n1 != n2)
		return NO;
	for (int i = 0; i < n1; i++)
		if (a[i] != b[i])
			return NO;
	return YES;
}

void test_find_bigger(void)
{
	{
		char a[] = {1,2,3};
		char b[] = {2,3,3};
		int n2;
		char c[] = {2,3,3}
		
		printf("TEST1:");
		
		find_bigger(a, sizeof(a) / sizeof(a[0]), b, &n2);
		if (is_eq(b,n2,c,sizeof(c) / sizeof(c[0])))
			printf("OK\n");
		else
			printf("FAIL\n");
	}
	
}

int main(void)
{
	test_find_bigger();
	return 0;
}