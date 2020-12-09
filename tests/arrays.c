int arr[4] = {
	0, 3, 4, 5
};
int idx = 0;

// INVARIANT(global num32* arr, global num32 idx): WRITE(arr[2]) -> arr[idx] <= NEXT(arr[2])
int main(int argc, char** argv){
	if(argc != 2){
		return -1;
	} else {
		int idx2 = 1;
		if(*argv[1] == 'p'){
			idx2 = 2;
		}
		if(argv[1][1] == 'q'){
			idx = 3;
		}
		arr[idx2] = 1;
	}
}
