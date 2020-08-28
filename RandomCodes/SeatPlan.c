#include<stdio.h>

int findType(int seat)
{   
    int types[] = {1,6,7,12,2,5,8,11,3,4,9,10};
    int i = 0;
    while(seat != types[i])
    {
        i++;
    }
    
    if(i <= 3)
    {
        printf("WS");
        return 1;
    }
    else if(i <= 7)
    {
        printf("MS");
        return 2;
    }
    else
    {
        printf("AS");
        return 3;
    }
    
}
int main()
{
    int seatNo;
    printf("Enter seat number: ");
    scanf("%d",&seatNo);

    int temp = seatNo % 12; // Since each section has 12 seats.
    if(temp == 0)
        temp = 12;

    findType(temp);
}