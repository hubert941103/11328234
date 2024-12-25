def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # 檢查行
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    
    # 檢查列
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    # 檢查對角線
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"玩家 {current_player}，請輸入行（0-2）: "))
        col = int(input(f"玩家 {current_player}，請輸入列（0-2）: "))

        if board[row][col] != " ":
            print("這個位置已經被佔用了，請重新選擇！")
            continue

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"玩家 {winner} 獲勝！")
            break
        elif is_board_full(board):
            print_board(board)
            print("遊戲平局！")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()