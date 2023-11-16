#include<iostream>
using namespace std;
int main()
{
    int T;
    cin>>T;
    while(T--)
   {
    int A,B,P,Q;
    cin>>A>>B>>P>>Q;
    int c=P/A;
    int d=Q/B;
    if(abs(c-d)<=1 && P%A==0 && Q/B==0)
    {
        cout<<"yes";
    }
    else
    {
        cout<<"NO";
    }
   }
}
