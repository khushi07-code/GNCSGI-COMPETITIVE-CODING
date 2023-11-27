#include<iostream>
using namespace std;

int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        int A, B;
        cin>>A>>B;
        for(int i=1;A!=B&&A<B;i++)
        {
            (i%2!=0)?A=A+1:A=A+2;
        }
        (A==B)?cout<<"YES":cout<<"NO"<<endl;
    }
}
