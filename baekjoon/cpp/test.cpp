#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> v(10);int sum=0;
    for(int i=0;i<10;i++)scanf("%d",&v[i]),sum+=v[i];
    for(int i=0;i<10;i++)v[i]=min(sum-v[i]+!!i,v[i]);
    sum=accumulate(v.begin(),v.end(),0);
    vector<int> ans;
    while(sum){
        for(int i=9;i>=0;i--){
            if(!v[i]||(!ans.empty()&&ans.back()==i))continue;
            v[i]--,sum--;
            int mx=*max_element(v.begin(),v.end());
            if(mx>sum-mx+1)v[i]++,sum++;
            else{
                ans.push_back(i);
                break;
            }
        }
    }
    if(ans.empty())printf("0");
    else for(auto i:ans)printf("%d",i);
    return 0;
}