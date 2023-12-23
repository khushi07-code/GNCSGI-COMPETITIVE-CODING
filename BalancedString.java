import java.util.*;
class get{
	 get(String s)
	 {     int L=0,R=0,pair=0;
		 for(int i=0;i<s.length();i++)
		 {
			 if(s.charAt(i)=='L')
				 L++;	 
			 if(s.charAt(i)=='R')
			  R++;
			if(L==R)
			{
				pair++;
				L=R=0;
			}  
		 }
     System.out.println(pair);      
	 }
}
public class balancedstring {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		String s=sc.nextLine();
		 new get(s);
	}
}
