//  2022-12-07
//      14:46 - 15:44

#include <iostream>
using namespace std;

// #include <string>
#include <vector>
#include <fstream>

// different pairs of numbers between 1 and given int argument
vector <vector <int>> two_element_combinations(int highest) {
    vector <vector <int>> all_combinations;
    for (int i = 1; i <= highest; i++) {
        int current_first_number = i;
        int current_second_number = i;
        for (int j = current_first_number; j < highest; j++) {
            current_second_number += 1;
            vector <int> combination;
            combination.push_back(current_first_number);
            combination.push_back(current_second_number);
            // cout << current_first_number << " : " << current_second_number << endl;
            all_combinations.push_back(combination);
        }
    }
    return all_combinations;
}

bool tester(vector <vector <int>> combis, string data, int n) {
    for (int i = 0; i < combis.size(); i++) {
        if (data[n-combis[i][0]] == data[n-combis[i][1]]) {
            return 0;
        }
    }
    return 1;
}

int marker_finder(string data, int marker_length) {
    int len = data.length();
    int marker_position;
    vector <vector <int>> combinations = two_element_combinations(marker_length);
    for (int n = 4; n < len-1; n++) {
        if (tester(combinations, data, n) == 1)
        {
        //     for (int i = 0; i < 4; i++) 
        //     {
        //         cout << data[i + n - 4];
        //     }
        // cout << endl;
        marker_position = n;
        return marker_position;
        }
    }
    cout << "nothing";
    return 0;
    }

string read_last_line(string filename) {
    string text;
    fstream newfile;
    newfile.open(filename);
    if (newfile.is_open()) {
        string line;
        while(getline(newfile, line)) {
            text = line;
        }
    newfile.close();
    }
    return text;
}

int main() {
    // string abc = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw";
    string data = read_last_line("notepad/058_advent_2022_day_6.txt");
    cout << "one: " << marker_finder(data, 4) << endl;
    cout << "two: " << marker_finder(data, 14) << endl;
}