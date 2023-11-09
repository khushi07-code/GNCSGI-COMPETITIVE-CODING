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
              if(i%2!=0)
              {
                A=A+1;
              }
              else{
                A=A+2;
              }
        }
        if(A==B)
            {
                cout<<"YES"<<endl;
            }
        else{
            cout<<"NO"<<endl;
        }
        
    }
}
