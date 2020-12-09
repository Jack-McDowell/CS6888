grammar invariant;

//////////////////////Expressions //////////////////////////

expr : ('NEXT' | 'RETURN_VAL') '(' (expr)? ')' 	#funAppExpr
     |expr '.' IDENTIFIER 			#accessExpr
     | expr '[' expr ']'    			#indexExpr
     | '*' expr 				#deRefExpr
     | SUB NUMBER				#negNumber
     | '&' expr					#refExpr
     | expr EXP expr       			#exponentiationExpr
     | expr op=(MUL | DIV) expr 		#multiplicativeExpr
     | expr op=(ADD | SUB) expr 		#additiveExpr
     | expr op=(GT | GTE | LT | LTE) expr 	#relationalExpr
     | expr op=(EQ | NE) expr 			#equalityExpr
     | expr BAND expr     			#bandExpr
     | expr BXOR expr    			#bxorExpr
     | expr BOR expr     			#borExpr
     | BNOT expr                    #bnotExpr
     | expr LAND expr    			#landExpr
     | expr LOR expr     			#lorExpr
     | LNOT expr             			#notExpr
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
LNOT : '!' ;
BNOT : '~' ;

NUMBER : [0-9]+ ;

IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]* ;

// Ignore whitespace
WS : [ \t\n\r]+ -> skip ;
