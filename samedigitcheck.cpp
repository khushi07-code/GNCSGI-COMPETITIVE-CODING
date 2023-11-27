#include<iostream>
using namespace std;
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        int D;
        cin>>D;
        int one=0,zero=0;
        while(D!=0)
        {
            D%10==1?one++:zero++;
            D=D/10;
        }
        if(zero==1)
        {
            cout<<"yes";
        }
        else
        cout<<"no";

    }
}
