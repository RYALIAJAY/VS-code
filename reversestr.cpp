#include<iostream>
#include<cstring>
#include<vector>
using namespace std;
void reverse(string s)
{
    vector<string>temp;
    string str='';
    int i=0,l=s.length();
    for(i=0;i<l;i++)
    {
        if(s[i]==' ')
        {
            tmp.pushback(str);
            str='';
        }
        else
        {
            str=str+s[i];
        }
        for(i=temp.end();i!=temp.begin();++i)
        {
            cout<<temp.pushback<<" ";
        }
    }
}
int main()
{
    string s;
    cout<<"enter the string:"<<endl;
    cin>>s;
    reverse(s);
    return 0;
}