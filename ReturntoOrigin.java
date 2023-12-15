// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.*;
class Solution
{
    public void Judgecircle(String moves)
    {
        int U=0,R=0,D=0,L=0;
        for(int i=0;i<moves.length();i++)
        {
            if(moves.charAt(i)=='U')
              U++;
            else if(moves.charAt(i)=='D')
              D++;
            else if(moves.charAt(i)=='L')
              L++;
            else
               R++;
        }
       if( U==D && L==R)
       System.out.println("true");
       else
      System.out.println("False");
    }
}
class ReturntoOrigin{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String Moves=sc.nextLine();
        Solution obj=new Solution();
        obj.Judgecircle(Moves);
    }
}
