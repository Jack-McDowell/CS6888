#include <stdio.h>

int secret = 0x1337;
long long allowed = 1;

// INVARIANT(secret): WRITE(secret) -> *argv[1] == 'a'
int main(int argc, char** argv){
	if(argc != 2){
		return -1;
	} else {
		allowed = *argv[1] != 'a';
		if(argv[1][1] == 'x'){
			secret = 0x5432;
		}
	}

	allowed = 0;
	printf("%d", secret);
}
