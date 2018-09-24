#include <iostream>
#include <stack>
#include <string>
#include <unordered_map>


using namespace std;

class Solution {

private:
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    typedef stack<int> intstack;
    unordered_map<char, intstack> _edgeStacks;
    unordered_map<char, intstack> _valueStacks;
    unordered_map<char, int> maxValueMap;

    void refreshStacks() {
        _edgeStacks.clear(); _valueStacks.clear();
        int alphabetLen = alphabet.length();

        _edgeStacks.reserve(alphabetLen);
        _valueStacks.reserve(alphabetLen);
        maxValueMap.reserve(alphabetLen);

        for (char c: alphabet) {
            _edgeStacks.emplace(c);
            _valueStacks.emplace(c);
        }
    }

    void updateStacks(char c, int k) {

    }

public:
    int characterReplacement(string s, int k) {
        this->refreshStacks();

        for (char c: s) {

        }

        // for
    }
};
