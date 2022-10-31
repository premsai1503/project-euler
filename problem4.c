#include <stdio.h>
#include <stdlib.h>

static int is_palindrome(const unsigned long in) {
    unsigned long r = 0;
    for(unsigned long x = in; x; x /= 10)
        r = r * 10 + x % 10;
    return r == in;
}

int main(int argc, char* argv[]) {
    unsigned long max = argc > 1 ? strtoul(argv[1], 0, 10) : 0;
    if(!max || max > 9999)
        max = 999;
    unsigned long _a = 0, _b = 0, _m = 0; // best yet
    for(unsigned long a = max, a_min = 1; a >= a_min; --a)
        for(unsigned long b = max, b_min = _m / a + 1; b >= b_min; --b)
            if(is_palindrome(a*b)) {
                _a = a, _b = b, _m = a*b, a_min = _m / max + 1;
                break;
            }
    printf("Biggest palindrome-number which is product of two natural numbers"
        " no bigger than %lu: %lu = %lu * %lu\n", max, _m, _a, _b);
    return 0;
}
