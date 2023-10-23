
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int knapSack(int w,int wt[],int val[],int i,int **dp)
{
	if(i<0) //If number of items 0
	{
		return 0;
	}
	if(dp[i][w]!=-1)
	{
		return dp[i][w];
	}
	if(wt[i]>w) //if weight of the item is greater than capacity of the bag
	{
		dp[i][w] = knapSack(w,wt,val,i-1,dp); //store the profit for the last item
	}
	else //if weight is less than the capacity
	{
		dp[i][w] = max(knapSack(w,wt,val,i-1,dp), val[i]+knapSack(w-wt[i],wt,val,i-1,dp));
	}
	
	return dp[i][w];
}
int main()
{
	int val[] = { 1,2,5,6 };
    int wt[] = { 2,3,4,5 };
    int w = 8;
    int n = sizeof(val) / sizeof(val[0]);
    int i,j;
    int **dp;
    dp = new int*[n];
    for (int i = 0; i < n; i++)
    {
        dp[i] = new int[w + 1];
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < w + 1; j++)
            dp[i][j] = -1;

    cout << knapSack(w, wt, val, n-1,dp);
	return 0;
}
