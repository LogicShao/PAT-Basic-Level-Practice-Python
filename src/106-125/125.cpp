#include <bits/stdc++.h>

int main() {
  std::cin.tie(nullptr)->sync_with_stdio(false);

  std::string s, p;
  std::cin >> s >> p;

  std::vector snxtchr(s.size(), std::vector<int>(26, -1));
  for (int i = (int)s.size() - 2; i >= 0; --i) {
    snxtchr[i] = snxtchr[i + 1];
    snxtchr[i][s[i + 1] - 'a'] = i + 1;
  }

  int l = 0, r = s.size() - 1;
  for (int i = 0; i < s.size() - p.size() + 1; ++i) {
    if (s[i] != p[0])
      continue;
    int j = i;
    for (int k = 1; k < p.size(); ++k) {
      j = snxtchr[j][p[k] - 'a'];
      if (j == -1)
        break;
    }
    if (j != -1 && j - i < r - l) {
      l = i, r = j;
    }
  }

  std::cout << s.substr(l, r - l + 1) << '\n';
}