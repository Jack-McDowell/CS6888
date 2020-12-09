#include <stdio.h>

long long secret = 0x1337;
long long not_secret = 0x1234;

long long* arr[] = {
	&not_secret,
	&not_secret,
	&secret,
	&not_secret,
	&not_secret,
	&not_secret,
	&not_secret,
	&not_secret,
	&not_secret,
	&not_secret,
};

// INVARIANT(global num64 secret): READ(secret) -> false
int main(int argc, char** argv){
	if(argc != 2){
		return -1;
	} else {
		if(*argv[1] >= '0' && *argv[1] <= '9'){
			int val = *arr[*argv[1] - '0'];
			if(val == 0x1337)
				puts("yay");
			else
				puts("nay");
		} else {
			return -1;
		}
	}
}
