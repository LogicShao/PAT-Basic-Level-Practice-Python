#include <bits/stdc++.h>

int main() {
  std::cin.tie(nullptr)->sync_with_stdio(false);
  int n;
  std::cin >> n;
  std::map<int, int> mp;
  for (int i = 0; i < n; ++i) {
    int a, b;
    std::cin >> a >> b;
    mp[a] += b;
  }
  auto [a, b] = *std::max_element(mp.begin(), mp.end(), [](const auto& x, const auto& y) {
    return x.second < y.second;
  });
  std::cout << a << ' ' << b << '\n';
}