//ugly number is number whose prime factor is only 2,3,5
import java.util.*;
class Solution{
	Solution(int number)
	{
		int i=2;
		while(number!=1)
		{
			if(number%i!=0)
			    i++;
			else {
	          if(i!=2 && i!=3 && i!=5)
				{ 
					System.out.println("false");
					break;
				}
	          number=number/i;
			}
		}
		 if(number==1)
			System.out.println("true");
	
	}
}
public class uglynumber {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
      new Solution(sc.nextInt());
	}
}
