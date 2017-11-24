grammar interpreter;

/*
 * Parser Rules
 */

interpreter                : line+ EOF ;

line        : drag_command positionX positionY repetitions NEWLINE | push_cmd time NEWLINE | touch_cmdxy positionX positionYt NEWLINE | touch_cmdn letter positionYt NEWLINE;

drag_command              : DRAG WHITESPACE ;

push_cmd  : PUSH WHITESPACE ;

touch_cmdxy : TOUCHXY WHITESPACE  ;

touch_cmdn  : TOUCHN WHITESPACE   ;

letter  :   ABC WHITESPACE;

positionX        : INT_NUMBER+ WHITESPACE;

positionY         :   INT_NUMBER+ WHITESPACE;

positionYt        :  INT_NUMBER+;

repetitions       :   INT_NUMBER+;

time              : INT_NUMBER+;

INT_NUMBER    :   DIGIT+;


/*
 * Lexer Rules
 */

fragment A          : ('A') ;
fragment C          : ('C') ;
fragment D          : ('D') ;
fragment P          : ('P') ;
fragment G          : ('G') ;
fragment R          : ('R') ;
fragment S          : ('S') ;
fragment Y          : ('Y') ;
fragment H          : ('H') ;
fragment O          : ('O') ;
fragment U          : ('U') ;
fragment T          : ('T') ;
fragment X          : ('X') ;
fragment N          : ('N') ;
fragment B          : ('B') ;


DIGIT   :   [0-9];

TOUCHXY               : T O U C H X Y ;

TOUCHN               : T O U C H N ;

PUSH                : P U S H ;

DRAG       	    : D R A G ;

WHITESPACE          : (' ');

NEWLINE             : ('\r'? '\n' | '\r')+ ;

ABC                 : (A | B | C);

