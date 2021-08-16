---
layout: post
title: "Day 34: Slowly Building Up"
date: 2021-08-16 +0530
categories: competitive-programming
---
### Disclaimer:
> I am a beginner in competitive programming, and this is me documenting my learnings. So, anything I say is just what I think at the moment and should not be taken as hard truths.

# Confession
I know, I am being super inconsistent. Today is Day 34, it has been 25 days till last coding day.
Nevertheless, let us get back on the horse now.

### Problem 1: [Coin Rows](https://codeforces.com/problemset/problem/1555/C)


Main points:
- The player can move only right or down
- We need to minimize the score, i.e., the coins Bob collects.

First solution that comes in mind is to maximize the coins Alice collects, but that is not the goal.
More score for Alice doesn't imply overall minimum score for Bob.


My solution:
```cpp
#define T int tt; cin >> t; while(tt--)

main() {
  T {
    int n; cin >> n;
    vvl v(2, vl(n));
    for(auto& row: v) for(auto& e: row) cin >> e;
    ll sum1 = accumulate(all(v[0]), 0L);
    ll sum2 = 0;
    ll bob_score = INT_MAX;
    forn(i, n) {
        sum1 -= v[0][i];
        bob_score = min(bob_score, max(sum1, sum2));
        sum2 += v[1][i];
    }
    cout << bob_score << endl;
  }
}
```

Official solution:
```cpp
#define T int tt; cin >> t; while(tt--)
#define all(x) begin(x), end(x)

main() {
  T {
    int n; cin >> n;
    vvl v(2, vl(n));
    for(auto& row: v) for(auto& e: row) cin >> e;
    ll sum1 = accumulate(all(v[0]), 0L);
    ll sum2 = 0;
    ll bob_score = INT_MAX;
    forn(i, n) {
        sum1 -= v[0][i];
        bob_score = min(bob_score, max(sum1, sum2));
        sum2 += v[1][i];
    }
    cout << bob_score << endl;
  }
}
```

#### Things to learn:

On Algorithmic thinking:
- Try to make a guess on what could be possible.
- Check for restrictions if any.


On Technical point:
- Write little code as possible.
- Use small variable name.
- Practice to type fast.


In this particular problem we just needed to iterate through all possible solution for Bob and find the
minimum from it.

### Problem 2: [Mikasa](https://codeforces.com/problemset/problem/1554/C)

The gist of the problem:

n, m are given and we need to find smallest non-negative number not present in the sequence
(n^0, n^1...n^m)

My first submission: (TLE) [O(n) solution/test case]
```cpp
main() {
  T {
    ll n, m;
    cin >> n >> m;
    forn(i, max(n, m)+1) {
        ll val = i^n;
        if(val > m) {
            cout << i << endl;
            break;
        }
    }
  }
}
```

My solution after reading the editorial (not seeing the code)
```cpp
main() {
  T {
    ll n, m;
    cin >> n >> m;
    if(m < n) cout << 0 << endl;
    else {
        ll p = m+1;
        ll ans = 0;
        for(int i = 31; i >= 0; i--) {
            ll t = (1L<<i);
            if((ll(t&p) > 0) && (ll(t&n) == 0)) {
                ans = ans^t;
            } else {
                if(ll(ans^n) >= p) break;
                if(ll(p&t) > 0) {
                    if(ll(n&t) > 0) continue;
                    else {
                        ans = ans^t;
                    }
                }
            }
        }
        cout << ans << endl;
    }
  }
}
```

This is the official editorial solution. Still I need to wrap my head around it.
```cpp
main() {
 int t; cin >> t;
  while (t--) {
    int n, m; cin >> n >> m;
    ++m;
    int ans = 0;
    for (int k = 30; k >= 0 and n < m; k--) {
      if ((n >> k & 1) == (m >> k & 1)) continue;
      if (m >> k & 1) ans |= 1 << k, n |= 1 << k;
    }
    cout << ans << '\n';
  }
}
```

#### Things to learn:

On Technical point:
- Know C++ well. Some time went in debugging as I was comparing `t&n > 0`, it didn't work out.
- Learn ways to debug better.


## Algorithm

We didn't learn any new algorithm of sort, but we did studied how to use C++ STL algorithm, such as
- accumulate
- partial_sum
- reduce

As Sean Parent said, we should know our algorithms and idioms.
