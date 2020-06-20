#include<stdio.h>
#include<math.h>

int main(){
	int T, N, i;
	int output[100];
	printf("Enter the no. of test cases: ");
	scanf("%d",&T);
	for(i = 0; i < T; i++){
		printf("Enter the maximum price of the item present on Philaland: ");
		scanf("%d",&N);
		
		int coin = 0;
		while(pow(coin,2) <= N){
			coin++;
		}
		output[i] = coin;
	}
	
	for(i = 0; i < T; i++){
		printf("%d\n",output[i]);
	}
}
