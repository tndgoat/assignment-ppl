# Generated from c://Users//Tung Nguyen//OneDrive//Máy tính//HK232//PPL//assignment//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,369,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,5,0,80,
        8,0,10,0,12,0,83,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,92,8,1,1,2,
        1,2,1,2,1,2,3,2,98,8,2,1,3,1,3,1,3,3,3,103,8,3,1,4,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,3,5,113,8,5,1,5,1,5,3,5,117,8,5,1,6,1,6,1,6,1,6,3,
        6,123,8,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,136,8,
        9,1,10,1,10,1,10,1,10,1,10,3,10,143,8,10,1,11,1,11,1,11,1,11,1,11,
        3,11,150,8,11,1,12,1,12,1,12,1,12,1,12,3,12,157,8,12,1,13,1,13,1,
        13,1,13,1,13,1,13,5,13,165,8,13,10,13,12,13,168,9,13,1,14,1,14,1,
        14,1,14,1,14,1,14,5,14,176,8,14,10,14,12,14,179,9,14,1,15,1,15,1,
        15,1,15,1,15,1,15,5,15,187,8,15,10,15,12,15,190,9,15,1,16,1,16,1,
        16,3,16,195,8,16,1,17,1,17,1,17,3,17,200,8,17,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,3,18,210,8,18,1,19,1,19,1,19,1,19,3,19,216,8,
        19,1,19,1,19,3,19,220,8,19,1,19,1,19,3,19,224,8,19,1,19,1,19,3,19,
        228,8,19,1,20,1,20,1,20,3,20,233,8,20,1,20,1,20,1,20,1,20,1,20,1,
        20,3,20,241,8,20,3,20,243,8,20,1,21,1,21,1,21,1,21,3,21,249,8,21,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,260,8,22,1,23,
        1,23,1,23,1,24,1,24,1,24,3,24,268,8,24,1,24,1,24,1,24,1,24,1,25,
        1,25,1,25,1,25,1,25,3,25,279,8,25,1,25,1,25,1,25,1,25,3,25,285,8,
        25,1,25,3,25,288,8,25,1,26,1,26,1,26,1,26,1,26,3,26,295,8,26,1,26,
        1,26,1,26,1,26,3,26,301,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        3,27,310,8,27,1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,29,1,30,1,30,
        1,30,3,30,323,8,30,1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,32,3,32,
        333,8,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,
        1,34,1,34,3,34,348,8,34,1,35,1,35,1,35,1,35,1,36,1,36,3,36,356,8,
        36,1,36,1,36,1,37,1,37,1,37,1,37,1,38,4,38,365,8,38,11,38,12,38,
        366,1,38,0,3,26,28,30,39,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        74,76,0,5,1,0,3,5,3,0,28,28,30,34,36,36,1,0,21,22,1,0,23,24,1,0,
        25,27,382,0,81,1,0,0,0,2,91,1,0,0,0,4,97,1,0,0,0,6,102,1,0,0,0,8,
        104,1,0,0,0,10,109,1,0,0,0,12,118,1,0,0,0,14,124,1,0,0,0,16,126,
        1,0,0,0,18,135,1,0,0,0,20,142,1,0,0,0,22,149,1,0,0,0,24,156,1,0,
        0,0,26,158,1,0,0,0,28,169,1,0,0,0,30,180,1,0,0,0,32,194,1,0,0,0,
        34,199,1,0,0,0,36,209,1,0,0,0,38,211,1,0,0,0,40,242,1,0,0,0,42,248,
        1,0,0,0,44,259,1,0,0,0,46,261,1,0,0,0,48,267,1,0,0,0,50,273,1,0,
        0,0,52,300,1,0,0,0,54,302,1,0,0,0,56,313,1,0,0,0,58,316,1,0,0,0,
        60,319,1,0,0,0,62,326,1,0,0,0,64,329,1,0,0,0,66,336,1,0,0,0,68,347,
        1,0,0,0,70,349,1,0,0,0,72,355,1,0,0,0,74,359,1,0,0,0,76,364,1,0,
        0,0,78,80,5,46,0,0,79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,
        82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,3,2,1,0,85,86,5,0,0,
        1,86,1,1,0,0,0,87,88,3,4,2,0,88,89,3,2,1,0,89,92,1,0,0,0,90,92,3,
        4,2,0,91,87,1,0,0,0,91,90,1,0,0,0,92,3,1,0,0,0,93,98,3,38,19,0,94,
        95,3,6,3,0,95,96,3,76,38,0,96,98,1,0,0,0,97,93,1,0,0,0,97,94,1,0,
        0,0,98,5,1,0,0,0,99,103,3,8,4,0,100,103,3,10,5,0,101,103,3,12,6,
        0,102,99,1,0,0,0,102,100,1,0,0,0,102,101,1,0,0,0,103,7,1,0,0,0,104,
        105,5,7,0,0,105,106,5,42,0,0,106,107,5,29,0,0,107,108,3,22,11,0,
        108,9,1,0,0,0,109,112,3,14,7,0,110,113,5,42,0,0,111,113,3,16,8,0,
        112,110,1,0,0,0,112,111,1,0,0,0,113,116,1,0,0,0,114,115,5,29,0,0,
        115,117,3,22,11,0,116,114,1,0,0,0,116,117,1,0,0,0,117,11,1,0,0,0,
        118,119,5,8,0,0,119,122,5,42,0,0,120,121,5,29,0,0,121,123,3,22,11,
        0,122,120,1,0,0,0,122,123,1,0,0,0,123,13,1,0,0,0,124,125,7,0,0,0,
        125,15,1,0,0,0,126,127,5,42,0,0,127,128,5,39,0,0,128,129,3,18,9,
        0,129,130,5,40,0,0,130,17,1,0,0,0,131,132,5,43,0,0,132,133,5,41,
        0,0,133,136,3,18,9,0,134,136,5,43,0,0,135,131,1,0,0,0,135,134,1,
        0,0,0,136,19,1,0,0,0,137,138,3,22,11,0,138,139,5,41,0,0,139,140,
        3,20,10,0,140,143,1,0,0,0,141,143,3,22,11,0,142,137,1,0,0,0,142,
        141,1,0,0,0,143,21,1,0,0,0,144,145,3,24,12,0,145,146,5,35,0,0,146,
        147,3,24,12,0,147,150,1,0,0,0,148,150,3,24,12,0,149,144,1,0,0,0,
        149,148,1,0,0,0,150,23,1,0,0,0,151,152,3,26,13,0,152,153,7,1,0,0,
        153,154,3,26,13,0,154,157,1,0,0,0,155,157,3,26,13,0,156,151,1,0,
        0,0,156,155,1,0,0,0,157,25,1,0,0,0,158,159,6,13,-1,0,159,160,3,28,
        14,0,160,166,1,0,0,0,161,162,10,2,0,0,162,163,7,2,0,0,163,165,3,
        28,14,0,164,161,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,
        1,0,0,0,167,27,1,0,0,0,168,166,1,0,0,0,169,170,6,14,-1,0,170,171,
        3,30,15,0,171,177,1,0,0,0,172,173,10,2,0,0,173,174,7,3,0,0,174,176,
        3,30,15,0,175,172,1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,177,178,
        1,0,0,0,178,29,1,0,0,0,179,177,1,0,0,0,180,181,6,15,-1,0,181,182,
        3,32,16,0,182,188,1,0,0,0,183,184,10,2,0,0,184,185,7,4,0,0,185,187,
        3,32,16,0,186,183,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,189,
        1,0,0,0,189,31,1,0,0,0,190,188,1,0,0,0,191,192,5,20,0,0,192,195,
        3,32,16,0,193,195,3,34,17,0,194,191,1,0,0,0,194,193,1,0,0,0,195,
        33,1,0,0,0,196,197,7,3,0,0,197,200,3,34,17,0,198,200,3,36,18,0,199,
        196,1,0,0,0,199,198,1,0,0,0,200,35,1,0,0,0,201,210,3,72,36,0,202,
        210,3,68,34,0,203,210,5,42,0,0,204,205,5,37,0,0,205,206,3,22,11,
        0,206,207,5,38,0,0,207,210,1,0,0,0,208,210,3,64,32,0,209,201,1,0,
        0,0,209,202,1,0,0,0,209,203,1,0,0,0,209,204,1,0,0,0,209,208,1,0,
        0,0,210,37,1,0,0,0,211,212,5,9,0,0,212,213,5,42,0,0,213,215,5,37,
        0,0,214,216,3,40,20,0,215,214,1,0,0,0,215,216,1,0,0,0,216,217,1,
        0,0,0,217,227,5,38,0,0,218,220,3,76,38,0,219,218,1,0,0,0,219,220,
        1,0,0,0,220,221,1,0,0,0,221,228,3,60,30,0,222,224,3,76,38,0,223,
        222,1,0,0,0,223,224,1,0,0,0,224,225,1,0,0,0,225,228,3,66,33,0,226,
        228,3,76,38,0,227,219,1,0,0,0,227,223,1,0,0,0,227,226,1,0,0,0,228,
        39,1,0,0,0,229,232,3,14,7,0,230,233,5,42,0,0,231,233,3,16,8,0,232,
        230,1,0,0,0,232,231,1,0,0,0,233,234,1,0,0,0,234,235,5,41,0,0,235,
        236,3,40,20,0,236,243,1,0,0,0,237,240,3,14,7,0,238,241,5,42,0,0,
        239,241,3,16,8,0,240,238,1,0,0,0,240,239,1,0,0,0,241,243,1,0,0,0,
        242,229,1,0,0,0,242,237,1,0,0,0,243,41,1,0,0,0,244,245,3,44,22,0,
        245,246,3,42,21,0,246,249,1,0,0,0,247,249,1,0,0,0,248,244,1,0,0,
        0,248,247,1,0,0,0,249,43,1,0,0,0,250,260,3,46,23,0,251,260,3,48,
        24,0,252,260,3,50,25,0,253,260,3,54,27,0,254,260,3,56,28,0,255,260,
        3,58,29,0,256,260,3,60,30,0,257,260,3,62,31,0,258,260,3,66,33,0,
        259,250,1,0,0,0,259,251,1,0,0,0,259,252,1,0,0,0,259,253,1,0,0,0,
        259,254,1,0,0,0,259,255,1,0,0,0,259,256,1,0,0,0,259,257,1,0,0,0,
        259,258,1,0,0,0,260,45,1,0,0,0,261,262,3,6,3,0,262,263,3,76,38,0,
        263,47,1,0,0,0,264,268,5,42,0,0,265,266,5,42,0,0,266,268,3,74,37,
        0,267,264,1,0,0,0,267,265,1,0,0,0,268,269,1,0,0,0,269,270,5,29,0,
        0,270,271,3,22,11,0,271,272,3,76,38,0,272,49,1,0,0,0,273,274,5,15,
        0,0,274,275,5,37,0,0,275,276,3,22,11,0,276,278,5,38,0,0,277,279,
        3,76,38,0,278,277,1,0,0,0,278,279,1,0,0,0,279,280,1,0,0,0,280,281,
        3,44,22,0,281,287,3,52,26,0,282,284,5,16,0,0,283,285,3,76,38,0,284,
        283,1,0,0,0,284,285,1,0,0,0,285,286,1,0,0,0,286,288,3,44,22,0,287,
        282,1,0,0,0,287,288,1,0,0,0,288,51,1,0,0,0,289,290,5,17,0,0,290,
        291,5,37,0,0,291,292,3,22,11,0,292,294,5,38,0,0,293,295,3,76,38,
        0,294,293,1,0,0,0,294,295,1,0,0,0,295,296,1,0,0,0,296,297,3,44,22,
        0,297,298,3,52,26,0,298,301,1,0,0,0,299,301,1,0,0,0,300,289,1,0,
        0,0,300,299,1,0,0,0,301,53,1,0,0,0,302,303,5,10,0,0,303,304,5,42,
        0,0,304,305,5,11,0,0,305,306,3,22,11,0,306,307,5,12,0,0,307,309,
        3,22,11,0,308,310,3,76,38,0,309,308,1,0,0,0,309,310,1,0,0,0,310,
        311,1,0,0,0,311,312,3,44,22,0,312,55,1,0,0,0,313,314,5,13,0,0,314,
        315,3,76,38,0,315,57,1,0,0,0,316,317,5,14,0,0,317,318,3,76,38,0,
        318,59,1,0,0,0,319,322,5,6,0,0,320,323,3,22,11,0,321,323,1,0,0,0,
        322,320,1,0,0,0,322,321,1,0,0,0,323,324,1,0,0,0,324,325,3,76,38,
        0,325,61,1,0,0,0,326,327,3,64,32,0,327,328,3,76,38,0,328,63,1,0,
        0,0,329,330,5,42,0,0,330,332,5,37,0,0,331,333,3,20,10,0,332,331,
        1,0,0,0,332,333,1,0,0,0,333,334,1,0,0,0,334,335,5,38,0,0,335,65,
        1,0,0,0,336,337,5,18,0,0,337,338,3,76,38,0,338,339,3,42,21,0,339,
        340,5,19,0,0,340,341,3,76,38,0,341,67,1,0,0,0,342,348,5,43,0,0,343,
        348,5,45,0,0,344,348,5,1,0,0,345,348,5,2,0,0,346,348,3,70,35,0,347,
        342,1,0,0,0,347,343,1,0,0,0,347,344,1,0,0,0,347,345,1,0,0,0,347,
        346,1,0,0,0,348,69,1,0,0,0,349,350,5,39,0,0,350,351,3,20,10,0,351,
        352,5,40,0,0,352,71,1,0,0,0,353,356,5,42,0,0,354,356,3,64,32,0,355,
        353,1,0,0,0,355,354,1,0,0,0,356,357,1,0,0,0,357,358,3,74,37,0,358,
        73,1,0,0,0,359,360,5,39,0,0,360,361,3,20,10,0,361,362,5,40,0,0,362,
        75,1,0,0,0,363,365,5,46,0,0,364,363,1,0,0,0,365,366,1,0,0,0,366,
        364,1,0,0,0,366,367,1,0,0,0,367,77,1,0,0,0,38,81,91,97,102,112,116,
        122,135,142,149,156,166,177,188,194,199,209,215,219,223,227,232,
        240,242,248,259,267,278,284,287,294,300,309,322,332,347,355,366
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LE", 
                      "GT", "GE", "CONCAT_STR", "COMPARE_STR", "LR_BRACKET", 
                      "RR_BRACKET", "LS_BRACKET", "RS_BRACKET", "COMMA", 
                      "ID", "NUMBER_LIT", "BOOL_LIT", "STRING_LIT", "NEWLINE", 
                      "COMMENTS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_declared = 1
    RULE_declared = 2
    RULE_variables = 3
    RULE_implicit_var = 4
    RULE_keyword_var = 5
    RULE_implicit_dynamic = 6
    RULE_prim_type = 7
    RULE_array_declared = 8
    RULE_list_NUMBER_LIT = 9
    RULE_expression_list = 10
    RULE_expression = 11
    RULE_expression1 = 12
    RULE_expression2 = 13
    RULE_expression3 = 14
    RULE_expression4 = 15
    RULE_expression5 = 16
    RULE_expression6 = 17
    RULE_expression7 = 18
    RULE_function = 19
    RULE_prameters_list = 20
    RULE_statement_list = 21
    RULE_statement = 22
    RULE_declaration_statement = 23
    RULE_assignment_statement = 24
    RULE_if_statement = 25
    RULE_elif_statement_list = 26
    RULE_for_statement = 27
    RULE_break_statement = 28
    RULE_continue_statement = 29
    RULE_return_statement = 30
    RULE_call_statement = 31
    RULE_func_call = 32
    RULE_block_statement = 33
    RULE_literal = 34
    RULE_array_literal = 35
    RULE_array_element = 36
    RULE_index_operators = 37
    RULE_ignore = 38

    ruleNames =  [ "program", "list_declared", "declared", "variables", 
                   "implicit_var", "keyword_var", "implicit_dynamic", "prim_type", 
                   "array_declared", "list_NUMBER_LIT", "expression_list", 
                   "expression", "expression1", "expression2", "expression3", 
                   "expression4", "expression5", "expression6", "expression7", 
                   "function", "prameters_list", "statement_list", "statement", 
                   "declaration_statement", "assignment_statement", "if_statement", 
                   "elif_statement_list", "for_statement", "break_statement", 
                   "continue_statement", "return_statement", "call_statement", 
                   "func_call", "block_statement", "literal", "array_literal", 
                   "array_element", "index_operators", "ignore" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    NOT=20
    AND=21
    OR=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    MOD=27
    EQUAL=28
    ASSIGN=29
    NOT_EQUAL=30
    LT=31
    LE=32
    GT=33
    GE=34
    CONCAT_STR=35
    COMPARE_STR=36
    LR_BRACKET=37
    RR_BRACKET=38
    LS_BRACKET=39
    RS_BRACKET=40
    COMMA=41
    ID=42
    NUMBER_LIT=43
    BOOL_LIT=44
    STRING_LIT=45
    NEWLINE=46
    COMMENTS=47
    WS=48
    ERROR_CHAR=49
    UNCLOSE_STRING=50
    ILLEGAL_ESCAPE=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 78
                self.match(ZCodeParser.NEWLINE)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.list_declared()
            self.state = 85
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(ZCodeParser.DeclaredContext,0)


        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_declared




    def list_declared(self):

        localctx = ZCodeParser.List_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_declared)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.declared()
                self.state = 88
                self.list_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionContext,0)


        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declared




    def declared(self):

        localctx = ZCodeParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declared)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.function()
                pass
            elif token in [3, 4, 5, 7, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.variables()
                self.state = 95
                self.ignore()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicit_var(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_varContext,0)


        def keyword_var(self):
            return self.getTypedRuleContext(ZCodeParser.Keyword_varContext,0)


        def implicit_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamicContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variables




    def variables(self):

        localctx = ZCodeParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variables)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.implicit_var()
                pass
            elif token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.keyword_var()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.implicit_dynamic()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_var




    def implicit_var(self):

        localctx = ZCodeParser.Implicit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_implicit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(ZCodeParser.VAR)
            self.state = 105
            self.match(ZCodeParser.ID)
            self.state = 106
            self.match(ZCodeParser.ASSIGN)
            self.state = 107
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prim_type(self):
            return self.getTypedRuleContext(ZCodeParser.Prim_typeContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def array_declared(self):
            return self.getTypedRuleContext(ZCodeParser.Array_declaredContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_keyword_var




    def keyword_var(self):

        localctx = ZCodeParser.Keyword_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_keyword_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.prim_type()
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 110
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 111
                self.array_declared()
                pass


            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 114
                self.match(ZCodeParser.ASSIGN)
                self.state = 115
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_dynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_dynamic




    def implicit_dynamic(self):

        localctx = ZCodeParser.Implicit_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_implicit_dynamic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(ZCodeParser.DYNAMIC)
            self.state = 119
            self.match(ZCodeParser.ID)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 120
                self.match(ZCodeParser.ASSIGN)
                self.state = 121
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prim_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_prim_type




    def prim_type(self):

        localctx = ZCodeParser.Prim_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_prim_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LS_BRACKET(self):
            return self.getToken(ZCodeParser.LS_BRACKET, 0)

        def list_NUMBER_LIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBER_LITContext,0)


        def RS_BRACKET(self):
            return self.getToken(ZCodeParser.RS_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_declared




    def array_declared(self):

        localctx = ZCodeParser.Array_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(ZCodeParser.ID)

            self.state = 127
            self.match(ZCodeParser.LS_BRACKET)
            self.state = 128
            self.list_NUMBER_LIT()
            self.state = 129
            self.match(ZCodeParser.RS_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_NUMBER_LITContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_NUMBER_LIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBER_LITContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_NUMBER_LIT




    def list_NUMBER_LIT(self):

        localctx = ZCodeParser.List_NUMBER_LITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list_NUMBER_LIT)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(ZCodeParser.NUMBER_LIT)

                self.state = 132
                self.match(ZCodeParser.COMMA)
                self.state = 133
                self.list_NUMBER_LIT()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(ZCodeParser.NUMBER_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_list




    def expression_list(self):

        localctx = ZCodeParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression_list)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.expression()
                self.state = 138
                self.match(ZCodeParser.COMMA)
                self.state = 139
                self.expression_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression1Context,i)


        def CONCAT_STR(self):
            return self.getToken(ZCodeParser.CONCAT_STR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.expression1()
                self.state = 145
                self.match(ZCodeParser.CONCAT_STR)
                self.state = 146
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression2Context,i)


        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def COMPARE_STR(self):
            return self.getToken(ZCodeParser.COMPARE_STR, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LE(self):
            return self.getToken(ZCodeParser.LE, 0)

        def GE(self):
            return self.getToken(ZCodeParser.GE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression1




    def expression1(self):

        localctx = ZCodeParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.expression2(0)
                self.state = 152
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 102273908736) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 153
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(ZCodeParser.Expression2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression2



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 161
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 162
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 163
                    self.expression3(0) 
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression3



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 172
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 173
                    _la = self._input.LA(1)
                    if not(_la==23 or _la==24):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 174
                    self.expression4(0) 
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression4



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 183
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 184
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 185
                    self.expression5() 
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression5




    def expression5(self):

        localctx = ZCodeParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expression5)
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(ZCodeParser.NOT)
                self.state = 192
                self.expression5()
                pass
            elif token in [1, 2, 23, 24, 37, 39, 42, 43, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.expression6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def expression7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression6




    def expression6(self):

        localctx = ZCodeParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expression6)
        self._la = 0 # Token type
        try:
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 197
                self.expression6()
                pass
            elif token in [1, 2, 37, 39, 42, 43, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.expression7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element(self):
            return self.getTypedRuleContext(ZCodeParser.Array_elementContext,0)


        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LR_BRACKET(self):
            return self.getToken(ZCodeParser.LR_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RR_BRACKET(self):
            return self.getToken(ZCodeParser.RR_BRACKET, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression7




    def expression7(self):

        localctx = ZCodeParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression7)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.array_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.match(ZCodeParser.LR_BRACKET)
                self.state = 205
                self.expression()
                self.state = 206
                self.match(ZCodeParser.RR_BRACKET)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 208
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LR_BRACKET(self):
            return self.getToken(ZCodeParser.LR_BRACKET, 0)

        def RR_BRACKET(self):
            return self.getToken(ZCodeParser.RR_BRACKET, 0)

        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def prameters_list(self):
            return self.getTypedRuleContext(ZCodeParser.Prameters_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(ZCodeParser.FUNC)
            self.state = 212
            self.match(ZCodeParser.ID)
            self.state = 213
            self.match(ZCodeParser.LR_BRACKET)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 214
                self.prameters_list()


            self.state = 217
            self.match(ZCodeParser.RR_BRACKET)
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 218
                    self.ignore()


                self.state = 221
                self.return_statement()
                pass

            elif la_ == 2:
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 222
                    self.ignore()


                self.state = 225
                self.block_statement()
                pass

            elif la_ == 3:
                self.state = 226
                self.ignore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prameters_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prim_type(self):
            return self.getTypedRuleContext(ZCodeParser.Prim_typeContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def prameters_list(self):
            return self.getTypedRuleContext(ZCodeParser.Prameters_listContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def array_declared(self):
            return self.getTypedRuleContext(ZCodeParser.Array_declaredContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_prameters_list




    def prameters_list(self):

        localctx = ZCodeParser.Prameters_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_prameters_list)
        try:
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.prim_type()
                self.state = 232
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 230
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 231
                    self.array_declared()
                    pass


                self.state = 234
                self.match(ZCodeParser.COMMA)
                self.state = 235
                self.prameters_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.prim_type()
                self.state = 240
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 238
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 239
                    self.array_declared()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_list




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_statement_list)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6, 7, 8, 10, 13, 14, 15, 18, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.statement()
                self.state = 245
                self.statement_list()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_statementContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Call_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_statement)
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.declaration_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 253
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 254
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 255
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 256
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 257
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 258
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration_statement




    def declaration_statement(self):

        localctx = ZCodeParser.Declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_declaration_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.variables()
            self.state = 262
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 264
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 265
                self.match(ZCodeParser.ID)
                self.state = 266
                self.index_operators()
                pass


            self.state = 269
            self.match(ZCodeParser.ASSIGN)
            self.state = 270
            self.expression()
            self.state = 271
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LR_BRACKET(self):
            return self.getToken(ZCodeParser.LR_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RR_BRACKET(self):
            return self.getToken(ZCodeParser.RR_BRACKET, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def elif_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statement_listContext,0)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(ZCodeParser.IF)
            self.state = 274
            self.match(ZCodeParser.LR_BRACKET)
            self.state = 275
            self.expression()
            self.state = 276
            self.match(ZCodeParser.RR_BRACKET)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 277
                self.ignore()


            self.state = 280
            self.statement()
            self.state = 281
            self.elif_statement_list()
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 282
                self.match(ZCodeParser.ELSE)
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 283
                    self.ignore()


                self.state = 286
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LR_BRACKET(self):
            return self.getToken(ZCodeParser.LR_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RR_BRACKET(self):
            return self.getToken(ZCodeParser.RR_BRACKET, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def elif_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statement_listContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_statement_list




    def elif_statement_list(self):

        localctx = ZCodeParser.Elif_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_elif_statement_list)
        self._la = 0 # Token type
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.match(ZCodeParser.ELIF)
                self.state = 290
                self.match(ZCodeParser.LR_BRACKET)
                self.state = 291
                self.expression()
                self.state = 292
                self.match(ZCodeParser.RR_BRACKET)
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 293
                    self.ignore()


                self.state = 296
                self.statement()
                self.state = 297
                self.elif_statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(ZCodeParser.FOR)
            self.state = 303
            self.match(ZCodeParser.ID)
            self.state = 304
            self.match(ZCodeParser.UNTIL)
            self.state = 305
            self.expression()
            self.state = 306
            self.match(ZCodeParser.BY)
            self.state = 307
            self.expression()

            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 308
                self.ignore()


            self.state = 311
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(ZCodeParser.BREAK)
            self.state = 314
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(ZCodeParser.CONTINUE)
            self.state = 317
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(ZCodeParser.RETURN)
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 20, 23, 24, 37, 39, 42, 43, 45]:
                self.state = 320
                self.expression()
                pass
            elif token in [46]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 324
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_statement




    def call_statement(self):

        localctx = ZCodeParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.func_call()
            self.state = 327
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LR_BRACKET(self):
            return self.getToken(ZCodeParser.LR_BRACKET, 0)

        def RR_BRACKET(self):
            return self.getToken(ZCodeParser.RR_BRACKET, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(ZCodeParser.ID)

            self.state = 330
            self.match(ZCodeParser.LR_BRACKET)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 49065732603910) != 0):
                self.state = 331
                self.expression_list()


            self.state = 334
            self.match(ZCodeParser.RR_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(ZCodeParser.BEGIN)
            self.state = 337
            self.ignore()
            self.state = 338
            self.statement_list()
            self.state = 339
            self.match(ZCodeParser.END)
            self.state = 340
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_literal)
        try:
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.match(ZCodeParser.NUMBER_LIT)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 344
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 345
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 5)
                self.state = 346
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS_BRACKET(self):
            return self.getToken(ZCodeParser.LS_BRACKET, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def RS_BRACKET(self):
            return self.getToken(ZCodeParser.RS_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(ZCodeParser.LS_BRACKET)
            self.state = 350
            self.expression_list()
            self.state = 351
            self.match(ZCodeParser.RS_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_element




    def array_element(self):

        localctx = ZCodeParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_array_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 353
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 354
                self.func_call()
                pass


            self.state = 357
            self.index_operators()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS_BRACKET(self):
            return self.getToken(ZCodeParser.LS_BRACKET, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def RS_BRACKET(self):
            return self.getToken(ZCodeParser.RS_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_index_operators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(ZCodeParser.LS_BRACKET)
            self.state = 360
            self.expression_list()
            self.state = 361
            self.match(ZCodeParser.RS_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_ignore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 363
                self.match(ZCodeParser.NEWLINE)
                self.state = 366 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==46):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expression2_sempred
        self._predicates[14] = self.expression3_sempred
        self._predicates[15] = self.expression4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




