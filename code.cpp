#include <bits/stdc++.h>
using namespace std;

int solve(){
    int n,k;
    cin>>n>>k;
    vector<int>arr(n);
    for(int i =0; i<n; i++){
        cin>>arr[i];
    }
    int count = 0;

    for(int i =0 ;i<n ; i++ ){
        for(int j=i+1; j<n-1 ; j++){
            if(arr[j]<arr[i]){
                swap(arr[j] , arr[i]);
                count++;
            }
        }
    }

    if(count > k){
        cout<<"NO"<< endl;
    }
    else{
        cout<<"YES"<< endl;
    }
}
int main(){
    int t;
    cin>>t;
    while(t--){
        solve();
    }
}