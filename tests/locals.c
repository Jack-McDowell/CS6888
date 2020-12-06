// INVARIANT(arg, local): RETURN(func) -> local > arg
void func(int arg){
	int local = arg ^ 1;
}

int main(int argc, char** argv){
	if(argc != 2){
		return -1;
	} else {
		func(*argv[1]);
	}
}
