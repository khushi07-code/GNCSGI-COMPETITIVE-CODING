#include<iostream>
using namespace std;
int main()

{
    int T;
    cin>>T;
    while(T--)
    {
        int D,C;
        cin>>D>>C;
        int A[3],B[3];
        for(int i=0;i<3;i++)
        {
            cin>>A[i];
        }
       for(int i=0;i<3;i++)
        {
            cin>>B[i];
        }
        int costA=0,costB=0,totalwithC=0,totalwithoutC=0;
        for(int i=0;i<3;i++)
        {
            costA=costA+A[i];
            costB=costB+B[i];
        }
        if(costA>=150 && costB>=150)
        {
           totalwithC=costA+costB+C;
           totalwithoutC=costA+costB+2*D;
        }
        else if(costA>=150 || costB>=150)
        {
            totalwithC=costA+costB+C+D;
            totalwithoutC=costA+costB+2*D;
        }
        if(totalwithC>totalwithoutC || totalwithC==totalwithoutC)
        {
            cout<<"NO";
        }
        else{
            cout<<"yes";
        }


    }
}
