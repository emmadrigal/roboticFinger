# Generated from interpreter.g4 by ANTLR 4.5.1
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\13")
        buf.write("d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\6\2")
        buf.write("\34\n\2\r\2\16\2\35\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3\66\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\t\6\tH\n\t\r\t\16\tI\3\t\3\t\3\n")
        buf.write("\6\nO\n\n\r\n\16\nP\3\n\3\n\3\13\6\13V\n\13\r\13\16\13")
        buf.write("W\3\f\6\f[\n\f\r\f\16\f\\\3\r\6\r`\n\r\r\r\16\ra\3\r\2")
        buf.write("\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2\2`\2\33\3\2\2\2")
        buf.write("\4\65\3\2\2\2\6\67\3\2\2\2\b:\3\2\2\2\n=\3\2\2\2\f@\3")
        buf.write("\2\2\2\16C\3\2\2\2\20G\3\2\2\2\22N\3\2\2\2\24U\3\2\2\2")
        buf.write("\26Z\3\2\2\2\30_\3\2\2\2\32\34\5\4\3\2\33\32\3\2\2\2\34")
        buf.write("\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\37\3\2\2\2")
        buf.write("\37 \7\2\2\3 \3\3\2\2\2!\"\5\6\4\2\"#\5\20\t\2#$\5\22")
        buf.write("\n\2$%\5\26\f\2%&\7\n\2\2&\66\3\2\2\2\'(\5\b\5\2()\5\30")
        buf.write("\r\2)*\7\n\2\2*\66\3\2\2\2+,\5\n\6\2,-\5\20\t\2-.\5\24")
        buf.write("\13\2./\7\n\2\2/\66\3\2\2\2\60\61\5\f\7\2\61\62\5\16\b")
        buf.write("\2\62\63\5\24\13\2\63\64\7\n\2\2\64\66\3\2\2\2\65!\3\2")
        buf.write("\2\2\65\'\3\2\2\2\65+\3\2\2\2\65\60\3\2\2\2\66\5\3\2\2")
        buf.write("\2\678\7\b\2\289\7\t\2\29\7\3\2\2\2:;\7\7\2\2;<\7\t\2")
        buf.write("\2<\t\3\2\2\2=>\7\5\2\2>?\7\t\2\2?\13\3\2\2\2@A\7\6\2")
        buf.write("\2AB\7\t\2\2B\r\3\2\2\2CD\7\13\2\2DE\7\t\2\2E\17\3\2\2")
        buf.write("\2FH\7\3\2\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2\2J")
        buf.write("K\3\2\2\2KL\7\t\2\2L\21\3\2\2\2MO\7\3\2\2NM\3\2\2\2OP")
        buf.write("\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RS\7\t\2\2S\23\3")
        buf.write("\2\2\2TV\7\3\2\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2")
        buf.write("\2X\25\3\2\2\2Y[\7\3\2\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2")
        buf.write("\2\\]\3\2\2\2]\27\3\2\2\2^`\7\3\2\2_^\3\2\2\2`a\3\2\2")
        buf.write("\2a_\3\2\2\2ab\3\2\2\2b\31\3\2\2\2\t\35\65IPW\\a")
        return buf.getvalue()


