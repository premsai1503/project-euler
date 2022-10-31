#include <stdio.h>
#include <math.h>

static unsigned long total;

int main(void)
{
  total = 0;

  for(unsigned int i = 1; i < 334; i++){
     total  = total + (3*i);
  }

  for(unsigned int j = 1; j < 1000; j++){

    if(j%5==0 && j%3!=0){
      total  += j; //total
    }else{
      total = total;
    }
  }

  printf("Project Euler problem 1 solution is ");
  printf("%lu \n", total);

  return 0;
}
