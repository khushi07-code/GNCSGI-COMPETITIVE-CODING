#include<iostream>
using namespace std;

int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        int a=0;
       char X[10],Y[10];
       cin>>X>>Y;
       for(int i=0;i!='\0';i++)
       {
            if(X[i]=='?'&& Y[i]!='?')
             {
                 X[i]=Y[i];
             }
            if(Y[i]=='?'&& X[i]!='?')
             { 
               Y[i]=X[i];
             }
             if(X[i]!='?'&& Y[i]!='?')
             {
                  if(X[i]!=Y[i])
                  {
                     a=a+1;
                     break;
                  }
             }
       }
       if(a==0)
       {
          cout<<"YES";
       }
       else
      {
        cout<<"NO";
      }
    }   
       
}
