/**
\file
\brief Заголовочный файл с описанием функций перевода из 2ой в 16ую систему 
счисления

Данный файл содержит в себе определения основных 
функций, используемых при переводе числа из 2ой в 16ую систему счисления. 
*/

#ifndef __SIXTEEN_H__
#define __SIXTEEN_H__

#include <stdio.h>
#include <assert.h>

#define N 200

void get_number_in_sixteen(const char *a1, int n1, char *a2, int *n2);

void go_in_sixteen(const char *b, char *x);

#endif 