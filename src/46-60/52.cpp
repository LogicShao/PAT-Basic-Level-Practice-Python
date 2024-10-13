#include <iostream>
#include <string>

using namespace std;

int getString(string str, string a[]) {
  int k = 0;
  for (int i = 0; i < str.length(); i++) {
    if (str[i] != '[' && str[i] != ' ' && str[i] != ']') {
      a[k] += str[i];
    }
    if (str[i] == ']')
      k++;
  }
  return k;
}

bool isValid(int a, int b) {
  if (a <= b && a > 0)
    return true;
  else
    return false;
}

string s[3];
string hand[11], eye[11], mouth[11];
int main() {
  for (int i = 0; i < 3; i++) {
    getline(cin, s[i]);
  }
  int len1 = getString(s[0], hand);
  int len2 = getString(s[1], eye);
  int len3 = getString(s[2], mouth);
  int n;
  cin >> n;
  int num[n][5];
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < 5; j++) {
      cin >> num[i][j];
    }
  }
  for (int i = 0; i < n; i++) {
    int a = num[i][0];
    int b = num[i][1];
    int c = num[i][2];
    int d = num[i][3];
    int e = num[i][4];
    if (isValid(a, len1) && isValid(b, len2) && isValid(c, len3) &&
        isValid(d, len2) && isValid(e, len1)) {
      cout << hand[a - 1] << "(" << eye[b - 1] << mouth[c - 1] << eye[d - 1]
           << ")" << hand[e - 1] << endl;
    } else {
      cout << "Are you kidding me? @\\/@" << endl;
    }
  }
  return 0;
}