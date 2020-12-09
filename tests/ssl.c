#include<stdlib.h>
#include<string.h>
#include<stdio.h>

//Modified heartbeat processing function for POC
//This function has the same basic bug as heartbleed, although it removes some of the utility functions as well as the
//component responsible for actually sending the leaked data back. However, the key vulnerability and the same logic
//remains present
// INVARIANT(local num8* pl, local unum64 pl_len): READ(pl[pl_len]) -> false
int dtls1_process_heartbeat(char *pl, unsigned int payload, unsigned long long pl_len){
    unsigned char *buffer, * bp;
    int r;
    unsigned short hbtype;
    //Padding isn't essential for bug
    unsigned int padding = 16; /* Use minimum padding */

    /* Allocate memory for the response, size is 1 byte
     * message type, plus 2 bytes payload length, plus
     * payload, plus padding
     */
    buffer = (unsigned char *)malloc(1 + 2 + payload + padding);
    //allocate all that memory without any checks
    bp = buffer;
    /* Enter response type, length and copy payload */
    *bp++ = 0;
    memcpy(bp, pl, payload);
    bp += payload;
    /* We don't actually need the random padding */
    char *pad = "0123456789ABCDEF";
    memcpy(bp, pad, padding);
    bp -= payload;
    //send the response back, even the stuff the attacker wasn't supposed to see
    puts(bp);
    return 0;
}
char *gib = "AFDBNADGINOPKFNWPOIBDANK:NSFPQIOBNNDAFKJQWIOPJGNBAPSOFI:QKBNEIOJW:AKNBIEO:JFAKFNGOEIBJE:AFJKAFJ";

int main(int argc, char **argv){
    if(argc != 2){
        return -1;
    }
    int len = argv[1][0];
    int cpyLen = argv[1][1];
    char* msg = (char *)malloc(len);
    memcpy(msg, gib, len);
    dtls1_process_heartbeat(msg, cpyLen, len);
    return 0;
}
