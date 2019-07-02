# Общие компиляции
CFLAGS := -std=c99 -Wall -Werror -pedantic

ifeq ($(mode), debug)
	CFLAGS += -g3
endif

ifeq ($(mode), release)
	CFLAGS += -g0 -DNDEBUG
endif

app.exe : sixteen.o main.o in_out.o
	gcc -o app.exe sixteen.o main.o in_out.o

test.exe : sixteen.o test.o in_out.o
	gcc -o test.exe sixteen.o test.o in_out.o

sixteen.o : sixteen.c  sixteen.h
	gcc $(CFLAGS) -c sixteen.c
	
main.o : main.c in_out.h sixteen.h
	gcc $(CFLAGS) -c main.c

in_out.o : in_out.c in_out.h
	gcc $(CFLAGS) -c in_out.c
	
test.o : test.c sixteen.h
	gcc $(CFLAGS) -c test.c


clean :
	rm *.o *.exe
