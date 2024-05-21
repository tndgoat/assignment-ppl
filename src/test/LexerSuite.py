import unittest

from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_KeyWord_Operators_Separators(self):
        """test KeyWord Operators Separators"""

        ##^ test KeyWord
        input = "true false number bool string return var dynamic func for until by break continue if else elif begin end not and or"
        expect = "true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 101))

        ##^ test Operators
        input = "+-*/%= <- != < <= > >= ... =="
        expect = "+,-,*,/,%,=,<-,!=,<,<=,>,>=,...,==,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 102))

        ##^ test Separators
        input = "[(,,)]"
        expect = "[,(,,,,,),],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 103))

        ##^ test fail toán tử
        input = "&"
        expect = "Error Token &"
        self.assertTrue(TestLexer.test(input, expect, 104))

        input = "#"
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 105))

    def test_Identifiers(self):
        """test Identifiers"""
        ##^ test true ID
        self.assertTrue(
            TestLexer.test(
                "A _ a az AZ aZ _a a_ a1 _1 A1",
                "A,_,a,az,AZ,aZ,_a,a_,a1,_1,A1,<EOF>",
                106,
            )
        )

        ##^ test false ID
        self.assertTrue(TestLexer.test("1Nguyenc", "1,Nguyenc,<EOF>", 107))
        self.assertTrue(TestLexer.test("11Nguyenc", "11,Nguyenc,<EOF>", 108))

    def test_Literal(self):
        """test Identifiers"""

        ##^ test NUMBER_LIT
        input = "0 -0 199 001 012. 12. 0. 12.3 12.3e3 12.3e-30 2.e3 0.e-30 31e+3 31e-3 0e+3 0e-3"
        expect = "0,-,0,199,001,012.,12.,0.,12.3,12.3e3,12.3e-30,2.e3,0.e-30,31e+3,31e-3,0e+3,0e-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 109))
        ##^ fail NUMBER_LIT
        self.assertTrue(TestLexer.test(".12e-3", "Error Token .", 110))
        self.assertTrue(TestLexer.test("12.2h-3", "12.2,h,-,3,<EOF>", 111))

        ##^ test STRING_LIT
        input = """ "Tung  Nguyen" """  # kiểm tra bình thường
        expect = "Tung  Nguyen,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 112))
        self.assertTrue(TestLexer.test(""" "" """, ",<EOF>", 113))  # chuỗi rỗng

        ##^ kiểm tra các kí tự cho phép
        input = """ "' \\b \\f \\r \\n \\t \\\\ Tung \\b \\f \\r \\n \\t \\\\  Nguyen \\b \\f \\r \\n \\t \\\\" """
        expect = "' \\b \\f \\r \\n \\t \\\\ Tung \\b \\f \\r \\n \\t \\\\  Nguyen \\b \\f \\r \\n \\t \\\\,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 114))
        self.assertTrue(
            TestLexer.test(
                """ "'"Tung '" Nguyen '' '"" """, "'\"Tung '\" Nguyen '' '\",<EOF>", 115
            )
        )

        ##^ kiểm tra lỗi Unclosed String
        self.assertTrue(
            TestLexer.test(""" "Tung \n" """, "Unclosed String: Tung ", 116)
        )
        self.assertTrue(
            TestLexer.test(""" "Tung \n Nguyen" """, "Unclosed String: Tung ", 117)
        )
        self.assertTrue(TestLexer.test(""" "Tung  """, "Unclosed String: Tung  ", 118))
        self.assertTrue(
            TestLexer.test(""" "Tung \\n \n """, "Unclosed String: Tung \\n ", 119)
        )
        self.assertTrue(
            TestLexer.test(
                """ "Tung ' \\n \\b """, "Unclosed String: Tung ' \\n \\b ", 120
            )
        )

        ##^ kiểm tra lỗi Illegal Escape
        self.assertTrue(
            TestLexer.test(
                """ "Nguyen ' \\1  """, "Illegal Escape In String: Nguyen ' \\1", 123
            )
        )
        self.assertTrue(
            TestLexer.test(
                """ "Nguyen \\2 \\n \n """, "Illegal Escape In String: Nguyen \\2", 124
            )
        )
        self.assertTrue(
            TestLexer.test(
                """ "Nguyen \\e \\n \\r """, "Illegal Escape In String: Nguyen \\e", 125
            )
        )
        self.assertTrue(
            TestLexer.test(
                """ "Nguyen '" \\321 \\n \\r """,
                "Illegal Escape In String: Nguyen '\" \\3",
                126,
            )
        )
        self.assertTrue(
            TestLexer.test(
                """ "Nguyen \\"1 " """, 'Illegal Escape In String: Nguyen \\"', 127
            )
        )
        self.assertTrue(
            TestLexer.test(
                """ "Nguyen ' '" \\" """,
                "Illegal Escape In String: Nguyen ' '\" \\\"",
                128,
            )
        )
        self.assertTrue(
            TestLexer.test(
                """ "Nguyen \\' ""1 """, "Nguyen \\' ,Unclosed String: 1 ", 129
            )
        )

    def test_Comments_newline(self):
        """test Comments và newline"""
        self.assertTrue(TestLexer.test("## Tung Nguyen", "<EOF>", 130))
        self.assertTrue(TestLexer.test("###", "<EOF>", 131))
        self.assertTrue(TestLexer.test("a##1", "a,<EOF>", 132))
        self.assertTrue(TestLexer.test("a#", "a,Error Token #", 133))
        self.assertTrue(TestLexer.test("a\n##1\nb", "a,\n,\n,b,<EOF>", 134))
        self.assertTrue(TestLexer.test("a\n\n\n#", "a,\n,\n,\n,Error Token #", 135))
        input = """a
                    ## comment
                """
        expect = """a,
,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 136))

    def test_complex(self):  # test case 140 ->

        input = "."
        expect = "Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 140))

        input = ";"
        expect = "Error Token ;"
        self.assertTrue(TestLexer.test(input, expect, 141))

        input = "{"
        expect = "Error Token {"
        self.assertTrue(TestLexer.test(input, expect, 142))

        self.assertTrue(TestLexer.test("+1-2", "+,1,-,2,<EOF>", 143))
        self.assertTrue(
            TestLexer.test(""" "Nguyen \t \n" """, "Unclosed String: Nguyen 	 ", 144)
        )
        self.assertTrue(
            TestLexer.test(
                """ "Nguyen \\" """, 'Illegal Escape In String: Nguyen \\"', 145
            )
        )
        self.assertTrue(
            TestLexer.test(
                """ "Nguyen \\\n """, "Illegal Escape In String: Nguyen \\\n", 146
            )
        )
        self.assertTrue(
            TestLexer.test(
                """ "Nguyen '\\ """, "Illegal Escape In String: Nguyen '\\ ", 147
            )
        )
        self.assertTrue(TestLexer.test(""" "Nguyen \'" " """, "Nguyen '\" ,<EOF>", 148))
        self.assertTrue(
            TestLexer.test(
                """ "Nguyen \\\'" " """, "Nguyen \\',Unclosed String:  ", 149
            )
        )
        self.assertTrue(
            TestLexer.test(
                """ "Nguyen 
                                       " """,
                "Unclosed String: Nguyen ",
                150,
            )
        )
        self.assertTrue(
            TestLexer.test(
                """ ##Tung Nguyen
##Tung Nguyen\n
##Tung Nguyen """,
                """
,
,
,<EOF>""",
                151,
            )
        )

        self.assertTrue(
            TestLexer.test(
                """ ##Tung Nguyen "123" ## 12 \n""",
                """
,<EOF>""",
                152,
            )
        )

        self.assertTrue(
            TestLexer.test(""" "\\a" """, """Illegal Escape In String: \\a""", 153)
        )

        self.assertTrue(
            TestLexer.test(""" "\\:" """, """Illegal Escape In String: \\:""", 154)
        )

        self.assertTrue(
            TestLexer.test(
                """ "\\\\1 \\z" """, """Illegal Escape In String: \\\\1 \\z""", 155
            )
        )

        self.assertTrue(
            TestLexer.test(
                """ "'z \\z" """, """Illegal Escape In String: 'z \\z""", 156
            )
        )

        self.assertTrue(
            TestLexer.test(
                """ "'a \\a" """, """Illegal Escape In String: 'a \\a""", 157
            )
        )

        self.assertTrue(TestLexer.test("1.1/3", "1.1,/,3,<EOF>", 110))
