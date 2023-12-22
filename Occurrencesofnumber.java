import java.util.*;
class solution
{
	  solution(int Array[])
	{
		int size=Array.length;
		int count=0;
		int prev=count;
		boolean flag=false;
		for(int i=0;i<size;i++)
		{  
		    if(i==size-1 || Array[i]!=Array[i+1] && i<size-1)
		    {      prev=count;
		    	   count=0;    
			      for(int j=0;j<size;j++)
			       {
				        if(Array[i]==Array[j])
				          count++;
			       } 
				    if(count==prev)
				     {
				    	  flag=true;
					       System.out.println("false");
					       break;
				     }
		     } 
		}
		if(flag==false)
	       System.out.println("true");
	    
	}
}
public class occurrences {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("enter the size");
        int size=sc.nextInt();
        int A[]=new int[size];
        for(int i=0;i<size;i++)
        {
            A[i]=sc.nextInt();
        }
       new hi(A);
       
  
}
}
