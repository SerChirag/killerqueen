#include <iostream>

using namespace std;

int main()
{
    int n, m=0;
    int input[1000], output[1000];
    cin>>n;
    for(int i=0;i<n;++i)
    {
        cin>>input[i];
    }
    for(int i=0;i<=n;++i)
    {
        if(m==1000)
        {
            break;
        }
        if(i==n)
        {
            output[m]=input[i-1];
            ++m;
            break;
        }
        if(input[i+1]==1)
        {
            output[m]=input[i];
            ++m;
        }
    }
    cout<<m<<endl;
    for(int i=0;i<m;++i)
    {
        cout<<output[i]<<" ";
    }
    return 0;
}