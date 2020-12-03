#include <stdio.h>

int secret = 0x1337;
char allowed = 1;

int special(){
	return printf("%d", secret);
}

// INVARIANT(secret): CALL(special) -> allowed == 1
int main(int argc, char** argv){
	if(argc != 2){
		return -1;
	} else {
		allowed = argv[1][0] != 'a';
		if(argv[1][1] == 'x'){
			return special();
		} else {
			return printf("%d", 123);
		}
	}
}
