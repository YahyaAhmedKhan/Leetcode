class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int i=0; i<9; i++){
            int[] nums = new int[10];
            for (int j=0; j<9; j++){
                if (board[i][j]=='.' || board[i][j]==',') continue;
                int num = Character.getNumericValue(board[i][j]);
                nums[num]++;
            }
            for (int x : nums){
                if (x>1) return false;
            }
        }
        for (int i=0; i<9; i++){
            int[] nums = new int[10];
            for (int j=0; j<9; j++){
                if (board[j][i]=='.' || board[j][i]==',') continue;
                int num = Character.getNumericValue(board[j][i]);
                nums[num]++;
            }
            for (int x : nums){
                if (x>1) return false;
            }
        }
        for (int a=0; a<9; a+=3){
            for (int b=0; b<9; b+=3){
                int[] nums = new int[10];
                for (int i=0; i<3; i++){
                    for (int j=0; j<3; j++){
                        if (board[a+i][b+j]=='.' || board[a+i][b+j]==',') continue;
                        int num = Character.getNumericValue(board[a+i][b+j]);
                        nums[num]++;
                    }
                    
                }
                for (int x : nums){
                        if (x>1) return false;
                    }
            }
        }
        return true;
        
        
        
    }
}