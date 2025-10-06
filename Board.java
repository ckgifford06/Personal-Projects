/*
 * class for a Board object
 *
 * Charlie Gifford
 */


public class Board
{
	public static final int size = 3;

	private char [][] board;

	/*
	 * initializes board by placing a dot in each cell
	 */

	public Board()
	{
		this.board = new char [size][size];
		
		for(int i = 0; i < size; i++){
			for(int j = 0; j < size; j++){
				board[i][j] = '•';
			}
		}

	}

	/*
	 * places player's symbol on specified row and column
	 */

	public void makeMove(char p, int r, int c)
	{
		board[r-1][c-1] = p;

	}

	/*
	 * returns true if row and column are within board 
	 */

	public boolean isValidMove(int r, int c)
	{
		if(r > 3 || r <= 0){
			return false;
		}else if(c > 3 || c <= 0){
			return false;
		}else{
			return true;
		}
	}

	/*
	 * returns true if space is unfilled
	 */

	public boolean isEmpty(int r, int c)
	{
		if(board[r-1][c-1] == '•'){
			return true;
		}else{
			return false; 
		}
	}

	/*
	 * returns true if any row, column, or diagonal is filled with
	 * one player's symbol
	 */

	public boolean gameWon()
	{
		if(board[0][0] == 'X' && board[0][1] == 'X' && board[0][2] == 'X' || board[0][0] == 'O' && board[0][1] == 'O' && board[0][2] == 'O'){
			return true;
		}else if(board[1][0] == 'X' && board[1][1] == 'X' && board[1][2] == 'X' || board[1][0] == 'O' && board[1][1] == 'O' && board[1][2] == 'O'){
			return true;
		}else if(board[2][0] == 'X' && board[2][1] == 'X' && board[2][2] == 'X' || board[2][0] == 'O' && board[2][1] == 'O' && board[2][2] == 'O'){
			return true;
		}else if(board[0][0] == 'X' && board[1][0] == 'X' && board[2][0] == 'X' || board[0][0] == 'O' && board[1][0] == 'O' && board[2][0] == 'O'){
			return true;
		}else if(board[0][1] == 'X' && board[1][1] == 'X' && board[2][1] == 'X' || board[0][1] == 'O' && board[1][1] == 'O' && board[2][1] == 'O'){
			return true;
		}else if(board[0][2] == 'X' && board[1][2] == 'X' && board[2][2] == 'X' || board[0][2] == 'O' && board[1][2] == 'O' && board[2][2] == 'O'){
			return true;
		}else if(board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X' || board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O'){
			return true;
		}else if(board[0][2] == 'X' && board[1][1] == 'X' && board[2][0] == 'X' || board[0][2] == 'O' && board[1][1] == 'O' && board[2][0] == 'O'){
			return true;
		}else{
			return false;
		}
	}

	/*
	 * returns string representation of board
	 *
	 * | X O X |
	 * | . O . |
	 * | . . . |
	 */

	
	public String toString()
	{
		String newBoard = "";

		for(int i = 0; i < size; i++){
			newBoard += " | ";
			for(int j = 0; j < size; j++){
				newBoard += board[i][j] + " ";
			}
			newBoard += "| \n";
		}
		return newBoard;
	}
	
}