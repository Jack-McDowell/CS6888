int val = 2;

// INVARIANT(global num32 val): RETURN() -> RETURN_VAL() > val
int main(int argc, char** argv){
	if(argc != 2){
		return -1;
	} else {
		val = 4;
		if(*argv[1] == 'j'){
			return 3;
		} else {
			return 5;
		}
	}
}
