#include <stdio.h>
main()
{
    long long int i,j,b,a=0;
    for(i=3; i<=600851475143/2; i++)
    {
        if(600851475143%i == 0)
        {
            for(j=2; j<=i/2; j++)
            {
                if(i%j == 0)
                {
                    a=1;
                    break;
                }            
            }
            if(a==0)
            {
                b=i;
            }
        }
      
    }
    printf("The sum of all multiples is %lld", b);
}
