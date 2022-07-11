#include <stdio.h>

int main() {
	long long n, p, i;
	long long result = 1;

	scanf("%lld %lld", &n, &p);

	for (i = 1; i <= n; i++) {
		result = result * i;
		result = result % p;
	}
	printf("%lld", result);
	return 0;
}