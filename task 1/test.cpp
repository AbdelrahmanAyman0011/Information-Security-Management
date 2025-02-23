#include <iostream>
#include <fstream>
#include <string>
using namespace std;
// Abdelrahman Ayman Saad Abdelhalim Mohamed   2205033
int main()
{
    ifstream file("file.txt");
    cout << "enter password " << endl;
    string line, password = "abdelrahman";
    bool flag = true;
    while (getline(file, line))
    {
        if (line == password)
        {
            flag = false;
            cout << "password found" << endl;
            cout << line << endl;
        }
    }
    if (flag)
        cout << "password not found" << endl;

    file.close();
    return 0;
}
