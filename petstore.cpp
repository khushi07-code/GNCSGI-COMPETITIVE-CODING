// program for check the 2 person have exactly same type of pet or not in total also
#include<iostream>
using namespace std;

int checkarray(int array[],int N, int n)
{
    for(int i=0; i<N;i++)
    {
        if(array[i]==n)
        {
            return 1;
        }
    }
    return 0;
    
}
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        int N;
        cin>>N;
        int A[N];
        for(int i=0; i<N;i++)
        {
            cin>>A[i];
        }
       
        if(N%2!=0)
        {
            cout<<"NO";
        }
        else
        { 
            int top1=-1 ,top2=-1;
            int N1=N/2,N2=N/2;
            int a[N1],b[N2];
            int g,h;
            for(int i=0;i<N1;i++)
            {
                g=A[i];
                 if(top1==-1)
                 a[++top1]=g;
                if(checkarray(a,N1,g)==0)
                {
                    if(top1<N1)
                      a[++top1]=g;
                }
            }
            for(int j=N2; j<N;j++)
            {
                 h=A[j];
                 if(top2==-1)
                 b[++top2]=h;
                else if(checkarray(b,N2,h)==0)
                {
                    if(top2<N2)
                      b[++top2]=h;
                }
            }
            for(int i=0;i<=top1;i++)  
            {
              if(checkarray(b,N2,a[i])==0)
                   {
                     cout<<"NO";
                     exit(1);;
                   }
            }
            cout<<"YES";
            
        }
    }
}
