import java.util.*;

public class leetcode1 {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		System.out.println("X=");
		int X=sc.nextInt();
		int b=String.valueOf(X).length();
		int a=0;
		if(X>=Math.pow(-2,31)&& X<( Math.pow(2,31)-1))
		{ 
			if(X%10==0)
			{
				X=X/10;
				b=b-1;
			}
			while(b!=0)
			{ 
				a=a*10+X%10;
				X=X/10;
				b--;
			}	
		}
		 X=a;
		 System.out.println(X);

	}

}
