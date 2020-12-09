#include <stdio.h>

int secret = 0x1337;
long long allowed = 1;

// INVARIANT(global num32 secret, local num8** argv): WRITE(secret) -> *argv[1] == 97
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
