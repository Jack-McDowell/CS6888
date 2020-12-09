#include <stdio.h>
#include <string.h>

const char* password = "secret123";

// INVARIANT(local num8 is_admin, global num8* password): READ(password) -> is_admin
void execute_query(const char* query, char is_admin){
	if(strstr(query, "secret")){
		if(is_admin){
			puts(password);
		} else {
			puts("not admin");
		}
	}
}

int main(int argc, char** argv){
	if(argc != 2){
		printf("Usage: %s <query>\n", argv[0]);
	} else {
		execute_query(argv[1], 0);
	}
	return 0;
}
