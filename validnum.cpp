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
        int X;
        cin>>X;
        int total=N*X,count=0;
        while(total!=0)
        {
             count++;
            total=total/10;
        }
        (count!=5)?cout<<"NO":cout<<"Yes";
    }

}
