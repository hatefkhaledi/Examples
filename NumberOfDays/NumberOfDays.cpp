#include <iostream>

using namespace std;

int main()
{
    int monthnumber;

    //Reading a month number from user

    cout << "Enter month number(1-12): ";
    cin >> monthnumber;

    switch (monthnumber)
    {
    case 1: cout << "31 days";
        break;
    case 2: cout << "28 or 29 days";
        break;
    case 3: cout << "31 days";
        break;
    case 4: cout << "30 days";
        break;
    case 5: cout << "31 days";
        break;
    case 6: cout << "30 days";
        break;
    case 7: cout << "31 days";
        break;
    case 8: cout << "31 days";
        break;
    case 9: cout << "30 days";
        break;
    case 10: cout << "31 days";
        break;
    case 11: cout << "30 days";
        break;
    case 12: cout << "31 days";
        break;
    default: cout << "Invalid input!!! enter month number between 1-12";

    }
    return 0;

}