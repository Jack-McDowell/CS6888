int val = 2;

// INVARIANT(global val): RETURN() -> RETURN_VAL() > val
int main(int argc, char** argv){
	if(argc != 2){
		return -1;
	} else {
		val = 4;
		if(*argv[0] == 'j'){
			return 3;
		} else {
			return 5;
		}
	}
}
