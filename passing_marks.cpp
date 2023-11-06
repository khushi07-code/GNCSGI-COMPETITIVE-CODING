#include<iostream>
using namespace std;

int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        int N,X ,pass,a;
        cin>>N>>X;
        int A[N];
        for(int i=0;i<N;i++)
        {
            cin>>A[i];
        }
        while(X--)
        {
             pass=0;
            for(int j=0; j<N; j++)
            {
                if(A[j]>pass)
                {
                    pass=A[j];
                    a=j;
                }
            }
            A[a]=0;
        }

        pass=pass-1;
        cout<<pass;
    }
}
