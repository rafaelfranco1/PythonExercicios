#include <stdio.h>
#include <stdlib.h>

int main() {
	
	int n1;
	int n2;
	
	printf("Digite o começo do intervalo");
	scanf("%d",&n1);
	printf("Digite o final do intervalor");
	scanf("%d",&n2);
	
	while (n1 <= n2) {
		if (n1 % 2 == 0 and n1 % 7 ==0) {
				
			printf("%d",n1);	
		}
		
		n1++;
		
	}
	
	return 0;
}