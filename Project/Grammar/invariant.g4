grammar invariant;

//////////////////////Expressions //////////////////////////

expr : expr '(' (expr (',' expr)*)? ')' 	#funAppExpr
     |expr '.' IDENTIFIER 			#accessExpr
     | '*' expr 				#deRefExpr
     | SUB NUMBER				#negNumber
     | '&' expr					#refExpr
     | expr EXP expr       #exponentiationExpr
     | expr op=(MUL | DIV) expr 		#multiplicativeExpr
     | expr op=(ADD | SUB) expr 		#additiveExpr
     | expr '[' expr ']'    #indexExpr
     | expr op=(GT | GTE | LT | LTE) expr 				#relationalExpr
     | expr op=(EQ | NE) expr 			#equalityExpr
     | expr BAND expr     #bandExpr
     | expr BXOR expr    #bxorExpr
     | expr BOR expr     #borExpr
     | expr LAND expr    #landExpr
     | expr LOR expr     #lorExpr
     | NOT expr             #notExpr
     | IDENTIFIER				#varExpr
     | NUMBER					#numExpr
     | '(' expr ')'				#parenExpr
;

//////////////////////Lexicon //////////////////////////

MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
GT  : '>' ;
LT : '<' ;
GTE : '<=' ;
LTE : '>=' ;
EQ  : '==' ;
NE  : '!=' ;
EXP : '**' ;
LAND : '&&' ;
LOR : '||' ;
BAND : '&' ;
BOR : '|' ;
BXOR : '^' ;
NOT : '!' ;

NUMBER : [0-9]+ ;

IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]* ;

// Ignore whitespace
WS : [ \t\n\r]+ -> skip ;