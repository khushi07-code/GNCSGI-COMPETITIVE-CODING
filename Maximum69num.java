import java.util.*;
class Solution3
{
	void Maximumnumber(Integer num)
	{
		String Array=num.toString();
		for(int i=0; i<Array.length();i++)
		{
		    Character six='6';
			if(six.equals(Array.charAt(i)))
			{
				
				Array=Array.substring(0, i)+'9'+Array.substring(i+1);
			   break;
			}
		}
	   num=Integer.valueOf(Array);
	   System.out.println(num);
	}
}
public class maximun69num {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		Solution3 s=new Solution3();
		s.Maximumnumber(sc.nextInt());
		

	}

}
