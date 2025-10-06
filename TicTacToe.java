/*
 * TicTacToe.java
 *
 * Charlie Gifford
 *
 * uses Board object to play TicTacToe
 */

import java.util.Scanner;

public class TicTacToe
{
	public static void printRules()
	{
		System.out.println("\nPlay alternates between X and O.");
		System.out.println("X goes first.");
		System.out.println("Rows and columns go from 1 to 3.\n");
	}

	public static void main (String [] args)
	{
		printRules();
		Scanner scanner = new Scanner(System.in);

		Board b = new Board();
		for(int i = 0; i < 9; i++){
			if(i % 2 == 0){
				System.out.println("X's turn");

				System.out.println("Row: ");
				int rowX = scanner.nextInt();

				System.out.println("Column ");
				int columnX = scanner.nextInt();

				if(b.isValidMove(rowX, columnX) == false || b.isEmpty(rowX, columnX) == false){
					System.out.println("Invalid move.");
					i--;
					continue;
				}else{
					b.makeMove('X', rowX, columnX);
					System.out.println(b.toString());
					if(b.gameWon() == true){
						System.out.println("Player X won!");
						break;
					}
				}	
				}else{
					System.out.println("O's turn");

					System.out.println("Row: ");
					int rowX = scanner.nextInt();

					System.out.println("Column ");
					int columnX = scanner.nextInt();

					if(b.isValidMove(rowX, columnX) == false || b.isEmpty(rowX, columnX) == false){
						System.out.println("Invalid move.");
						i--;
						continue;
					}else{
						b.makeMove('O', rowX, columnX);
						System.out.println(b.toString());
						if(b.gameWon() == true){
							System.out.println("Player O won!");
							break;
						}
				}
			}
			if(i == 8){
				System.out.println("Tie game!");
			}
		}
	}
}

