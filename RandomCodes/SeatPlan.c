#include<stdio.h>

void findType(int seat)
{   
    int types[] = {1,6,7,12,2,5,8,11,3,4,9,10};
    int i = 0;
    while(seat != types[i])
    {
        i++;
    }
    
    if(i <= 3)
        printf("WS");
    else if(i <= 7)
        printf("MS");
    else
        printf("AS");
    
}

int facingSeat(int currentSeat)
{
    int faceSeat = 13 - currentSeat;
    return faceSeat - currentSeat;
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
    int diff = facingSeat(temp);
    printf(" %d",seatNo + diff);
    return 0;
}