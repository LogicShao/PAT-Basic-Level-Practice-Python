#include <bits/stdc++.h>

using PII = std::pair<int, int>;

int main() {
  int head, n, k;
  scanf("%05d %d %d", &head, &n, &k);
  std::map<int, PII> link;
  for (int i = 0; i < n; ++i) {
    int addr, data, next;
    scanf("%05d %d %05d", &addr, &data, &next);
    link[addr] = {data, next};
  }
  std::array<std::vector<PII>, 3> res;
  for (int i = head; i != -1; i = link[i].second) {
    int idx = link[i].first < 0 ? 0 : link[i].first <= k ? 1 : 2;
    res[idx].emplace_back(i, link[i].first);
  }
  std::vector<PII> ans;
  for (int i = 0; i < 3; ++i) {
    for (auto &p : res[i]) {
      ans.emplace_back(p);
    }
  }
  for (int i = 0; i < ans.size(); ++i) {
    printf("%05d %d ", ans[i].first, ans[i].second);
    if (i == ans.size() - 1) {
      printf("-1\n");
    } else {
      printf("%05d\n", ans[i + 1].first);
    }
  }
}