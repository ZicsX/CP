#include <bits/stdc++.h>
using namespace std;

int arr[100][100];

int main() {
	int sum,rowrepc,colrepc;
	int t; cin >> t;
	int tcase = 1;
	while(t-->0) {
		int n; cin >> n;
		bool countn[n] = {false} , countm[n] = {false};
		sum = 0;
		rowrepc=0;
		colrepc=0;

		for(int i=0;i<n;++i){
			for(int j=0;j<n;++j){
				cin >> arr[i][j];
				if(i==j){
					sum+=arr[i][j];
				}
			}
		}
		for(int i=0;i<n;++i){
			for(int j=0;j<n;++j){
				for(int k = j+1;k<n ;++k){
					if(countm[i] && countn[i])
                        break;
                    
                    
                    if(!countn[i]){
                        
                        if (arr[i][j] == arr[i][k]){
                            countn[i] = true;
						    rowrepc++;
                        }
					}
					if(!countm[i]){
					    if(arr[j][i] == arr[k][i]){
    					    countm[i] = true;
						    colrepc++;
					    }
					}
					
				}
				
			}
		}
		cout <<"Case #"<<tcase<<": "<<sum<<" "<<rowrepc<<" "<<colrepc<<endl;
		tcase++;
	}
	return 0;
}