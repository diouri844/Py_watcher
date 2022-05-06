import java.util.Scanner;

public class teste {
	private static Scanner buf;
	public static void main(String[] args) {
		// TODO Auto-generated method stub:
        System.out.printf("watcher demo :) ");
		double a,b,resultat;
		String operation;
		buf=new Scanner(System.in);
		System.out.printf(" Donner l operateur 1 :     ");
		a=buf.nextDouble();
		System.out.printf("\n Donner l operateur 2 :    ");
		b=buf.nextDouble();
		System.out.printf("\n Donner l operation a efectuer ( <+> , <-> , <*> , </> ,):	");
		operation=buf.next();
		// tester sur les operations : 
		switch (operation) {
		case "<+>": resultat=a+b;
		System.out.printf("\n resultat :   %.2f %s %.2f = %.2f ",a,operation,b,resultat);
		break;
		case "<->": if(a>=b) {
			resultat=a-b;
			System.out.printf("\n resultat :   %.2f %s %.2f = %.2f ",a,operation,b,resultat);
		}else {
			System.err.printf("\n Operateur non disponible ");
		}
		System.exit(0);
		break;
		case "<*>":resultat=a*b;
		System.out.printf("\n resultat :   %.2f %s %.2f = %.2f ",a,operation,b,resultat);
		break;
		case "</>":if(b!=0) {
			resultat=a/b;
		}else {
			System.err.printf("\n Operateur non disponible ");
		}
		System.exit(0);
		break;
		}
		
	}

}
