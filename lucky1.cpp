// if number N is divisble by 2^p and p is divisible by 2 then print 1 (lucky) else 0(not lucky)
#include<iostream>
#include<math.h>
using namespace std;
int main()
{
   int T;
   cin>>T;
   while(T--)
   {
      int N;
      cin>>N;
      int a;
      a=log2(N);
      int b;
      b=pow(2,a);
      while(N%b!=0)
      {
        a--;
        b=pow(2,a);
      }
      (a%2==0)?cout<<1:cout<<0;
      
   }
}
