int longestCommonSum(vector<int>& a1, vector<int>& a2) {
    int n = a1.size();
    unordered_map<int, int> d;
    int s1 = 0, s2 = 0, maxi = 0;

    for (int i = 0; i < n; ++i) {
        s1 += a1[i];
        s2 += a2[i];

        int diff = s2 - s1;

        if (diff == 0) {
            maxi = i + 1;
        } else if (d.find(diff) != d.end()) {
            maxi = max(maxi, i - d[diff]);
        } else {
            d[diff] = i;
        }
    }

    return maxi;
}
