---
layout: post
title:  "Type Conversion in C++"
date:   2021-07-23 +0530
categories: competitive-programming
---
### Disclaimer:
> I am a beginner in competitive programming, and this is me documenting my learnings. So, anything I say is just what I think at the moment and should not be taken as hard truths.


## char to int

```cpp
main() {
  char c = '5';
  int num = c - '0'; 
  cout << num << endl;

  // OR

  int number = atoi(&c);
  cout << number << endl;
}
```

## int to char [only 0-9]
```cpp
main() {
  int num = 5;
  char c = num + '0';
  cout << c << endl;  // output: 5
}
```

## string to int

```cpp
main() {
  string s = "256alphabet";
  int num = stoi(s);
  cout << num << endl;  // output: 256
}
```

`stoi` will parse any string and return integer. Additonally takes the `base` as parameter.

```cpp
main() {
  string s = "001010";
  int num = stoi(s, nullptr, 2);
  cout << num << endl; // output: 10
}
```


## int to string

```cpp
main() {
  int num = 256;
  string s = to_string(num);
  cout << s << endl;  // output: 256
}
```

## string to vector\<char\>

```cpp
#define all(x) begin(x), end(x)

main() {
  string s = "5555";
  vector<char> v(all(s));
  for(auto& c: v) cout << c << ' ';  // output: 5 5 5 5
}
```

## vector\<char\> to string

```cpp
#define all(x) begin(x), end(x)

main() {
  vector<char> v = {'1', '2', '3', '4', '5'};
  string s(all(v));
  cout << s << endl;  // output: 12345
}
```

## vector\<int\> to string

```cpp
main() {
  vector<int> v = {12345, 54321};
  string s;
  for(auto& e: v) s.append(to_string(e));
  cout << s << endl;
}
```

## string to vector\<int\>

```cpp
main() {
  string s = "12345";
  vector<int> v;
  for(auto& c: s) v.push_back(c-'0');

  // OR

  vector<int> v_new;
  transform(all(s), back_inserter(v_new), [](auto& c) { return c-'0'; });
}
```

Okay! Now we understand basic transformation from one form to another.

Now let us see some base conversions.

## base 10 to base 2 [decimal to binary]
```cpp
main() {
  int num = 5; // binary : 0101
  string binary = bitset<8>(num).to_string();
  cout << binary << endl;  // output: 00000101
}
```

## decimal to hex|oct [ int -> string ]

```cpp
main() {
  int num = 16; // hex: 10
  stringstream ss;
  ss << std::hex << num;
  cout << ss.str() << endl;  // output: 10

  // for oct
  ss << std::dec << num;
  cout << ss.str() << endl;  // output: 20
}
```


## some base to another base(dec/hex/oct) [ string -> string ]

```cpp
main() {
  string num = "16";
  stringstream ss;
  // consider s to be decimal
  // decimal to hex
  int initial_base = 10;
  ss << std::hex << stoi(num, nullptr, initial_base);
  cout << ss.str() << endl; // output: 10
}
```


## Sources:
- [Decimal to Binary](https://stackoverflow.com/questions/22746429/c-decimal-to-binary-converting)

## Further Read:
- [Base 10 to Base N conversion](https://stackoverflow.com/questions/12713999/base-10-to-base-n-conversions)
