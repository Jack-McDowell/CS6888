#include<stdlib.h>
#include<string.h>
#include<stdio.h>
char * secret;

// INVARIANT(global num8* msg, global num32 len): READ(msg[len]) -> false

//Modified heartbeat processing function for POC
//This function has the same basic bug as heartbleed, although it removes some of the fluff that makes
//this function actually perform ssl and breaks it down to the bearbones requirement to emulate the memory leak
int dtls1_process_heartbeat(char *pl, unsigned int payload){
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
char *msg;
char *gib = "AFDBNADGINOPKFNWPOIBDANK:NSFPQIOBNNDAFKJQWIOPJGNBAPSOFI:QKBNEIOJW:AKNBIEO:JFAKFNGOEIBJE:AFJKAFJ";
int len;
int cpyLen;

int main(int argc, char **argv){
    if(argc != 3){
        return -1;
    }
    int len = argv[1][0] - 'a';
    int cpyLen = argv[2][0] - 'a';
    msg = (char *)malloc(len);
    memcpy(msg, gib, len);
    dtls1_process_heartbeat(msg, cpyLen);
    return 0;
}