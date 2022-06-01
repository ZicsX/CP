#include <bits/stdc++.h>
using namespace std;

int main() {
    
    int n,m,k;
    cin >> n>>m>>k;
    string place;
    int cost;
    int arr[n];

    double sum = 0.0;
    
    map<string, double> places; 

    for(int i = 0;i<k;++i){
        cin>>place>>cost;
        places[place] = cost;
    }

    vector<vector<string>> windows(m);
    
    int j;
    bool inpflg = false;

    for(int i = 0;i<n;++i){
        cin>>place;
        j=0;
        inpflg = false;
        while(j<m){
            if((!(windows[j].size()==0) && windows[j].back() == place) || ((windows[j].size()==0) || j == m-1)){
                windows[j].push_back(place);
                arr[i] = j+1;
                inpflg = true;
            }
            ++j;
            
            if(inpflg)
                break;
        }
    }

    
    for (int i = 0; i < windows.size(); i++) { 
        for (int j = 0; j < windows[i].size(); j++){
            if(j>0 && windows[i][j-1] == windows[i][j]){
                sum+=(places[windows[i][j]] - places[windows[i][j]]*2/10);
            }
            else
                sum+=places[windows[i][j]];       
        }
    } 
    
    cout<<sum<<"\n";

    for(int i =0; i<n;++i){
        cout<<arr[i]<<"\n";
    }
    
    return 0;
}
