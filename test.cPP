#include<iostream>
using namespace std;
class Student
{
private:
    int rollnum;
    float marks;
public:
    void setdata(){
        rollnum=1001;
        marks=99;
    }
    void showdata(){
        cout<<"Roll Number :"<<rollnum<<"Marks: " <<marks <<endl;
    }
};

int main(){
    Student shalini;
    shalini.setdata();
    shalini.showdata();

}
