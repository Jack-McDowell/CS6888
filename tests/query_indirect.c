#include <stdio.h>
#include <string.h>

const char* password = "secret123";
const char** strings[] = {
	&"aaaaa",
	&"bbbbb",
	&password,
	&"ccccc",
	&"ddddd",
	&"eeeee",
	&"fffff",
	&"ggggg",
	&"hhhhh",
	&"iiiii",
};
char is_admin;

// INVARIANT(is_admin, password): READ(password) -> is_admin
void execute_query(const char* query){
	if(strstr(query, "secret")){
		if(is_admin){
			puts(password);
		} else {
			puts("not admin");
		}
	}

	const char* ptr = strstr(query, "lookup");
	if(ptr){
		char idx = *(ptr + 6) - '0';
		if(idx >= 0 && idx <= 9){
			puts(*strings[idx]);
		}
	}
}

int main(int argc, char** argv){
	if(argc != 2){
		printf("Usage: %s <query>\n", argv[0]);
	} else {
		execute_query(argv[1]);
	}
	return 0;
}