class interpreterParser ( Parser ):

    grammarFileName = "interpreter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "INT_NUMBER", "DIGIT", "TOUCHXY", "TOUCHN", 
                      "PUSH", "DRAG", "WHITESPACE", "NEWLINE", "ABC" ]

    RULE_interpreter = 0
    RULE_line = 1
    RULE_drag_command = 2
    RULE_push_cmd = 3
    RULE_touch_cmdxy = 4
    RULE_touch_cmdn = 5
    RULE_letter = 6
    RULE_positionX = 7
    RULE_positionY = 8
    RULE_positionYt = 9
    RULE_repetitions = 10
    RULE_time = 11

    ruleNames =  [ "interpreter", "line", "drag_command", "push_cmd", "touch_cmdxy", 
                   "touch_cmdn", "letter", "positionX", "positionY", "positionYt", 
                   "repetitions", "time" ]

    EOF = Token.EOF
    INT_NUMBER=1
    DIGIT=2
    TOUCHXY=3
    TOUCHN=4
    PUSH=5
    DRAG=6
    WHITESPACE=7
    NEWLINE=8
    ABC=9

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class InterpreterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(interpreterParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(interpreterParser.LineContext)
            else:
                return self.getTypedRuleContext(interpreterParser.LineContext,i)


        def getRuleIndex(self):
            return interpreterParser.RULE_interpreter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterpreter" ):
                listener.enterInterpreter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterpreter" ):
                listener.exitInterpreter(self)




    def interpreter(self):

        localctx = interpreterParser.InterpreterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_interpreter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.line()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << interpreterParser.TOUCHXY) | (1 << interpreterParser.TOUCHN) | (1 << interpreterParser.PUSH) | (1 << interpreterParser.DRAG))) != 0)):
                    break

            self.state = 29
            self.match(interpreterParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def drag_command(self):
            return self.getTypedRuleContext(interpreterParser.Drag_commandContext,0)


        def positionX(self):
            return self.getTypedRuleContext(interpreterParser.PositionXContext,0)


        def positionY(self):
            return self.getTypedRuleContext(interpreterParser.PositionYContext,0)


        def repetitions(self):
            return self.getTypedRuleContext(interpreterParser.RepetitionsContext,0)


        def NEWLINE(self):
            return self.getToken(interpreterParser.NEWLINE, 0)

        def push_cmd(self):
            return self.getTypedRuleContext(interpreterParser.Push_cmdContext,0)


        def time(self):
            return self.getTypedRuleContext(interpreterParser.TimeContext,0)


        def touch_cmdxy(self):
            return self.getTypedRuleContext(interpreterParser.Touch_cmdxyContext,0)


        def positionYt(self):
            return self.getTypedRuleContext(interpreterParser.PositionYtContext,0)


        def touch_cmdn(self):
            return self.getTypedRuleContext(interpreterParser.Touch_cmdnContext,0)


        def letter(self):
            return self.getTypedRuleContext(interpreterParser.LetterContext,0)


        def getRuleIndex(self):
            return interpreterParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = interpreterParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 51
            token = self._input.LA(1)
            if token in [interpreterParser.DRAG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.drag_command()
                self.state = 32
                self.positionX()
                self.state = 33
                self.positionY()
                self.state = 34
                self.repetitions()
                self.state = 35
                self.match(interpreterParser.NEWLINE)

            elif token in [interpreterParser.PUSH]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.push_cmd()
                self.state = 38
                self.time()
                self.state = 39
                self.match(interpreterParser.NEWLINE)

            elif token in [interpreterParser.TOUCHXY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.touch_cmdxy()
                self.state = 42
                self.positionX()
                self.state = 43
                self.positionYt()
                self.state = 44
                self.match(interpreterParser.NEWLINE)

            elif token in [interpreterParser.TOUCHN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.touch_cmdn()
                self.state = 47
                self.letter()
                self.state = 48
                self.positionYt()
                self.state = 49
                self.match(interpreterParser.NEWLINE)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Drag_commandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DRAG(self):
            return self.getToken(interpreterParser.DRAG, 0)

        def WHITESPACE(self):
            return self.getToken(interpreterParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return interpreterParser.RULE_drag_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrag_command" ):
                listener.enterDrag_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrag_command" ):
                listener.exitDrag_command(self)




    def drag_command(self):

        localctx = interpreterParser.Drag_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_drag_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(interpreterParser.DRAG)
            self.state = 54
            self.match(interpreterParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Push_cmdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUSH(self):
            return self.getToken(interpreterParser.PUSH, 0)

        def WHITESPACE(self):
            return self.getToken(interpreterParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return interpreterParser.RULE_push_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPush_cmd" ):
                listener.enterPush_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPush_cmd" ):
                listener.exitPush_cmd(self)




    def push_cmd(self):

        localctx = interpreterParser.Push_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_push_cmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(interpreterParser.PUSH)
            self.state = 57
            self.match(interpreterParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Touch_cmdxyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOUCHXY(self):
            return self.getToken(interpreterParser.TOUCHXY, 0)

        def WHITESPACE(self):
            return self.getToken(interpreterParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return interpreterParser.RULE_touch_cmdxy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTouch_cmdxy" ):
                listener.enterTouch_cmdxy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTouch_cmdxy" ):
                listener.exitTouch_cmdxy(self)




    def touch_cmdxy(self):

        localctx = interpreterParser.Touch_cmdxyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_touch_cmdxy)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(interpreterParser.TOUCHXY)
            self.state = 60
            self.match(interpreterParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Touch_cmdnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOUCHN(self):
            return self.getToken(interpreterParser.TOUCHN, 0)

        def WHITESPACE(self):
            return self.getToken(interpreterParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return interpreterParser.RULE_touch_cmdn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTouch_cmdn" ):
                listener.enterTouch_cmdn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTouch_cmdn" ):
                listener.exitTouch_cmdn(self)




    def touch_cmdn(self):

        localctx = interpreterParser.Touch_cmdnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_touch_cmdn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(interpreterParser.TOUCHN)
            self.state = 63
            self.match(interpreterParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LetterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABC(self):
            return self.getToken(interpreterParser.ABC, 0)

        def WHITESPACE(self):
            return self.getToken(interpreterParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return interpreterParser.RULE_letter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetter" ):
                listener.enterLetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetter" ):
                listener.exitLetter(self)




    def letter(self):

        localctx = interpreterParser.LetterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_letter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(interpreterParser.ABC)
            self.state = 66
            self.match(interpreterParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PositionXContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHITESPACE(self):
            return self.getToken(interpreterParser.WHITESPACE, 0)

        def INT_NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(interpreterParser.INT_NUMBER)
            else:
                return self.getToken(interpreterParser.INT_NUMBER, i)

        def getRuleIndex(self):
            return interpreterParser.RULE_positionX

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionX" ):
                listener.enterPositionX(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionX" ):
                listener.exitPositionX(self)




    def positionX(self):

        localctx = interpreterParser.PositionXContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_positionX)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.match(interpreterParser.INT_NUMBER)
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==interpreterParser.INT_NUMBER):
                    break

            self.state = 73
            self.match(interpreterParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PositionYContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHITESPACE(self):
            return self.getToken(interpreterParser.WHITESPACE, 0)

        def INT_NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(interpreterParser.INT_NUMBER)
            else:
                return self.getToken(interpreterParser.INT_NUMBER, i)

        def getRuleIndex(self):
            return interpreterParser.RULE_positionY

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionY" ):
                listener.enterPositionY(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionY" ):
                listener.exitPositionY(self)




    def positionY(self):

        localctx = interpreterParser.PositionYContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_positionY)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 75
                self.match(interpreterParser.INT_NUMBER)
                self.state = 78 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==interpreterParser.INT_NUMBER):
                    break

            self.state = 80
            self.match(interpreterParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PositionYtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(interpreterParser.INT_NUMBER)
            else:
                return self.getToken(interpreterParser.INT_NUMBER, i)

        def getRuleIndex(self):
            return interpreterParser.RULE_positionYt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionYt" ):
                listener.enterPositionYt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionYt" ):
                listener.exitPositionYt(self)




    def positionYt(self):

        localctx = interpreterParser.PositionYtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_positionYt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 82
                self.match(interpreterParser.INT_NUMBER)
                self.state = 85 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==interpreterParser.INT_NUMBER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RepetitionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(interpreterParser.INT_NUMBER)
            else:
                return self.getToken(interpreterParser.INT_NUMBER, i)

        def getRuleIndex(self):
            return interpreterParser.RULE_repetitions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetitions" ):
                listener.enterRepetitions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetitions" ):
                listener.exitRepetitions(self)




    def repetitions(self):

        localctx = interpreterParser.RepetitionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_repetitions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 87
                self.match(interpreterParser.INT_NUMBER)
                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==interpreterParser.INT_NUMBER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TimeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(interpreterParser.INT_NUMBER)
            else:
                return self.getToken(interpreterParser.INT_NUMBER, i)

        def getRuleIndex(self):
            return interpreterParser.RULE_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime" ):
                listener.enterTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime" ):
                listener.exitTime(self)




    def time(self):

        localctx = interpreterParser.TimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_time)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 92
                self.match(interpreterParser.INT_NUMBER)
                self.state = 95 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==interpreterParser.INT_NUMBER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





