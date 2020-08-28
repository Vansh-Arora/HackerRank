#include<stdio.h>

void findType(int seat)
{   
    // Array has seats in groups of 4
      //  0 - 3 Window Seats(WS)
      //  4 - 7 Middle Seats(MS)
      //  8 - 11 Aisle Seats(AS)
    int types[] = {1,6,7,12,2,5,8,11,3,4,9,10};

    // Find the index where current seat lies
    int i = 0;
    while(seat != types[i])
    {
        i++;
    }
    
    // Check if index lies in range of WS, MS or AS
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
        temp = 12;          // For seat 12 temp will be 0 so we assign it 12 again

    findType(temp);

    int diff = facingSeat(temp);
    printf(" %d",seatNo + diff);
    
    return 0;
}