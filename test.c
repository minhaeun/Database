#include <stdio.h>

int main(){
    // 끄는거 1 키는거 0
    unsigned char led = 0xfe; // 11111110
    
    led = led << 1 | 0x1; // 11111101 11111011 11110111 11101111 11011111 1011111 01111111 11111111
    print((unsigned char*)&led);
    printf("%p", &led);
}