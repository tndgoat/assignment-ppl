# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u018e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$")
        buf.write("\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+")
        buf.write("\7+\u011b\n+\f+\16+\u011e\13+\3,\6,\u0121\n,\r,\16,\u0122")
        buf.write("\3,\3,\5,\u0127\n,\3,\5,\u012a\n,\5,\u012c\n,\3-\3-\3")
        buf.write(".\3.\3/\3/\5/\u0134\n/\3/\6/\u0137\n/\r/\16/\u0138\3\60")
        buf.write("\3\60\7\60\u013d\n\60\f\60\16\60\u0140\13\60\3\61\3\61")
        buf.write("\5\61\u0144\n\61\3\62\3\62\3\62\7\62\u0149\n\62\f\62\16")
        buf.write("\62\u014c\13\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\5\63")
        buf.write("\u0155\n\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\66\7")
        buf.write("\66\u015f\n\66\f\66\16\66\u0162\13\66\3\66\3\66\3\67\6")
        buf.write("\67\u0167\n\67\r\67\16\67\u0168\3\67\3\67\38\38\38\39")
        buf.write("\39\39\79\u0173\n9\f9\169\u0176\139\39\39\39\59\u017b")
        buf.write("\n9\39\39\3:\3:\3:\7:\u0182\n:\f:\16:\u0185\13:\3:\3:")
        buf.write("\3:\3;\3;\3;\5;\u018d\n;\2\2<\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y\2[\2]\2_\2a.c")
        buf.write("/e\2g\2i\60k\61m\62o\63q\64s\65u\2\3\2\16\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\3\2\62;\4\2--//\4\2GGgg\t\2))^^ddhhpptt")
        buf.write("vv\6\2\f\f\16\17$$^^\3\2\f\f\4\2\f\f\16\17\5\2\n\13\16")
        buf.write("\17\"\"\3\3\f\f\3\2\16\17\2\u019a\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m")
        buf.write("\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\3w\3\2\2\2\5")
        buf.write("|\3\2\2\2\7\u0082\3\2\2\2\t\u0089\3\2\2\2\13\u008e\3\2")
        buf.write("\2\2\r\u0095\3\2\2\2\17\u009c\3\2\2\2\21\u00a0\3\2\2\2")
        buf.write("\23\u00a8\3\2\2\2\25\u00ad\3\2\2\2\27\u00b1\3\2\2\2\31")
        buf.write("\u00b7\3\2\2\2\33\u00ba\3\2\2\2\35\u00c0\3\2\2\2\37\u00c9")
        buf.write("\3\2\2\2!\u00cc\3\2\2\2#\u00d1\3\2\2\2%\u00d6\3\2\2\2")
        buf.write("\'\u00dc\3\2\2\2)\u00e0\3\2\2\2+\u00e4\3\2\2\2-\u00e8")
        buf.write("\3\2\2\2/\u00eb\3\2\2\2\61\u00ed\3\2\2\2\63\u00ef\3\2")
        buf.write("\2\2\65\u00f1\3\2\2\2\67\u00f3\3\2\2\29\u00f5\3\2\2\2")
        buf.write(";\u00f7\3\2\2\2=\u00fa\3\2\2\2?\u00fd\3\2\2\2A\u00ff\3")
        buf.write("\2\2\2C\u0102\3\2\2\2E\u0104\3\2\2\2G\u0107\3\2\2\2I\u010b")
        buf.write("\3\2\2\2K\u010e\3\2\2\2M\u0110\3\2\2\2O\u0112\3\2\2\2")
        buf.write("Q\u0114\3\2\2\2S\u0116\3\2\2\2U\u0118\3\2\2\2W\u0120\3")
        buf.write("\2\2\2Y\u012d\3\2\2\2[\u012f\3\2\2\2]\u0131\3\2\2\2_\u013a")
        buf.write("\3\2\2\2a\u0143\3\2\2\2c\u0145\3\2\2\2e\u0154\3\2\2\2")
        buf.write("g\u0156\3\2\2\2i\u0158\3\2\2\2k\u015a\3\2\2\2m\u0166\3")
        buf.write("\2\2\2o\u016c\3\2\2\2q\u016f\3\2\2\2s\u017e\3\2\2\2u\u018c")
        buf.write("\3\2\2\2wx\7v\2\2xy\7t\2\2yz\7w\2\2z{\7g\2\2{\4\3\2\2")
        buf.write("\2|}\7h\2\2}~\7c\2\2~\177\7n\2\2\177\u0080\7u\2\2\u0080")
        buf.write("\u0081\7g\2\2\u0081\6\3\2\2\2\u0082\u0083\7p\2\2\u0083")
        buf.write("\u0084\7w\2\2\u0084\u0085\7o\2\2\u0085\u0086\7d\2\2\u0086")
        buf.write("\u0087\7g\2\2\u0087\u0088\7t\2\2\u0088\b\3\2\2\2\u0089")
        buf.write("\u008a\7d\2\2\u008a\u008b\7q\2\2\u008b\u008c\7q\2\2\u008c")
        buf.write("\u008d\7n\2\2\u008d\n\3\2\2\2\u008e\u008f\7u\2\2\u008f")
        buf.write("\u0090\7v\2\2\u0090\u0091\7t\2\2\u0091\u0092\7k\2\2\u0092")
        buf.write("\u0093\7p\2\2\u0093\u0094\7i\2\2\u0094\f\3\2\2\2\u0095")
        buf.write("\u0096\7t\2\2\u0096\u0097\7g\2\2\u0097\u0098\7v\2\2\u0098")
        buf.write("\u0099\7w\2\2\u0099\u009a\7t\2\2\u009a\u009b\7p\2\2\u009b")
        buf.write("\16\3\2\2\2\u009c\u009d\7x\2\2\u009d\u009e\7c\2\2\u009e")
        buf.write("\u009f\7t\2\2\u009f\20\3\2\2\2\u00a0\u00a1\7f\2\2\u00a1")
        buf.write("\u00a2\7{\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4\7c\2\2\u00a4")
        buf.write("\u00a5\7o\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7e\2\2\u00a7")
        buf.write("\22\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa\7w\2\2\u00aa")
        buf.write("\u00ab\7p\2\2\u00ab\u00ac\7e\2\2\u00ac\24\3\2\2\2\u00ad")
        buf.write("\u00ae\7h\2\2\u00ae\u00af\7q\2\2\u00af\u00b0\7t\2\2\u00b0")
        buf.write("\26\3\2\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3\7p\2\2\u00b3")
        buf.write("\u00b4\7v\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6\7n\2\2\u00b6")
        buf.write("\30\3\2\2\2\u00b7\u00b8\7d\2\2\u00b8\u00b9\7{\2\2\u00b9")
        buf.write("\32\3\2\2\2\u00ba\u00bb\7d\2\2\u00bb\u00bc\7t\2\2\u00bc")
        buf.write("\u00bd\7g\2\2\u00bd\u00be\7c\2\2\u00be\u00bf\7m\2\2\u00bf")
        buf.write("\34\3\2\2\2\u00c0\u00c1\7e\2\2\u00c1\u00c2\7q\2\2\u00c2")
        buf.write("\u00c3\7p\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5\7k\2\2\u00c5")
        buf.write("\u00c6\7p\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8\7g\2\2\u00c8")
        buf.write("\36\3\2\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7h\2\2\u00cb")
        buf.write(" \3\2\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7n\2\2\u00ce")
        buf.write("\u00cf\7u\2\2\u00cf\u00d0\7g\2\2\u00d0\"\3\2\2\2\u00d1")
        buf.write("\u00d2\7g\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4\7k\2\2\u00d4")
        buf.write("\u00d5\7h\2\2\u00d5$\3\2\2\2\u00d6\u00d7\7d\2\2\u00d7")
        buf.write("\u00d8\7g\2\2\u00d8\u00d9\7i\2\2\u00d9\u00da\7k\2\2\u00da")
        buf.write("\u00db\7p\2\2\u00db&\3\2\2\2\u00dc\u00dd\7g\2\2\u00dd")
        buf.write("\u00de\7p\2\2\u00de\u00df\7f\2\2\u00df(\3\2\2\2\u00e0")
        buf.write("\u00e1\7p\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3\7v\2\2\u00e3")
        buf.write("*\3\2\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7p\2\2\u00e6")
        buf.write("\u00e7\7f\2\2\u00e7,\3\2\2\2\u00e8\u00e9\7q\2\2\u00e9")
        buf.write("\u00ea\7t\2\2\u00ea.\3\2\2\2\u00eb\u00ec\7-\2\2\u00ec")
        buf.write("\60\3\2\2\2\u00ed\u00ee\7/\2\2\u00ee\62\3\2\2\2\u00ef")
        buf.write("\u00f0\7,\2\2\u00f0\64\3\2\2\2\u00f1\u00f2\7\61\2\2\u00f2")
        buf.write("\66\3\2\2\2\u00f3\u00f4\7\'\2\2\u00f48\3\2\2\2\u00f5\u00f6")
        buf.write("\7?\2\2\u00f6:\3\2\2\2\u00f7\u00f8\7>\2\2\u00f8\u00f9")
        buf.write("\7/\2\2\u00f9<\3\2\2\2\u00fa\u00fb\7#\2\2\u00fb\u00fc")
        buf.write("\7?\2\2\u00fc>\3\2\2\2\u00fd\u00fe\7>\2\2\u00fe@\3\2\2")
        buf.write("\2\u00ff\u0100\7>\2\2\u0100\u0101\7?\2\2\u0101B\3\2\2")
        buf.write("\2\u0102\u0103\7@\2\2\u0103D\3\2\2\2\u0104\u0105\7@\2")
        buf.write("\2\u0105\u0106\7?\2\2\u0106F\3\2\2\2\u0107\u0108\7\60")
        buf.write("\2\2\u0108\u0109\7\60\2\2\u0109\u010a\7\60\2\2\u010aH")
        buf.write("\3\2\2\2\u010b\u010c\7?\2\2\u010c\u010d\7?\2\2\u010dJ")
        buf.write("\3\2\2\2\u010e\u010f\7*\2\2\u010fL\3\2\2\2\u0110\u0111")
        buf.write("\7+\2\2\u0111N\3\2\2\2\u0112\u0113\7]\2\2\u0113P\3\2\2")
        buf.write("\2\u0114\u0115\7_\2\2\u0115R\3\2\2\2\u0116\u0117\7.\2")
        buf.write("\2\u0117T\3\2\2\2\u0118\u011c\t\2\2\2\u0119\u011b\t\3")
        buf.write("\2\2\u011a\u0119\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a")
        buf.write("\3\2\2\2\u011c\u011d\3\2\2\2\u011dV\3\2\2\2\u011e\u011c")
        buf.write("\3\2\2\2\u011f\u0121\5Y-\2\u0120\u011f\3\2\2\2\u0121\u0122")
        buf.write("\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123")
        buf.write("\u012b\3\2\2\2\u0124\u012c\5_\60\2\u0125\u0127\5_\60\2")
        buf.write("\u0126\u0125\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0129\3")
        buf.write("\2\2\2\u0128\u012a\5]/\2\u0129\u0128\3\2\2\2\u0129\u012a")
        buf.write("\3\2\2\2\u012a\u012c\3\2\2\2\u012b\u0124\3\2\2\2\u012b")
        buf.write("\u0126\3\2\2\2\u012cX\3\2\2\2\u012d\u012e\t\4\2\2\u012e")
        buf.write("Z\3\2\2\2\u012f\u0130\t\5\2\2\u0130\\\3\2\2\2\u0131\u0133")
        buf.write("\t\6\2\2\u0132\u0134\5[.\2\u0133\u0132\3\2\2\2\u0133\u0134")
        buf.write("\3\2\2\2\u0134\u0136\3\2\2\2\u0135\u0137\5Y-\2\u0136\u0135")
        buf.write("\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0136\3\2\2\2\u0138")
        buf.write("\u0139\3\2\2\2\u0139^\3\2\2\2\u013a\u013e\7\60\2\2\u013b")
        buf.write("\u013d\5Y-\2\u013c\u013b\3\2\2\2\u013d\u0140\3\2\2\2\u013e")
        buf.write("\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f`\3\2\2\2\u0140")
        buf.write("\u013e\3\2\2\2\u0141\u0144\5\3\2\2\u0142\u0144\5\5\3\2")
        buf.write("\u0143\u0141\3\2\2\2\u0143\u0142\3\2\2\2\u0144b\3\2\2")
        buf.write("\2\u0145\u014a\7$\2\2\u0146\u0149\5g\64\2\u0147\u0149")
        buf.write("\5e\63\2\u0148\u0146\3\2\2\2\u0148\u0147\3\2\2\2\u0149")
        buf.write("\u014c\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b\3\2\2\2")
        buf.write("\u014b\u014d\3\2\2\2\u014c\u014a\3\2\2\2\u014d\u014e\7")
        buf.write("$\2\2\u014e\u014f\b\62\2\2\u014fd\3\2\2\2\u0150\u0151")
        buf.write("\7^\2\2\u0151\u0155\t\7\2\2\u0152\u0153\7)\2\2\u0153\u0155")
        buf.write("\7$\2\2\u0154\u0150\3\2\2\2\u0154\u0152\3\2\2\2\u0155")
        buf.write("f\3\2\2\2\u0156\u0157\n\b\2\2\u0157h\3\2\2\2\u0158\u0159")
        buf.write("\t\t\2\2\u0159j\3\2\2\2\u015a\u015b\7%\2\2\u015b\u015c")
        buf.write("\7%\2\2\u015c\u0160\3\2\2\2\u015d\u015f\n\n\2\2\u015e")
        buf.write("\u015d\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2")
        buf.write("\u0160\u0161\3\2\2\2\u0161\u0163\3\2\2\2\u0162\u0160\3")
        buf.write("\2\2\2\u0163\u0164\b\66\3\2\u0164l\3\2\2\2\u0165\u0167")
        buf.write("\t\13\2\2\u0166\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168")
        buf.write("\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\3\2\2\2")
        buf.write("\u016a\u016b\b\67\3\2\u016bn\3\2\2\2\u016c\u016d\13\2")
        buf.write("\2\2\u016d\u016e\b8\4\2\u016ep\3\2\2\2\u016f\u0174\7$")
        buf.write("\2\2\u0170\u0173\5g\64\2\u0171\u0173\5e\63\2\u0172\u0170")
        buf.write("\3\2\2\2\u0172\u0171\3\2\2\2\u0173\u0176\3\2\2\2\u0174")
        buf.write("\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u017a\3\2\2\2")
        buf.write("\u0176\u0174\3\2\2\2\u0177\u0178\7\17\2\2\u0178\u017b")
        buf.write("\7\f\2\2\u0179\u017b\t\f\2\2\u017a\u0177\3\2\2\2\u017a")
        buf.write("\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017d\b9\5\2")
        buf.write("\u017dr\3\2\2\2\u017e\u0183\7$\2\2\u017f\u0182\5g\64\2")
        buf.write("\u0180\u0182\5e\63\2\u0181\u017f\3\2\2\2\u0181\u0180\3")
        buf.write("\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184")
        buf.write("\3\2\2\2\u0184\u0186\3\2\2\2\u0185\u0183\3\2\2\2\u0186")
        buf.write("\u0187\5u;\2\u0187\u0188\b:\6\2\u0188t\3\2\2\2\u0189\u018d")
        buf.write("\t\r\2\2\u018a\u018b\7^\2\2\u018b\u018d\n\7\2\2\u018c")
        buf.write("\u0189\3\2\2\2\u018c\u018a\3\2\2\2\u018dv\3\2\2\2\27\2")
        buf.write("\u011c\u0122\u0126\u0129\u012b\u0133\u0138\u013e\u0143")
        buf.write("\u0148\u014a\u0154\u0160\u0168\u0172\u0174\u017a\u0181")
        buf.write("\u0183\u018c\7\3\62\2\b\2\2\38\3\39\4\3:\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQUAL = 28
    ASSIGN = 29
    NOT_EQUAL = 30
    LT = 31
    LE = 32
    GT = 33
    GE = 34
    CONCAT_STR = 35
    COMPARE_STR = 36
    LR_BRACKET = 37
    RR_BRACKET = 38
    LS_BRACKET = 39
    RS_BRACKET = 40
    COMMA = 41
    ID = 42
    NUMBER_LIT = 43
    BOOL_LIT = 44
    STRING_LIT = 45
    NEWLINE = 46
    COMMENTS = 47
    WS = 48
    ERROR_CHAR = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQUAL", "ASSIGN", "NOT_EQUAL", 
            "LT", "LE", "GT", "GE", "CONCAT_STR", "COMPARE_STR", "LR_BRACKET", 
            "RR_BRACKET", "LS_BRACKET", "RS_BRACKET", "COMMA", "ID", "NUMBER_LIT", 
            "BOOL_LIT", "STRING_LIT", "NEWLINE", "COMMENTS", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
                  "ASSIGN", "NOT_EQUAL", "LT", "LE", "GT", "GE", "CONCAT_STR", 
                  "COMPARE_STR", "LR_BRACKET", "RR_BRACKET", "LS_BRACKET", 
                  "RS_BRACKET", "COMMA", "ID", "NUMBER_LIT", "DIGIT", "SIGN", 
                  "EXPONENT", "DECIMAL", "BOOL_LIT", "STRING_LIT", "VALID_ESCAPE", 
                  "VALID_SEQUENCE", "NEWLINE", "COMMENTS", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "INVALID_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[48] = self.STRING_LIT_action 
            actions[54] = self.ERROR_CHAR_action 
            actions[55] = self.UNCLOSE_STRING_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1];
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             
                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[1:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:])
     


