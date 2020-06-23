#include<stdio.h>
long fib(long x) {
    if(x ==1 || x == 2) {
	return 1L;
    } else {
	return fib(x-1) + fib(x-2);
    }
}
int main() {
    int i=0;
    for(i=1; i< 50; ++i) {
	printf("%d %ld\n", i, fib(i) );
    }
    return 0;
}
