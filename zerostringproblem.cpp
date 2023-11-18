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
        int S[N];
        cin>>S[N];
        int zero=0, one=0;
        for(int i=0; i<N;i++)
        {
              if(S[i]==0)
              {
                 zero=zero+1;
              }
              else
              {
                one=one+1;
              }
        }
        int answer;
        if(one>zero)
        {
            answer=zero+1;
        }
        else{
            answer=one;
        }
        
    }
}
