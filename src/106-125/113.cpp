#include <bits/stdc++.h>

using LL = long long;

constexpr int base = 30;

int main() {
  std::string tmp = "0123456789abcdefghijklmnopqrstuvwxyz";
  std::map<char, int> mp;
  for (int i = 0; i < tmp.size(); ++i) {
    mp[tmp[i]] = i;
  }

  std::cin.tie(nullptr)->sync_with_stdio(false);
  std::string A, B;

  std::cin >> A >> B;
  std::reverse(A.begin(), A.end());
  std::reverse(B.begin(), B.end());

  std::string res;
  int carry = 0;
  for (int i = 0; i < std::max(A.size(), B.size()); ++i) {
    int sum = carry;
    if (i < A.size()) {
      sum += mp[A[i]];
    }
    if (i < B.size()) {
      sum += mp[B[i]];
    }
    carry = sum / base;
    sum %= base;
    res.push_back(tmp[sum]);
  }

  if (carry) {
    res.push_back(tmp[carry]);
  }

  while (res.size() > 1 && res.back() == '0') {
    res.pop_back();
  }

  std::reverse(res.begin(), res.end());

  std::cout << res << '\n';
}