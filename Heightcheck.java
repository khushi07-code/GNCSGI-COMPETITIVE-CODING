import java.util.*;
class Solution
{
	Solution(Integer Height[])
	{
		Integer expected[]=Height.clone();
		Arrays.sort(expected);
		int indice=0;
		for(int i=0;i<Height.length;i++)
		{    
			if(Height[i]!=expected[i])
			    indice++;
		}
		System.out.println(indice);
	}
}
public class heightchecker {
     public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		Integer size=sc.nextInt();
		Integer height[]=new Integer[size];
		for(int i=0; i<size;i++)
		{
			height[i]=sc.nextInt();
		}
		new Solution(height);
		
	}

}
