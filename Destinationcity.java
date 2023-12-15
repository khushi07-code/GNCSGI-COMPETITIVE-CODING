import java.util.*;
public class DestinationCity {

	public static void main(String[] args) {
		        Scanner sc=new Scanner(System.in);
		        System.out.println("enter the number of path:");
		        Integer length;
		        length=sc.nextInt();
		        String b[][]=new String[length][2];
		        System.out.println("enter  path:");
		        for(int i=0;i<length;i++)
		        {
		            for(int j=0;j<2;j++)
		            {
		            	System.out.println(i+" "+j+":");
		                b[i][j]=sc.next();
		            }
		        }
		    String last=b[0][1];
		  for(int i=1;i<length;i++)
		{ 
		    if(last.equals(b[i][0]))
		    {
		     last=b[i][1];
		    }
		}
		System.out.println(last);

		    
	}
		
}


