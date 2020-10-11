// A left rotation operation on an array shifts each of the array's elements 1 unit to the left

#include<stdio.h>

void rotate(int a[], int n)
{
    int i,temp;
    temp = a[0]; // Store the first element

    // Shift each element to left
    for(i=0;i<n-1;i++)
    {
        a[i] = a[i+1];
    }

    // After the loop i will be at n-1 i.e last index of array
    a[i] = temp;
}
int main()
{
    int n,d;
    scanf("%d",&n);
    scanf("%d",&d);
    int a[n],i;
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<d;i++)
    {
        rotate(a,n);
    }
   for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
    return 0;
}