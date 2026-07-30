#include <unordered_map>
class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0;
        int right = 0;
        int mode = 0;
        int maxStringSize = 0;
        std::unordered_map<char, int> window = {};
        while (right < s.size()){
            if (window.count(s[right])){
                window[s[right]]++;
            } else{
            window[s[right]] = 1;
            }
            mode = window[s[right]] > mode ? window[s[right]] : mode;
            right++;
            while (right-left > mode + k){
                window[s[left]]--;
                left++;
            }
            maxStringSize = right-left > maxStringSize ? right-left : maxStringSize;
        }
        return maxStringSize;
    }
};
