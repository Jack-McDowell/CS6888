int UID = 1;
int* pUID = &UID;

// INVARIANT(global num32* pUID): WRITE(*pUID) -> NEXT(*pUID) >= *pUID
int get_new_id(char c){
	if(c == 's'){
		UID -= 1;
	} else {
		UID += 1;
	}

	return UID;
}

int main(int argc, char** argv){
	if(argc != 2){
		return -1;
	} else {
		return get_new_id(*argv[1]);
	}
}
