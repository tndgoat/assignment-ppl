// MSSV: 2115232

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// --------------------- Begin ---------------------

program: NEWLINE* list_declared EOF;

list_declared: declared list_declared | declared;
declared: function | variables ignore;

// variable
variables: implicit_var | keyword_var | implicit_dynamic;
implicit_var: VAR ID ASSIGN expression;
keyword_var: prim_type (ID | array_declared) (ASSIGN expression)?;
implicit_dynamic: DYNAMIC ID (ASSIGN expression)?;
prim_type: BOOL | NUMBER | STRING;

// array
array_declared: ID (LS_BRACKET list_NUMBER_LIT RS_BRACKET);
list_NUMBER_LIT: NUMBER_LIT (COMMA list_NUMBER_LIT) | NUMBER_LIT;

// expression
expression_list: expression COMMA expression_list | expression;
expression: expression1 CONCAT_STR expression1 | expression1;
expression1: expression2 (EQUAL | COMPARE_STR | NOT_EQUAL | LT | GT | LE | GE) expression2 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: NOT expression5 | expression6;
expression6: (SUB | ADD) expression6 | expression7;
expression7: array_element | literal | ID | (LR_BRACKET expression RR_BRACKET) | func_call;

// function
function: FUNC ID LR_BRACKET prameters_list? RR_BRACKET (ignore? return_statement | ignore? block_statement | ignore);
prameters_list: prim_type (ID | array_declared) COMMA prameters_list | prim_type (ID | array_declared);

// statement
statement_list: statement statement_list | ;
statement: declaration_statement | assignment_statement 
            | if_statement | for_statement 
            | break_statement | continue_statement 
            | return_statement  | call_statement | block_statement;

// variable declaration - assignment
declaration_statement: variables ignore;
assignment_statement: (ID | ID index_operators) ASSIGN expression ignore;

// if - else - elif
if_statement: IF LR_BRACKET expression RR_BRACKET ignore? statement elif_statement_list (ELSE ignore? statement)?;
elif_statement_list: ELIF LR_BRACKET expression RR_BRACKET ignore? statement elif_statement_list | ;

// for - break - continue - return
for_statement: FOR ID UNTIL expression BY expression (ignore? statement);
break_statement: BREAK ignore;
continue_statement: CONTINUE ignore;
return_statement: RETURN (expression | ) ignore;

// function call
call_statement: func_call ignore;
func_call: ID (LR_BRACKET expression_list? RR_BRACKET);

// block
block_statement: BEGIN ignore statement_list END ignore;

// value
literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal;
array_literal: LS_BRACKET expression_list RS_BRACKET;
array_element: (ID | func_call) index_operators;
index_operators: (LS_BRACKET expression_list RS_BRACKET);

// ignore
ignore: NEWLINE+;



// ---------- Begin of Lexical structure ----------

// Keywords
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';

FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';

IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';

// Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

EQUAL: '=';
ASSIGN: '<-';
NOT_EQUAL: '!=';

LT: '<';
LE: '<=';
GT: '>';
GE: '>=';

CONCAT_STR: '...';
COMPARE_STR: '==';

// Separators
LR_BRACKET: '(';        // left round bracket
RR_BRACKET: ')';        // right round bracket
LS_BRACKET: '[';        // left square bracket
RS_BRACKET: ']';        // left square bracket
COMMA: ',';

// Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Literals
// Number
NUMBER_LIT: DIGIT+ (DECIMAL | DECIMAL? EXPONENT?);
fragment DIGIT: [0-9];
fragment SIGN: [+-];
fragment EXPONENT: [eE] SIGN? DIGIT+;
fragment DECIMAL: '.' DIGIT*;

// Boolean
BOOL_LIT: TRUE | FALSE;

// String
STRING_LIT: '"'(VALID_SEQUENCE | VALID_ESCAPE)* '"'{self.text = self.text[1:-1];};
fragment VALID_ESCAPE: '\\' [bfrnt'\\] | '\'"';
fragment VALID_SEQUENCE: ~[\r\n\f\\"];

// Anothers
NEWLINE: [\n];  // newlines
COMMENTS: '##' ~[\n\r\f]* -> skip;  // comments
WS : [ \f\b\t\r]+ -> skip ; // skip spaces, tabs

// Errors
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (VALID_SEQUENCE | VALID_ESCAPE)* ('\r\n' | '\n' | EOF) { 
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' (VALID_SEQUENCE | VALID_ESCAPE)* INVALID_ESCAPE {raise IllegalEscape(self.text[1:])};
fragment INVALID_ESCAPE: [\r\f] | '\\' ~[bfrnt'\\];

// ---------- End of Lexical structure ----------

// --------------------- End ---------------------