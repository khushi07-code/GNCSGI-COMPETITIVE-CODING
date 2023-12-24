import java.util.*;
public class AverageSalary {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		TreeSet<Integer> Salary=new TreeSet<Integer>();
		int size=sc.nextInt();
		while(--size!=-1)
		{
		    Salary.add(sc.nextInt()); 
		}
		System.out.println(Salary);
	   int min=Salary.first();
	   int max=Salary.last();
	   double Avg=(min+max)/2;
	   System.out.println(Avg);
	}

}
