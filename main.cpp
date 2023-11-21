#include<stdio.h>
#include <stdlib.h>
int main() {
	int n;
	scanf("%d", &n);
	int arr[n];
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	for (int i = 0; i < n; i++) {
		int y;
		int x = scanf("%d", &y);
		if (x <= 0) {
			printf("0\n");
			exit(0);
		}

		if (arr[i] != y) {
			printf("0\n");
			exit(0);
		}


	}

	printf("1\n");


}