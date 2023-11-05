#include<iostream>
using namespace std;

int main()
{
    int T;
    cin>>T;

    while(T--!=0)
    {
        int cost=0;
        int N , X;
        cin>>N>>X;
        int A[N], B[N];
        for(int i=0; i<N;i++)
        {
            cin>>A[i];
        }
        for(int i=0;i<N; i++)
        {
            cin>>B[i];
        }
        for(int i=0; i<N; i++)
        {
            if(A[i]>=X)
            {
                cost+=B[i];
            }

        }
         cout<<"total cost:"<<cost<<endl;
}
}

  
