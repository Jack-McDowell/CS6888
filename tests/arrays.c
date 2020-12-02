int arr[4] = {
	2, 3, 4, 0
};
int idx = 0;

// INVARIANT(arr, idx): WRITE(arr[2]) -> arr[idx] < NEXT(arr[2])
int main(int argc, char** argv){
	if(argc != 2){
		return -1;
	} else {
		int idx2 = 2;
		if(*argv[1] == 'p'){
			idx2 = 3;
		}
		if(argv[1][1] != 'q'){
			idx = 3;
		}
		arr[idx2] = 1;
	}
}
