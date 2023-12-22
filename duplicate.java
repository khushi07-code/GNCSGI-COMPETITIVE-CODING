import java.util.*;
class Solution
{
	Solution(ArrayList<Integer> Array){
		int count;
		boolean flag=false;
		for(int i=0;i<Array.size();i++)
		{  
			 count=0;
		   for(int j=0;j<Array.size();j++)
		   {  
			   if(Array.get(i).equals(Array.get(j)))
			       count++;   
		   }
		   if(count>=2)
		   {
			   flag=true;
			   System.out.println("true");
			   break;
		   }
		}
		if(flag==false)
		{
			System.out.println("false");
		}
	}
}
public class Duplicate {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("enter the size");
        int size=sc.nextInt();
        ArrayList<Integer> A=new ArrayList<Integer>(size);
        for(int i=0;i<size;i++)
        {
            A.add(sc.nextInt());
        }
        new Solution(A);

	}

}
