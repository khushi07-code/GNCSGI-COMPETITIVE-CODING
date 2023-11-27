/* check for string M is subsequence of string N or not */
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        string M;
        string N;
        cin>>M;
        cin>>N;
        int a=0;
        for(int i=0;M[i]!='\0';i++)
        { int j=i;
           if(M[i]!=N[j++])
           {
              while(N[j]!='\0')
              {
                 if(M[i]!=N[j++])
                  a++;
                  else
                  break;
              }
           }
        }
        a==0?cout<<"yes":cout<<"No";
    }
}
