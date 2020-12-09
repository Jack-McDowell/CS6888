#include <stdio.h>

int secret = 0x1337;
long long allowed = 1;

// INVARIANT(global num32 secret, global num64 allowed): READ(secret) -> allowed == 1
int main(int argc, char** argv){
	if(argc != 2){
		return -1;
	} else {
		allowed = *argv[1] != 'a';
		if(argv[1][1] == 'x'){
			return printf("%d", secret);
		} else {
			return printf("%d", 123);
		}
	}
}
