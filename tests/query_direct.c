#include <stdio.h>
#include <string.h>

const char* secret = "secret123";
char allowed = 0;

// INVARIANT(global allowed, global secret): READ(secret) -> allowed

void execute_query(const char* query){
	if(strstr(query, "secret")){
		if(allowed){
			puts(secret);
		} else {
			puts("not admin");
		}
	}

	const char* ptr = strstr(query, "lookup");
	if(ptr){
		puts(secret);
	}
}

int main(int argc, char** argv){
	if(argc != 2){
		printf("Usage: %s <query> <password>\n", argv[0]);
	} else {
		allowed = *argv[1] != 'g';
		execute_query(argv[1] + 1);
	}
	return 0;
}
