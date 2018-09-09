#include <stdio.h>

int main(int argc, char const *argv[]) {
  
  int a,b,c;
  
  printf("Enter three integers:\n");
  
  int nums = scanf("%d %d %d\n",&a,&b,&c);
  
  printf("You entered %d numbers: %d, %d, %d\n",nums,a,b,c);
  
  return 0;
}
