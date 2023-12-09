/* code for check  valid/unvalid  for prenthesis (for valid, must have pair of prenthesis and also in sequence otherwise it is unvalid)  */
import java.util.*;
public class leetcode2 {
	 public static void main(String args[])
	 {
		 char b[];
		 int j=0;
		 b=new char[10];
		 Scanner sc= new Scanner(System.in);
		 String A;
		 A=sc.nextLine();
		 for(int i=0 ;i<A.length();i++)
		 {   
		    if(A.charAt(i)=='(')
		    	{
		    	b[++j]=A.charAt(i);
		    	}
		    else if(A.charAt(i)=='[')
		    	{
		    	   b[++j]=A.charAt(i);
		            
		    	}
		    else if(A.charAt(i)=='{')
		    	{
		    	 b[++j]=A.charAt(i);
		          
		    	}
		    else
		    {
		    	  if( A.charAt(i)==')' && b[j]=='(')
		    	  { 
		    		--j;
		    	  }
		    	  if( A.charAt(i)==']' && b[j]=='[')
		    	  {
		    		 --j;
		    	  }
		    	  if( A.charAt(i)=='}' && b[j]=='{')
		    	  {
		    		  --j;
		    	  }
		    	  
		     }
		 }
         
		 if(j==0)
		 { 
			 System.out.println("true");
		 }
		 else
		 {
			 System.out.println("false");
		 }
		 sc.close();
		 
	 }

}
