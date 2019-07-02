/**
\file
\brief Заголовочный файл с описанием функций ввода/вывода

Данный файл содержит в себе определения основных 
функций, используемых при вводе и выводе значений.
*/
#ifndef __IN_OUT_H__
#define __IN_OUT_H__

#include <stdio.h>
#include <assert.h>

#define N 200

#define OK 0
#define ERR_IO 1
#define ERR_PARAM 2
#define END 4

int read_number(FILE *f, char *a, int *n);

void print_number(FILE *f, const char *a, int n);

#endif 
