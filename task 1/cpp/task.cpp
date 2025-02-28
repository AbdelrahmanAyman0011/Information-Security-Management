#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

const string CORRECT_PASSWORD = "ahmed";

bool dictionary_attack(const string &filename, string &found_password)
{
    ifstream file(filename);

    string line;
    while (getline(file, line))
    {
        if (line == CORRECT_PASSWORD)
        {
            found_password = line;
            file.close();
            return true;
        }
    }

    file.close();
    return false;
}

// brute force attack (5-letter)
bool brute_force_attack(string &found_password)
{
    string charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    int len = charset.size();

    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < len; j++)
        {
            for (int k = 0; k < len; k++)
            {
                for (int l = 0; l < len; l++)
                {
                    for (int m = 0; m < len; m++)
                    {
                        string attempt = {charset[i], charset[j], charset[k], charset[l], charset[m]};
                        if (attempt == CORRECT_PASSWORD)
                        {
                            found_password = attempt;
                            return true;
                        }
                    }
                }
            }
        }
    }

    return false;
}

int main()
{
    string username, found_password;
    cout << "Enter your username: ";
    cin >> username;

    cout << "Attempting dictionary attack: " << endl;
    if (dictionary_attack("file.txt", found_password))
    {
        cout << "Success! Password found: " << found_password << endl;
    }
    else
    {
        cout << "Dictionary attack failed" << endl;
        cout << "brute force attack:" << endl;

        if (brute_force_attack(found_password))
        {
            cout << "Success! Password found: " << found_password << endl;
        }
        else
        {
            cout << "Brute force attack failed. Password not found." << endl;
        }
    }

    return 0;
}
