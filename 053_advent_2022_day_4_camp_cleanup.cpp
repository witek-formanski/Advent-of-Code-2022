//  2022-12-04
//      12:15 - 14:12 part one
//      14:50 - 15:01 part two

#include <iostream>
using namespace std;

#include <vector>
#include <fstream>
#include <string>

vector <string> readlines_vect(string filename) {

    vector <string> rl_vect;
    ifstream file(filename);
    string str;

    while (getline(file, str)) {
        // cout << str << "\n";
        rl_vect.push_back(str);
    }
    
    return rl_vect;
}

#include <bits/stdc++.h>

vector <string> splitword_vect(string s, char del) {

    vector <string> sw_vect;
    stringstream ss(s);
    string word;

    while (!ss.eof()) {
        getline(ss, word, del);
        // cout << word << endl;
        sw_vect.push_back(word);
    }

    return sw_vect;
}

vector <vector <string>> splitlines_vect(vector <string> lines, char del) {

    vector <vector <string>> sl_vect;
    
    for (int i = 0; i < lines.size(); i++ ) {
        string line_str = lines[i];
        vector <string> line_vect = splitword_vect(line_str, del);
        sl_vect.push_back(line_vect);
    }

    return sl_vect;

}

vector <vector <vector <int>>> ints_3_vect(vector <vector <string>> vector_splitlines, char del) {
    
    vector <vector <vector <int>>> i3_vect;
    
    for (int i = 0; i < vector_splitlines.size(); i++) {
        vector <string> line_vect = vector_splitlines[i];
        vector <vector <int>> elf_int_vect_vect;
        for (int j = 0; j < line_vect.size(); j++) {
            string elf_str = line_vect[j];
            vector <string> elf_str_vect = splitword_vect(elf_str, del);
            vector <int> elf_int_vect;
            for (int k = 0; k < elf_str_vect.size(); k++) {
                string half_of_elf_str = elf_str_vect[k];
                int half_of_elf_int = stoi(half_of_elf_str);
                // cout << half_of_elf_int << endl;
                elf_int_vect.push_back(half_of_elf_int);
            }
            elf_int_vect_vect.push_back(elf_int_vect);
            // cout << endl;

        }
        i3_vect.push_back(elf_int_vect_vect);
    }


    return i3_vect;
}

int sumOfCompletelyOverlappingElves(vector <vector <vector <int>>> data_v3) {

    int ans = 0;

    vector <vector <vector <int>>> vector_of_pairs_of_elves = data_v3;
    for (int i = 0; i < data_v3.size(); i++) {
        
        vector <vector <int>> pair_of_elves = data_v3[i];
        vector <int> elf_left =  pair_of_elves[0];
        vector <int> elf_right = pair_of_elves[1];
        int elf_left_start = elf_left[0];
        int elf_left_end = elf_left[1];
        int elf_right_start = elf_right[0];
        int elf_right_end = elf_right[1];

        if (elf_left_start <= elf_right_start && elf_left_end >= elf_right_end) {
            ans += 1;
        }

        else if (elf_left_start >= elf_right_start && elf_left_end <= elf_right_end) {
            ans += 1;
        }
    }

    return ans;
}


int sumOfPartiallyOverlappingElves(vector <vector <vector <int>>> data_v3) {

    int ans = 0;

    vector <vector <vector <int>>> vector_of_pairs_of_elves = data_v3;
    for (int i = 0; i < data_v3.size(); i++) {
        
        vector <vector <int>> pair_of_elves = data_v3[i];
        vector <int> elf_left =  pair_of_elves[0];
        vector <int> elf_right = pair_of_elves[1];
        int elf_left_start = elf_left[0];
        int elf_left_end = elf_left[1];
        int elf_right_start = elf_right[0];
        int elf_right_end = elf_right[1];

        if (elf_left_start >= elf_right_start && elf_left_start <= elf_right_end) {
            ans += 1;
        }

        else if (elf_left_end >= elf_right_start && elf_left_end <= elf_right_end) {
            ans += 1;
        }

        else if (elf_right_start >= elf_left_start && elf_right_start <= elf_left_end) {
            ans += 1;
        }

        else if (elf_right_end >= elf_left_start && elf_right_end <= elf_left_end) {
            ans += 1;
        }

    }

    return ans;
}


int main() {
    
    string filename_1 = "notepad/047_advent_2022_day_4.txt";
    char delimiter = ',';
    char delimiter_2 = '-';

    vector <string> data_readlines = readlines_vect(filename_1);
    vector <vector <string>> data_splitlines = splitlines_vect(data_readlines, delimiter);
    
    vector <vector <vector <int>>> data_i3 = ints_3_vect(data_splitlines, delimiter_2);

    cout << "1: " << sumOfCompletelyOverlappingElves(data_i3) << endl;
    cout << "2: " << sumOfPartiallyOverlappingElves(data_i3) << endl;
    
}