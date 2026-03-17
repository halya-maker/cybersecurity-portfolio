#include <iostream>
#include <fstream>
using namespace std;

void addPassword() {
    string website, password;

    cout << "Enter website: ";
    cin >> website;

    cout << "Enter password: ";
    cin >> password;

    ofstream file("passwords.txt", ios::app);
    file << website << " " << password << endl;
    file.close();

    cout << "Password saved.\n";
}

void viewPasswords() {
    string website, password;

    ifstream file("passwords.txt");

    cout << "\nSaved Passwords:\n";

    while (file >> website >> password) {
        cout << website << " : " << password << endl;
    }

    file.close();
}

int main() {

    int choice;

    while (true) {

        cout << "\n=== Password Manager ===\n";
        cout << "1. Add Password\n";
        cout << "2. View Passwords\n";
        cout << "3. Exit\n";

        cout << "Choose: ";
        cin >> choice;

        if (choice == 1)
            addPassword();

        else if (choice == 2)
            viewPasswords();

        else if (choice == 3)
            break;

        else
            cout << "Invalid option\n";
    }

    return 0;
}
