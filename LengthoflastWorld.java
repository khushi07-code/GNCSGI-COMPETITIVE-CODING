import java.util.*;
class practice
{
	practice(String line)
	{
	    int len=line.length();
	    for(int i=len-1;i>=0;i--)
	    {
	    	if(line.charAt(i)==' ')
	       {
	    	   len=len-(i+1);
	            break;	
	       }
	    }
	    System.out.println(len);
	}
}
public class lengthoflastword {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String Line =sc.nextLine();
		new practice(Line);
		

	}

}
