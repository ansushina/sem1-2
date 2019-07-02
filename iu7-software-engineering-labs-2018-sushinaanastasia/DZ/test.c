/**
\brief Модульные тесты

Модульные тесты функций.
*/
#include "sixteen.h"

#define YES 1
#define NO 0

int is_eq(const char *a, int n1,const char *b, int n2)
{
	if (n1 != n2)
		return NO;
	for (int i = 0; i < n1; i++)
		if (a[i] != b[i])
			return NO;
	return YES;
}

void test_go_in_sixteen(void)
{
	printf("TEST GO IN SIXTEEN \n");
	{
		char b[] = {'1','0','0','0'};
		char x;
		char x1 = '8';
		
		go_in_sixteen(b, &x);
		printf("TEST1:");
		if (x == x1)
			printf("OK\n");
		else 
			printf("FAIL\n");
	}
	{
		char b[] = {'1','1','1','1'};
		char x;
		char x1 = 'F';
		
		go_in_sixteen(b, &x);
		printf("TEST1:");
		if (x == x1)
			printf("OK\n");
		else 
			printf("FAIL\n");
	}
	{
		char b[] = {'0','0','0','0'};
		char x;
		char x1 = '0';
		
		go_in_sixteen(b, &x);
		printf("TEST3:");
		if (x == x1)
			printf("OK\n");
		else 
			printf("FAIL\n");
	}
}

void test_get_number_in_sixteen(void)
{
	printf("TEST GET NUMBER IN SIXTEEN\n");
	
	{
		char a1[] = {'1','0','1','0'};
		char a2[N];
		int n2;
		char a3[] = {'A'};
		
		get_number_in_sixteen(a1, sizeof(a1) / sizeof(a1[0]), a2, &n2);
		printf("TEST1: ");
		if (is_eq(a2,n2,a3,sizeof(a3) / sizeof(a3[0])))
			printf("OK\n");
		else
			printf("FAIL\n");
	}
	{
		char a1[] = {'1'};
		char a2[N];
		int n2;
		char a3[] = {'1'};
		
		get_number_in_sixteen(a1, sizeof(a1) / sizeof(a1[0]), a2, &n2);
		printf("TEST1: ");
		if (is_eq(a2,n2,a3,sizeof(a3) / sizeof(a3[0])))
			printf("OK\n");
		else
			printf("FAIL\n");
	}
	{
		char a1[] = {'1','0','1','0','1','0','1','0','1','0'};
		char a2[N];
		int n2;
		char a3[] = {'2','A','A'};
		
		get_number_in_sixteen(a1, sizeof(a1) / sizeof(a1[0]), a2, &n2);
		printf("TEST1: ");
		if (is_eq(a2,n2,a3,sizeof(a3) / sizeof(a3[0])))
			printf("OK\n");
		else
			printf("FAIL\n");
	}
}

int main(void)
{
	test_go_in_sixteen();
	test_get_number_in_sixteen();
	return 0;
}