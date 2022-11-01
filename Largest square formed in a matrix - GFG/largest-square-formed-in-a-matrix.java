//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG{
    public static void main(String args[])throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while(t-- > 0){
            String a[] = in.readLine().trim().split("\\s+");
            int n = Integer.parseInt(a[0]);
            int m = Integer.parseInt(a[1]);
            String a1[] = in.readLine().trim().split("\\s+");
            int mat[][] = new int[n][m];
            for(int i = 0;i < n*m;i++)
                mat[i/m][i%m] = Integer.parseInt(a1[i]);
            
            Solution ob = new Solution();
            System.out.println(ob.maxSquare(n, m, mat));
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution{
    static int maxSquare(int n, int m, int matrix[][]){
        //initializing sentinal varibles
        int maxSqr=0 , rows=matrix.length , column=matrix[0].length;
        //base case
        if(rows==0) return 0;
        //dp matrix that we will be making
        int[][] dp=new int[rows+1][column+1];
		
        //Iterate over the matrix
        for(int i=1;i<=rows;i++)
            for(int j=1;j<=column;j++) {
                ///we found the 1 in our binary matrix 
                if(matrix[i-1][j-1]==0) continue;
                dp[i][j]=Math.min(dp[i-1][j],Math.min(dp[i-1][j-1],dp[i][j-1])) + 1;
                maxSqr=Math.max(maxSqr,dp[i][j]);
            }
        return maxSqr;
    }
}