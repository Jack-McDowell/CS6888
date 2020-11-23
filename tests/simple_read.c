#include <stdio.h>

int secret = 0x1337;

// INVARIANT(secret): READ(secret) -> false
int main(int argc, char** argv){
	if(argc != 2){
		return -1;
	} else {
		return printf("%d", secret);
	}
}
