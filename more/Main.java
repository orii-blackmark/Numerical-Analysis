package more;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner minn=new Scanner(System.in);
		System.out.println("Enter the value of n1: ");
		int n1=minn.nextInt();
		System.out.println("Enter the value of n2: ");
		int n2=minn.nextInt();
	        int min;
	        if(n1>n2)
	        min=n2;
	        else
	        min=n1;
	        System.out.println("The minimum value Entered is "+min);
	}

}
