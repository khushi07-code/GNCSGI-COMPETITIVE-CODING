// program to check how many sane element present in both array

#include<iostream>
using namespace std;
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        int N;
        cin>>N;
        int *A=(int*)malloc(N*sizeof(int));
        int *B=(int*)malloc(N*sizeof(int));
        int i=0,j=0;
        while(i<N)
        {
            cin>>*(A+(i++));
        }
        while(j<N)
        {
            cin>>*(B+(j++));
        }
         int count=0;
        for(int i=0;i<N;i++)
        {    j=-1;
            while(j<N)
            {

                 if(*(A+i)==*(B+(++j)))
                 {
                    count++;
                 }
            }
        }
       cout<<count<<endl;
    }
}
