// program to tell maximum possible height of triangle using number of coin

#include<iostream>
using namespace std;

int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        int N ,a=0;
        cin>>N;
        for(int i=1;i<=N;i++)
        {
            N=N-i;
            a=a+1;
        }
        cout<<a;
    }
}
