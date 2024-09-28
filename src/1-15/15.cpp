#include <bits/stdc++.h>

using LL = long long;

struct stu {
  LL id;
  int de, cai;

  bool operator<(const stu& rhs) const {
    if (de + cai != rhs.de + rhs.cai) {
      return de + cai > rhs.de + rhs.cai;
    } else if (de != rhs.de) {
      return de > rhs.de;
    } else {
      return id < rhs.id;
    }
  }
};

int main() {
  std::cin.tie(nullptr)->sync_with_stdio(false);
  int n, l, h;
  std::cin >> n >> l >> h;
  std::vector<stu> s1, s2, s3, s4;
  std::vector<stu> s(n);
  for (int i = 0; i < n; ++i) {
    std::cin >> s[i].id >> s[i].de >> s[i].cai;
    if (s[i].de >= l && s[i].cai >= l) {
      if (s[i].de >= h && s[i].cai >= h) {
        s1.push_back(s[i]);
      } else if (s[i].de >= h) {
        s2.push_back(s[i]);
      } else if (s[i].de >= s[i].cai) {
        s3.push_back(s[i]);
      } else {
        s4.push_back(s[i]);
      }
    }
  }
  std::sort(s1.begin(), s1.end());
  std::sort(s2.begin(), s2.end());
  std::sort(s3.begin(), s3.end());
  std::sort(s4.begin(), s4.end());
  std::cout << s1.size() + s2.size() + s3.size() + s4.size() << '\n';
  for (auto [id, de, cai] : s1) {
    std::cout << id << ' ' << de << ' ' << cai << '\n';
  }
  for (auto [id, de, cai] : s2) {
    std::cout << id << ' ' << de << ' ' << cai << '\n';
  }
  for (auto [id, de, cai] : s3) {
    std::cout << id << ' ' << de << ' ' << cai << '\n';
  }
  for (auto [id, de, cai] : s4) {
    std::cout << id << ' ' << de << ' ' << cai << '\n';
  }
}