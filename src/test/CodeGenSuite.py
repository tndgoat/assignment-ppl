import unittest

from AST import *
from TestUtils import TestCodeGen


class CheckCodeGenSuite(unittest.TestCase):
    # * test cơ bản về hàm main và các hàm write
    def test_1(self):
        input = """
        func main ()
        begin
            writeNumber(1)
            writeBool(true)
            writeString("votien")
        end
        """
        expect = "1.0\ntrue\nvotien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

        input = """
        func main ()
        begin
            writeNumber(1.0)
            writeBool(false)
            writeString("")
        end
        """
        expect = "1.0\nfalse\n\n"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    # * test visitVarDecl và visitId và visitAssign và visitReturn và visitCallStmt(cơ bản)
    def test_2(self):
        # * test visitVarDecl biến toàn cục emit.put và emit.get
        input = """
        number a <- 1
        func main ()
        begin
            writeNumber(a)
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

        # * test visitVarDecl biến cục bộ emit.read và emit.write
        input = """
        number a <- 1
        func main ()
        begin
            number a <- 2
            writeNumber(a)
        end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

        input = """
        number a <- 1
        func main ()
        begin
            begin
                number a <- 2
            end
            writeNumber(a)
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

        input = """
        number a <- 1
        func main ()
        begin
            begin
                number a <- 2
                writeNumber(a)
            end
            writeNumber(a)
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

        input = """
        dynamic a
        func main ()
        begin
            bool b <- true
            begin
                a <- b
            end
            writeBool(a)
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

        input = """
        dynamic a
        func main ()
        begin
            var b <- "votien"
            begin
                a <- b
            end
            writeString(a)
        end
        """
        expect = "votien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

        input = """
        dynamic a <- 1
        func foo(number a)
        begin
            writeNumber(a)
        end
        func main ()
        begin
            foo(2)
        end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

        input = """
        dynamic a <-1
        func foo(number a)
        begin
            var a <- 3
            writeNumber(a)
        end
        func main ()
        begin
            foo(2)
        end
        """
        expect = "3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

        input = """
        dynamic a <-1
        func foo(number a)
        begin
            writeNumber(a)
            var a <- 3
            writeNumber(a)
        end
        func main ()
        begin
            foo(2)
            writeNumber(a)
        end
        """
        expect = "2.0\n3.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

        input = """
        dynamic a <-1
        func foo()
        begin
            a <- 3
        end
        func main ()
        begin
            foo()
            writeNumber(a)
        end
        """
        expect = "3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

        input = """
        dynamic a <- 1
        func foo()
        begin
            begin
                number a <- 2
            end
            writeNumber(a)
            a <- 3
        end
        func main ()
        begin
            foo()
            writeNumber(a)
        end
        """
        expect = "1.0\n3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

        input = """
        dynamic a <- 1
        func foo()
        begin
            a <- 3
            writeNumber(a)
        end
        func main ()
        begin
            number a <- 2
            foo()
            writeNumber(a)
        end
        """
        expect = "3.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

        input = """
        dynamic a
        func foo()
        func main ()
        begin
            foo()
            writeNumber(a)
        end
        func foo()
        begin
            a <- 3
            writeNumber(a)
        end
        """
        expect = "3.0\n3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    # * test visitCallExpr và visitReturn
    def test_3(self):
        input = """
        func foo(number a)
        begin
            return a
        end
        func main ()
        begin
            writeNumber(foo(2))
        end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

        input = """
        func foo(number a)
        begin
            return true
        end
        func main ()
        begin
            writeBool(foo(2))
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

        input = """
        func foo(string a)
        begin
            return a
        end
        func main ()
        begin
            writeString(foo("vo"))
        end
        """
        expect = "vo\n"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

        input = """
        func main ()
        begin
            var a <- readString()
            writeString(a)
        end
        """
        expect = "-1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

        input = """
        func main ()
        begin
            var a <- readNumber()
            writeNumber(a)
        end
        """
        expect = "-1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

        # input = """
        # func main ()
        # begin
        #     var a <- readBool() #* true
        #     writeBool(a)
        # end
        # """
        # expect = "true\n"
        # self.assertTrue(TestCodeGen.test(input, expect, 503))

        input = """
        func foo()
            return true
        func main ()
        begin
            var a <- foo() ## true
            writeBool(a)
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

        input = """
        func foo()
            return "votien"
        func main ()
        begin
            var a <- foo() ## true
            writeString(a)
        end
        """
        expect = "votien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

        input = """
        func foo(number a, number c)
            return a
        func main ()
        begin
            var a <- foo(1, 2) ## true
            writeNumber(a)
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

        input = """
        number c <- 5
        func foo(number a, number c)
        begin
            return c
        end
        func main ()
        begin
            var a <- foo(1, 2)
            writeNumber(a)
        end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

        input = """
        number c <- 5
        func foo(number a)
        begin
            return c
        end
        func main ()
        begin
            var a <- foo(1)
            writeNumber(a)
        end
        """
        expect = "5.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    # * test visitBinaryOp và visitUnaryOp
    def test_4(self):
        input = """
        func main ()
        begin
            writeNumber(1 + 1)
            writeNumber(1 - 1)
            writeNumber(1 * 2)
            writeNumber(1 / 2)
            writeNumber(7.5%3.5)
            writeNumber(7.8%3.38)
        end
        """
        expect = "2.0\n0.0\n2.0\n0.5\n0.5\n1.04\n"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

        input = """
        func main ()
        begin
            writeNumber(1 + 1 + 1)
            writeNumber(1 + 1 * 3 - 1 * 2 / 2)
            writeNumber(2 * 3 % 2)
        end
        """
        expect = "3.0\n3.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

        input = """
        func main ()
        begin
            writeBool(1 > 2) ## push -1
            writeBool(2 > 1) ## push 1
            writeBool(1 > 1) ## push 0
        end
        """
        expect = "false\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

        input = """
        func main ()
        begin
            writeBool(1 >= 2)
            writeBool(2 >= 1)
            writeBool(1 >= 1)
        end
        """
        expect = "false\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

        input = """
        func main ()
        begin
            writeBool(1 < 2)
            writeBool(2 < 1)
            writeBool(1 < 1)
        end
        """
        expect = "true\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

        input = """
        func main ()
        begin
            writeBool(1 <= 2)
            writeBool(2 <= 1)
            writeBool(1 <= 1)
        end
        """
        expect = "true\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

        input = """
        func main ()
        begin
            writeBool(1 != 2)
            writeBool(2 != 1)
            writeBool(1 != 1)
        end
        """
        expect = "true\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

        input = """
        func main ()
        begin
            writeBool(1 = 2)
            writeBool(2 = 1)
            writeBool(1 = 1)
        end
        """
        expect = "false\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

        input = """
        func main ()
        begin
            writeBool(true and true)
            writeBool(true and false)
            writeBool(false and true)
            writeBool(false and false)
        end
        """
        expect = "true\nfalse\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

        input = """
        func main ()
        begin
            writeBool(true or true)
            writeBool(true or false)
            writeBool(false or true)
            writeBool(false or false)
        end
        """
        expect = "true\ntrue\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

        input = """
        func main ()
        begin
            writeBool(true or true and false or true)
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

        input = """
        func main ()
        begin
            writeString("vo" ... "tien")
        end
        """
        expect = "votien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

        input = """
        func main ()
        begin
            writeBool("vo" == "tien")
            writeBool("tien" == "tien")
        end
        """
        expect = "false\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

        input = """
        func main ()
        begin
            writeBool(not not true)
            writeBool(not true)
            writeBool(not false)
        end
        """
        expect = "true\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

        input = """
        func main ()
        begin
            writeNumber(--1)
            writeNumber(-1)
        end
        """
        expect = "1.0\n-1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    # * test visitFor
    def test_5(self):
        input = """
        func main ()
        begin
            var i <- 0
            for i until i >= 2 by 1
                writeNumber(i)

            writeNumber(i)
        end
        """
        expect = "0.0\n1.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

        input = """
        func main ()
        begin
            var i <- 0
            for i until i >= 2 by 1
            begin
                i <- 1000
                break
            end
            writeNumber(i)
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

        # * ảo ma canada
        # input = """
        # func main ()
        # begin
        #     var i <- 0
        #     for i until i >= 1 by 1
        #         var k <- 2
        #     writeNumber(i)
        #     ## writeNumber(k)
        # end
        # """
        # expect = "0.0\n"
        # self.assertTrue(TestCodeGen.test(input, expect, 505))

        input = """
        func main ()
        begin
            var i <- 0
            for i until i > 2 by 1
                writeNumber(i)
        end
        """
        expect = "0.0\n1.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

        input = """
        func main ()
        begin
            var i <- 0
            for i until i > 2 by 2
                writeNumber(i)
        end
        """
        expect = "0.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

        input = """
        func main ()
        begin
            var i <- 3
            for i until i > 2 by 2
                writeNumber(i)
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 545))

        input = """
        func main ()
        begin
            var i <- 0
            for i until i >= 2 by 1
            begin
                writeNumber(i)
                continue
                writeNumber(i)
            end
        end
        """
        expect = "0.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

        input = """
        func main ()
        begin
            var i <- 0
            for i until i >= 2 by 1
            begin
                writeNumber(i)
                break
                writeNumber(i)
            end
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

        input = """
        func main ()
        begin
            var i <- 0
            for i until i >= 2 by 1
                break
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    # * test visitIf và visitFor
    def test_6(self):
        input = """
            func main()
            begin
                if (true) writeNumber(1)
                else writeNumber(0)
            end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

        input = """
            func main()
            begin
                if (2 > 3) writeNumber(1)
                else writeNumber(0)
            end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

        input = """
            func main()
            begin
                if (2 = 2) writeNumber(1)
            end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

        input = """
            func main()
            begin
                var a <- 1
                if (a = 0) writeNumber(1)
                elif (a = 1) writeNumber(2)
                elif (a = 2) writeNumber(3)
            end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

        input = """
            func main()
            begin
                var a <- 2
                if (a = 0) writeNumber(1)
                elif (a = 1) writeNumber(2)
                elif (a = 2) writeNumber(3)
            end
        """
        expect = "3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

        input = """
            func main()
            begin
                var a <- 0
                if (a = 0) writeNumber(1)
                elif (a = 1) writeNumber(2)
                elif (a = 2) writeNumber(3)
            end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

        input = """
            func main()
            begin
                var a <- -1
                if (a = 0) writeNumber(1)
                elif (a = 1) writeNumber(2)
                elif (a = 2) writeNumber(3)
                else writeNumber(4)
            end
        """
        expect = "4.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

        # input = """
        #     func main()
        #     begin
        #         var a <- 0
        #         if (a = 0) var b <- 2
        #         elif (a = 1)  var b <- 3
        #         elif (a = 2)  var b <- 4
        #         else  var b <- 5
        #          writeNumber(b)
        #     end
        # """
        # expect = "4.0\n"
        # self.assertTrue(TestCodeGen.test(input, expect, 556))

        input = """
            func main()
            begin
                var i <- 0
                for i until i >= 10 by 1
                begin
                    if (i = 3) break
                    writeNumber(i)
                end
            end
        """
        expect = "0.0\n1.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

        input = """
            func main()
            begin
                var i <- 0
                for i until i >= 10 by 2
                begin
                    if (i = 3) break
                    writeNumber(i)
                end
            end
        """
        expect = "0.0\n2.0\n4.0\n6.0\n8.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    # * visitArrayCell và visitAssign và khởi tạo array
    def test_7(self):
        input = """
        number a[2]
        func main ()
        begin
            writeNumber(a[1])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

        input = """
        number a[2]
        func main ()
        begin
            writeNumber(a[1] + 1)
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

        input = """
        number a[2]
        func main ()
        begin
            var x <- a[0]
            writeNumber(x)
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

        input = """
        func main ()
        begin
            number a[2]
            var x <- a[0] + 2.5
            writeNumber(x)
        end
        """
        expect = "2.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

        input = """
        number a[2, 3]
        func main ()
        begin
           writeNumber(a[0,0])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

        input = """
        func main ()
        begin
            number a[2, 3]
           writeNumber(a[0,0])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

        input = """
        func main ()
        begin
            number a[2,2,2,2]
           writeNumber(a[0,0,0,0])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

        input = """
        func main ()
        begin
            number a[2,2,2,2]
            var c <- a[0,0,0]
           writeNumber(c[0])
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 566))

        input = """
        number a[2]
        func main ()
        begin
           a[1] <- 1
           writeNumber(a[1])
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

        input = """
        number a[2]
        func main ()
        begin
           a[1] <- a[0] + 1
           writeNumber(a[1])
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

        input = """
        number a[2,2]
        func main ()
        begin
           a[1,1] <- a[0,0] + 1
           writeNumber(a[1,1])
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

        input = """
        func main ()
        begin
            number a[2,2]
           a[1,1] <- a[0,0] + 1
           writeNumber(a[1,1])
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 570))

        input = """
        func main ()
        begin
            number a[2,2]
           var b <- a[0]
           b[0] <- 1
           writeNumber(a[0,0])
           writeNumber(b[0])
        end
        """
        expect = "1.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

        input = """
        bool a[2]
        bool b[2,2]
        func main ()
        begin
            writeBool(a[1])
            writeBool(b[0,0])
            a[0] <- true
            writeBool(a[0])
            b[0,0] <- true
            writeBool(b[0,0])
            var c <- b[0]
            c[1] <- true
            writeBool(b[0,1])
        end
        """
        expect = "false\nfalse\ntrue\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

        input = """
        func main ()
        begin
            bool a[2]
            bool b[2,2]
            writeBool(a[1])
            writeBool(b[0,0])
            a[0] <- true
            writeBool(a[0])
            b[0,0] <- true
            writeBool(b[0,0])
            var c <- b[0]
            c[1] <- true
            writeBool(b[0,1])
        end
        """
        expect = "false\nfalse\ntrue\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    # * test khởi tạo hàm và visitCallStmt và return
    def test_9(self):
        input = """
        func foo(string a)
        begin
            writeString(a)
        end
        func main ()
        begin
            foo("Votien")
        end
        """
        expect = "Votien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

        input = """
        func foo(string a)
        func main ()
        begin
            foo("Votien")
        end
        func foo(string a)
        begin
            writeString(a)
        end
        """
        expect = "Votien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

        input = """
        func foo(string a, bool b)
        func main ()
        begin
            foo("Votien", true)
        end
        func foo(string a, bool b)
        begin
            writeString(a)
            writeBool(true)
        end
        """
        expect = "Votien\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

        input = """
        func foo()
        begin
            writeString("1")
        end
        func foo1()
        begin
            writeString("2")
        end
        func main ()
        begin
            foo()
            foo1()
        end

        """
        expect = "1\n2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 595))

        input = """
        func foo(number a)
        begin
            writeNumber(a)
        end
        func main ()
        begin
            dynamic a
            a <- 1
            foo(a)
        end

        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    # * test all
    def test_10(self):
        input = """
        func areDivisors(number num1, number num2)
        return ((num1 % num2 = 0) or (num2 % num1 = 0))
        func main()
        begin
        var num1 <- 3
        var num2 <- 4
        if (areDivisors(num1, num2)) writeString("Yes")
        else writeString("No")
        end

                """
        expect = "No\n"
        self.assertTrue(TestCodeGen.test(input, expect, 900))

        input = """
        func areDivisors(number num1, number num2)
        return ((num1 % num2 = 0) or (num2 % num1 = 0))
        func main()
        begin
        var num1 <- 2
        var num2 <- 4
        if (areDivisors(num1, num2)) writeString("Yes")
        else writeString("No")
        end

                """
        expect = "Yes\n"
        self.assertTrue(TestCodeGen.test(input, expect, 901))

        input = """
        func isPrime(number x)
        func main()
        begin
        number x <- 7
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
        end
        func isPrime(number x)
        begin
        if (x <= 1) return false
        var i <- 2
        for i until i > x / 2 by 1
        begin
        if (x % i = 0) return false

        end
        return true
        end

                """
        expect = "Yes\n"
        self.assertTrue(TestCodeGen.test(input, expect, 902))

        input = """
            func isPrime(number x)
            func main()
            begin
            number x <- 59
            if (isPrime(x)) writeString("Yes")
            else writeString("No")
            end
            func isPrime(number x)
            begin
            if (x <= 1) return false
            var i <- 2
            for i until i > x / 2 by 1
            begin
            if (x % i = 0) return false

            end
            return true
            end

                    """
        expect = "Yes\n"
        self.assertTrue(TestCodeGen.test(input, expect, 903))

        input = """
        func isPrime(number x)
        func main()
        begin
        number x <- -9
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
        end
        func isPrime(number x)
        begin
        if (x <= 1) return false
        var i <- 2
        for i until i > x / 2 by 1
        begin
        if (x % i = 0) return false

        end
        return true
        end

                """
        expect = "No\n"
        self.assertTrue(TestCodeGen.test(input, expect, 904))

        input = """
        func isPrime(number x)
        func main()
        begin
        number x <- 24
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
        end
        func isPrime(number x)
        begin
        if (x <= 1) return false
        var i <- 2
        for i until i > x / 2 by 1
        begin
        if (x % i = 0) return false
        end
        return true
        end

                """
        expect = "No\n"
        self.assertTrue(TestCodeGen.test(input, expect, 905))
