from abc import ABC
from functools import reduce

from AST import *
from Emitter import *
from Frame import Frame
from Visitor import *


class CodeGenerator:
    def gen(self, ast, path):
        # ast: AST
        # dir_: String
        gc = CodeGenVisitor(ast, path)
        gc.visit(ast, None)


class Access:
    def __init__(self, frame, symbol, isLeft, checkTypeLHS_RHS=False):
        self.frame = frame
        self.symbol = symbol
        self.isLeft = isLeft
        self.checkTypeLHS_RHS = checkTypeLHS_RHS


class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, path):
        self.astTree = astTree
        self.path = path
        self.className = "ZCodeClass"
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.Listfunction = []
        self.function = None
        self.Return = False
        self.arrayCell = ""

    def printListfunction(self):
        print(f"self.function: {str(self.function)}")
        print(f"self.Return  : {str(self.Return)}")
        print(f"listFunction :")
        for item in self.Listfunction:
            print(f"         : {str(item)}")

    # CẬP NHẬT TYPE
    def LHS_RHS(self, LHS, RHS, o):
        # TRUYỀN checkTypeLHS_RHS = Flase -> nghĩa là chúng ta xét type trước, trước khi lấy stack
        _, rhsType = self.visit(RHS, Access(o.frame, o.symbol, False, True))
        _, lhsType = self.visit(LHS, Access(o.frame, o.symbol, True, True))
        if isinstance(lhsType, Zcode):
            lhsType.typ = rhsType
            self.emit.setType(lhsType)  # cập nhật lại type vì trước đó type là None

        elif isinstance(rhsType, Zcode):
            rhsType.typ = lhsType
            self.emit.setType(rhsType)  # cập nhật lại type vì trước đó type là None

    def visitProgram(self, ast: Program, o):
        # khởi tạo chương trình ZCodeClass
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        # cập nhật biến toàn cục và function, và khởi tạo self.emit.emitATTRIBUTE cho biến toàn cục
        Symbol = [[]]
        Main = None
        function = None
        for item in ast.decl:
            if type(item) is VarDecl:
                index = -1
                Symbol[0].append(
                    VarZcode(
                        item.name.name,
                        item.varType,
                        -1,
                        True if item.varInit else False,
                    )
                )
                self.emit.printout(
                    self.emit.emitATTRIBUTE(
                        item.name.name,
                        item.varType if item.varType else Symbol[0][-1],
                        False,
                        self.className,
                    )
                )
                Symbol[0][-1].line = self.emit.printIndexNew()
            elif type(item) is FuncDecl and item.body is not None:
                self.Listfunction += [
                    FuncZcode(item.name.name, None, [i.varType for i in item.param])
                ]
                if item.name.name == "main":
                    function = self.Listfunction[-1]
                    Main = item

        # hàm khởi tạo trong Zcode (contructor bắt buộc)
        frame = Frame("<init>", VoidType)
        self.emit.printout(
            self.emit.emitMETHOD(
                lexeme="<init>",
                in_=FuncZcode("init", VoidType(), []),
                isStatic=False,
                frame=frame,
            )
        )
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(
            self.emit.emitVAR(
                frame.getNewIndex(),
                "this",
                Zcode(),
                frame.getStartLabel(),
                frame.getEndLabel(),
                frame,
            )
        )
        self.emit.printout(self.emit.emitREADVAR("this", self.className, 0, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

        # hàm khởi tạo biến static Zcode (contructor cho static)
        frame = Frame("<clinit>", VoidType)
        self.emit.printout(
            self.emit.emitMETHOD(
                lexeme="<clinit>",
                in_=FuncZcode("clinit", VoidType(), []),
                isStatic=True,
                frame=frame,
            )
        )
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # có 2 TH là khởi tạo và khởi tạo array
        for var in ast.decl:
            if type(var) is VarDecl and var.varInit is not None:
                self.visit(Assign(var.name, var.varInit), Access(frame, Symbol, False))
            elif type(var) is VarDecl and type(var.varType) is ArrayType:
                if len(var.varType.size) == 1:
                    self.emit.printout(
                        self.visit(
                            NumberLiteral(var.varType.size[0]),
                            Access(frame, Symbol, False),
                        )[0]
                    )
                    self.emit.printout(self.emit.emitF2I(frame))
                    self.emit.printout(
                        self.emit.emitNEWARRAY(var.varType.eleType, frame)
                    )
                    self.emit.printout(
                        self.emit.emitPUTSTATIC(
                            self.className + "." + var.name.name, var.varType, frame
                        )
                    )
                else:
                    for i in var.varType.size:
                        self.emit.printout(
                            self.visit(NumberLiteral(i), Access(frame, Symbol, False))[
                                0
                            ]
                        )
                        self.emit.printout(self.emit.emitF2I(frame))
                    self.emit.printout(self.emit.emitMULTIANEWARRAY(var.varType, frame))
                    self.emit.printout(
                        self.emit.emitPUTSTATIC(
                            self.className + "." + var.name.name, var.varType, frame
                        )
                    )
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

        # khởi tạo các hàm static
        i = 0
        for item in ast.decl:
            if (
                type(item) is FuncDecl
                and item.body is not None
                and item.name.name != "main"
            ):
                self.function = self.Listfunction[i]
                self.visit(item, Symbol)
            if type(item) is FuncDecl and item.body is not None:
                i += 1

        # khởi tạo hàm main
        frame = Frame("main", VoidType)
        self.emit.printout(
            self.emit.emitMETHOD(
                lexeme="main",
                in_=FuncZcode("main", VoidType(), [ArrayType([1], StringType())]),
                isStatic=True,
                frame=frame,
            )
        )
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(
            self.emit.emitVAR(
                frame.getNewIndex(),
                "args",
                ArrayType([], StringType()),
                frame.getStartLabel(),
                frame.getEndLabel(),
                frame,
            )
        )
        index = frame.getNewIndex()
        typeParam = [VarZcode("for", NumberType(), index, True)]
        self.emit.printout(
            self.emit.emitVAR(
                index,
                "for",
                NumberType(),
                frame.getStartLabel(),
                frame.getEndLabel(),
                frame,
            )
        )
        self.function = function
        self.visit(Main.body, Access(frame, [typeParam] + Symbol, False))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        self.emit.emitEPILOG()

    def visitVarDecl(self, ast, o):
        """#TODO: Implement
        # tạo emitVAR và o.symbol[0].append, cập nhật o.symbol[0][-1].line
        # if ast.varInit is not None:
            # elf.visit(Assign(ast.name, ast.varInit), o)
        # elif type(ast.varType) is ArrayType:
            # giống phần khai báo biến static gần giống ý tưởng
        """
        idx = o.frame.getNewIndex()
        code = self.emit.emitVAR(
            idx,
            ast.name.name,
            ast.varType,
            o.frame.getStartLabel(),
            o.frame.getEndLabel(),
            o.frame,
        )
        o.symbol[0].append(
            VarZcode(ast.name.name, ast.varType, idx, True if ast.varInit else False)
        )
        self.emit.printout(code)
        o.symbol[0][-1].line = self.emit.printIndexNew()
        if ast.varInit is not None:
            self.visit(Assign(ast.name, ast.varInit), o)
        elif type(ast.varType) is ArrayType:
            if len(ast.varType.size) == 1:
                self.emit.printout(self.visit(NumberLiteral(ast.varType.size[0]), o)[0])
                self.emit.printout(self.emit.emitF2I(o.frame))
                self.emit.printout(self.emit.emitNEWARRAY(ast.varType.eleType, o.frame))
                self.emit.printout(
                    self.emit.emitWRITEVAR(ast.name.name, ast.varType, idx, o.frame)
                )
            else:
                for i in ast.varType.size:
                    self.emit.printout(self.visit(NumberLiteral(i), o)[0])
                    self.emit.printout(self.emit.emitF2I(o.frame))
                self.emit.printout(self.emit.emitMULTIANEWARRAY(ast.varType, o.frame))
                self.emit.printout(
                    self.emit.emitWRITEVAR(ast.name.name, ast.varType, idx, o.frame)
                )

    def visitFuncDecl(self, ast, Symbol):
        self.Return = False
        frame = Frame(ast.name.name, VoidType)
        self.emit.printout(
            self.emit.emitMETHOD(
                lexeme=ast.name.name,
                in_=FuncZcode(ast.name.name, None, [i.varType for i in ast.param]),
                isStatic=True,
                frame=frame,
            )
        )
        symbolnew = [[]] + Symbol
        line_of_method = self.emit.printIndexNew()
        # print(self.emit.buff[line_of_method], file=f)
        frame.enterScope(True)
        for decl in ast.param:
            self.visit(decl, Access(frame, symbolnew, False))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(
            self.emit.emitVAR(
                frame.getNewIndex(),
                "args",
                ArrayType([], StringType()),
                frame.getStartLabel(),
                frame.getEndLabel(),
                frame,
            )
        )
        index = frame.getNewIndex()
        typeParam = [VarZcode("for", NumberType(), index, True)]
        self.emit.printout(
            self.emit.emitVAR(
                index,
                "for",
                NumberType(),
                frame.getStartLabel(),
                frame.getEndLabel(),
                frame,
            )
        )

        self.visit(ast.body, Access(frame, [typeParam] + symbolnew, False))
        typ = self.function.typ

        if typ is None:
            typ = VoidType()
            self.function.typ = VoidType()

        self.emit.buff[line_of_method] = self.emit.emitMETHOD(
            lexeme=ast.name.name,
            in_=FuncZcode(ast.name.name, typ, [i.varType for i in ast.param]),
            isStatic=True,
            frame=frame,
        )
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitId(self, ast, o):
        frame = o.frame
        Symbol = o.symbol

        if o.checkTypeLHS_RHS:
            for item in Symbol:
                for sym in item:
                    if sym.name == ast.name:
                        return None, sym.typ if sym.typ else sym
        flag = False
        for item in Symbol:
            for sym in item:
                if sym.name == ast.name:
                    typ = sym.typ
                    if sym.index == -1:
                        if o.isLeft:
                            code = self.emit.emitPUTSTATIC(
                                "ZCodeClass." + sym.name, sym.typ, frame
                            )
                        else:
                            code = self.emit.emitGETSTATIC(
                                "ZCodeClass." + sym.name, sym.typ, frame
                            )
                    else:
                        if o.isLeft:
                            code = self.emit.emitWRITEVAR(
                                sym.name, sym.typ, sym.index, frame
                            )
                        else:
                            code = self.emit.emitREADVAR(
                                sym.name, sym.typ, sym.index, frame
                            )
                    flag = True
                    break
            if flag:
                break
        return code, typ

    def visitCallExpr(self, ast, o):
        if ast.name.name in ["readNumber", "readBool", "readString"]:
            if ast.name.name == "readNumber":
                if o.checkTypeLHS_RHS:
                    return None, NumberType()
                return (
                    self.emit.emitINVOKESTATIC(
                        f"io/{ast.name.name}",
                        FuncZcode(ast.name.name, NumberType(), []),
                        o.frame,
                    ),
                    NumberType,
                )
            elif ast.name.name == "readBool":
                if o.checkTypeLHS_RHS:
                    return None, BoolType()
                return (
                    self.emit.emitINVOKESTATIC(
                        f"io/{ast.name.name}",
                        FuncZcode(ast.name.name, BoolType(), []),
                        o.frame,
                    ),
                    NumberType,
                )
            elif ast.name.name == "readString":
                if o.checkTypeLHS_RHS:
                    return None, StringType()
                return (
                    self.emit.emitINVOKESTATIC(
                        f"io/{ast.name.name}",
                        FuncZcode(ast.name.name, StringType(), []),
                        o.frame,
                    ),
                    NumberType,
                )

        function = None
        for item in self.Listfunction:
            if item.name == ast.name.name:
                function = item

        if o.checkTypeLHS_RHS:
            for i in range(len(function.param)):
                self.LHS_RHS(function.param[i], ast.args[i], o)
            return None, function.typ if function.typ else function

        code = ""
        for i in range(len(function.param)):
            argscode, argstype = self.visit(ast.args[i], o)
            code += argscode

        code += self.emit.emitINVOKESTATIC(
            "ZCodeClass." + ast.name.name, function, o.frame
        )
        return code, function.typ

    def visitBinaryOp(self, ast: BinaryOp, o):
        op = ast.op
        # cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            if op in ["+", "-", "*", "/", "%"]:
                self.LHS_RHS(ast.left, NumberType(), o)
                self.LHS_RHS(ast.right, NumberType(), o)
                return None, NumberType()
            elif op in ["=", "!=", "<", ">", ">=", "<="]:
                self.LHS_RHS(ast.left, NumberType(), o)
                self.LHS_RHS(ast.right, NumberType(), o)
                return None, BoolType()
            elif op in ["and", "or"]:
                self.LHS_RHS(ast.left, BoolType(), o)
                self.LHS_RHS(ast.right, BoolType(), o)
                return None, BoolType()
            elif op in ["=="]:
                self.LHS_RHS(ast.left, StringType(), o)
                self.LHS_RHS(ast.right, StringType(), o)
                return None, BoolType()
            elif op in ["..."]:
                self.LHS_RHS(ast.left, StringType(), o)
                self.LHS_RHS(ast.right, StringType(), o)
                return None, StringType()

        """#TODO emitADDOP, emitMULOP, emitREOP, emitANDOP,emitOROP, emitREOP, emitINVOKEVIRTUAL (dùng java/lang/String/concat và java/lang/String/equals)
        #^ mọi năm có tính toán lười cho and và or năm này thấy thầy ko mô tả lạ thật :((
        # khó nhất chắc là % ta dùng như sau 
            codeLeft
            codeRight
            codeLeft
            codeRight
            '/'
            emitF2I -> ép kiểu sang int
            emitI2F -> từ in ép kiểu ngược lại
            '*'
            '-'
        """

        codeLeft, _ = self.visit(ast.left, o)
        codeRight, _ = self.visit(ast.right, o)

        if ast.op in ["+", "-"]:
            op = self.emit.emitADDOP(ast.op, NumberType(), o.frame)
            typ = NumberType()

        elif ast.op in ["*", "/"]:
            op = self.emit.emitMULOP(ast.op, NumberType(), o.frame)
            typ = NumberType()

        elif ast.op in ["%"]:
            frame = o.frame
            frame.push()
            frame.push()
            first = (
                self.emit.emitMULOP("/", NumberType(), frame)
                + self.emit.emitF2I(frame)
                + self.emit.emitI2F(frame)
            )
            second = self.emit.emitMULOP(
                "*", NumberType(), frame
            ) + self.emit.emitADDOP("-", NumberType(), frame)
            return (
                codeLeft + codeRight + codeLeft + codeRight + first + second,
                NumberType(),
            )

        elif ast.op in ["and"]:
            op = self.emit.emitANDOP(o.frame)
            typ = BoolType()

        elif ast.op in ["or"]:
            op = self.emit.emitOROP(o.frame)
            typ = BoolType()

        elif ast.op in ["..."]:
            op = self.emit.emitINVOKEVIRTUAL(
                "java/lang/String/concat",
                FuncZcode("concat", StringType(), [StringType()]),
                o.frame,
            )
            typ = StringType()

        elif ast.op in ["=="]:
            op = self.emit.emitINVOKEVIRTUAL(
                "java/lang/String/equals",
                FuncZcode("equals", BoolType(), [None]),
                o.frame,
            )
            typ = BoolType()
        else:
            op = self.emit.emitREOP(ast.op, BoolType(), o.frame)
            typ = BoolType()

        return codeLeft + codeRight + op, typ

    def visitUnaryOp(self, ast: UnaryOp, o):
        op = ast.op
        # cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            if op in ["-"]:
                self.LHS_RHS(ast.operand, NumberType(), o)
                return None, NumberType()
            elif op in ["not"]:
                self.LHS_RHS(ast.operand, BoolType(), o)
                return None, BoolType()
        """#TODO mitNEGOP, emitNOT
        """
        code, _ = self.visit(ast.operand, o)

        if ast.op in ["-"]:
            op = self.emit.emitNEGOP(NumberType(), o.frame)
            typ = NumberType()
        else:
            op = self.emit.emitNOT(BoolType(), o.frame)
            typ = BoolType()
        return code + op, typ

    def visitArrayLiteral(self, ast, o):
        frame = o.frame
        # cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            mainTyp = None
            for item in ast.value:
                _, checkTyp = self.visit(item, o)
                if mainTyp is None and isinstance(
                    checkTyp, (BoolType, StringType, NumberType, ArrayType)
                ):
                    mainTyp = checkTyp
                    break

            for item in ast.value:
                self.LHS_RHS(mainTyp, item, o)

            if isinstance(mainTyp, (BoolType, StringType, NumberType)):
                return None, ArrayType([len(ast.value)], mainTyp)
            return None, ArrayType(
                [float(len(ast.value))] + mainTyp.size, mainTyp.eleType
            )

        """#TODO:
        # trường hợp mảng 1 chiều
            emitPUSHCONST -> giá trị khởi tạo của mảng
            emitF2I -> ép kiểu sang int
            emitNEWARRAY -> khởi tạo mảng
            for
                emitDUP -> nhân 2 ở đây là địa chỉ của mảng khởi tạo phía trên
                emitPUSHCONST -> giá trị index trong mảng
                emitF2I
                visit -> giá trị biến
                emitASTORE -> lưu trữ
    
        # trường hợp mảng nhiều chiều
            emitPUSHCONST -> giá trị khởi tạo của mảng
            emitF2I -> ép kiểu sang int
            emitANEWARRAY -> khởi tạo mảng
            for
                emitDUP -> nhân 2 ở đây là địa chỉ của mảng khởi tạo phía trên
                emitPUSHCONST -> giá trị index trong mảng
                emitF2I
                visit -> giá trị biến
                emitASTORE -> lưu trữ             
        """

    def visitArrayCell(self, ast, o):
        # cập nhật type lhs or RHS giống btl3

        if o.checkTypeLHS_RHS:
            _, arr = self.visit(ast.arr, Access(o.frame, o.symbol, False, False))
            for i in ast.idx:
                self.LHS_RHS(NumberType(), i, o)
            if len(arr.size) == len(ast.idx):
                return None, arr.eleType
            return None, ArrayType(arr.size[len(ast.idx) :], arr.eleType)

        find = False

        for item in o.symbol:
            for sym in item:
                if sym.name == ast.arr.name:
                    Sym = sym
                    find = True
                    break
            if find:
                break
        if len(Sym.typ.size) == len(ast.idx):
            code, _ = self.visit(ast.arr, Access(o.frame, o.symbol, False, False))
            for i in range(len(ast.idx) - 1):
                code += self.visit(ast.idx[i], Access(o.frame, o.symbol, False, False))[
                    0
                ]
                code += self.emit.emitF2I(o.frame)
                code += self.emit.emitALOAD(Sym.typ, o.frame)
            code += self.visit(ast.idx[-1], Access(o.frame, o.symbol, False, False))[0]
            code += self.emit.emitF2I(o.frame)
            if o.isLeft:
                self.arrayCell = Sym.typ.eleType
            else:
                code += self.emit.emitALOAD(Sym.typ.eleType, o.frame)
            return code, Sym.typ.eleType if Sym.typ.eleType else Sym.typ
        else:
            code, _ = self.visit(ast.arr, Access(o.frame, o.symbol, False, False))
            for i in range(len(ast.idx) - 1):
                code += self.visit(ast.idx[i], Access(o.frame, o.symbol, False, False))[
                    0
                ]
                code += self.emit.emitF2I(o.frame)
                code += self.emit.emitALOAD(Sym.typ, o.frame)
            code += self.visit(ast.idx[-1], Access(o.frame, o.symbol, False, False))[0]
            code += self.emit.emitF2I(o.frame)
            if o.isLeft:
                self.arrayCell = Sym.typ
            else:
                code += self.emit.emitALOAD(Sym.typ, o.frame)
            return code, Sym.typ.eleType

    def visitNumberLiteral(self, ast, o):
        return (
            self.emit.emitPUSHCONST(ast.value, NumberType(), o.frame)
            if not o.checkTypeLHS_RHS
            else None
        ), NumberType()

    def visitBooleanLiteral(self, ast, o):
        return (
            self.emit.emitPUSHCONST(ast.value, BoolType(), o.frame)
            if not o.checkTypeLHS_RHS
            else None
        ), BoolType()

    def visitStringLiteral(self, ast, o):
        return (
            self.emit.emitPUSHCONST('"' + ast.value + '"', StringType(), o.frame)
            if not o.checkTypeLHS_RHS
            else None
        ), StringType()

    def visitArrayType(self, ast, param):
        return None, ast

    def visitNumberType(self, ast, param):
        return None, NumberType()

    def visitVoidType(self, ast, param):
        return None, VoidType()

    def visitBoolType(self, ast, param):
        return None, BoolType()

    def visitStringType(self, ast, param):
        return None, StringType()

    def visitFuncZcode(self, ast, param):
        return None, ast.typ if ast.typ else ast

    def visitVarZcode(self, ast, param):
        return None, ast.typ if ast.typ else ast

    def visitReturn(self, ast, o):
        # CHECK TYPE BTL3
        self.LHS_RHS(self.function, ast.expr if ast.expr else VoidType(), o)
        # expr: Expr = None  # None if there is no expression after return

        self.Return = True  # đã có return
        frame = o.frame
        if ast.expr is None:
            self.emit.printout(self.emit.emitRETURN(VoidType, frame))
        else:
            code, typ = self.visit(ast.expr, o)
            self.emit.printout(code)
            self.emit.printout(self.emit.emitRETURN(typ, frame))

    def visitAssign(self, ast, o):
        self.LHS_RHS(ast.lhs, ast.rhs, o)
        frame = o.frame
        rhsCode, _ = self.visit(ast.rhs, Access(frame, o.symbol, False))
        lhsCode, _ = self.visit(ast.lhs, Access(frame, o.symbol, True))

        """#TODO
        TH1 : LHS = ArrayCell
        lhsCode
        rhsCode
        self.emit.emitASTORE(self.arrayCell, frame))
        
        TH2 : 
        lhsCode
        rhsCode        
        """
        if type(ast.lhs) is ArrayCell:
            code = lhsCode + rhsCode + self.emit.emitASTORE(self.arrayCell, frame)
        else:
            code = rhsCode + lhsCode
        self.emit.printout(code)
        self.arrayCell = ""

    def visitCallStmt(self, ast, o):
        if ast.name.name in ["writeNumber", "writeBool", "writeString"]:
            if ast.name.name == "writeNumber":
                self.LHS_RHS(NumberType(), ast.args[0], o)
            elif ast.name.name == "writeBool":
                self.LHS_RHS(BoolType(), ast.args[0], o)
            elif ast.name.name == "writeString":
                self.LHS_RHS(StringType(), ast.args[0], o)

            argsCode, argsType = self.visit(ast.args[0], o)
            self.emit.printout(argsCode)
            self.emit.printout(
                self.emit.emitINVOKESTATIC(
                    f"io/{ast.name.name}",
                    FuncZcode(ast.name.name, VoidType(), [argsType]),
                    o.frame,
                )
            )
            return

        function = None
        for item in self.Listfunction:
            if item.name == ast.name.name:
                function = item
        code = ""
        for expr in ast.args:
            cd, ty = self.visit(expr, Access(o.frame, o.symbol, False))
            code += cd
        code += self.emit.emitINVOKESTATIC(
            self.className + "/" + ast.name.name, function, o.frame
        )
        self.emit.printout(code)

    def visitBlock(self, ast, o):
        symbolnew = [[]] + o.symbol
        o.frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame))
        for item in ast.stmt:
            self.visit(item, Access(o.frame, symbolnew, False))
        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))
        o.frame.exitScope()

    def visitIf(self, ast, o):
        self.LHS_RHS(BoolType(), ast.expr, o)
        for item in ast.elifStmt:
            self.LHS_RHS(BoolType(), item[0], o)

        frame = o.frame
        """enterLoop
            điều kiện if -> nhảy đến đặt label end if
                |
            visit body
                |
            goto exit
                |
            đặt label end if
                |
            nếu có eilf -> for
                        tạo lable mới
                            |
                        điều kiện -> nhảy lable mới
                            | 
                        visit
                            |
                        goto exit
                            |
                        đặt đến lable mới
                            |
            -- end for
                |
            nếu có else
                            |
                          visit
                            |
            lable exit
        """
        exp_c, exp_t = self.visit(ast.expr, Access(o.frame, o.symbol, False))
        self.emit.printout(exp_c)

        # Label for jumping to else or the end of the whole if-elif-else structure
        endLabel = o.frame.getNewLabel()

        # False condition jumps to first elif or else
        fLabel = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(fLabel, o.frame))

        # True branch (then statement)
        self.visit(ast.thenStmt, o)
        print(ast.thenStmt)

        # After executing thenStmt, jump to end (bypassing elif and else)
        self.emit.printout(self.emit.emitGOTO(endLabel, o.frame))

        # Handle elif statements
        currentLabel = fLabel  # Start with the first false label
        if ast.elifStmt:
            for item in ast.elifStmt:
                # Label for this elif block
                self.emit.printout(self.emit.emitLABEL(currentLabel, o.frame))
                # Condition for elif
                exp_c, _ = self.visit(item[0], Access(o.frame, o.symbol, False))
                self.emit.printout(exp_c)

                # Label for next elif or else
                nextLabel = o.frame.getNewLabel()
                # If condition is false, jump to next label
                self.emit.printout(self.emit.emitIFFALSE(nextLabel, o.frame))

                # Execute elif block
                print(item[1])
                self.visit(item[1], o)

                # After elif block, jump to end
                self.emit.printout(self.emit.emitGOTO(endLabel, o.frame))

                # Update current label to next
                currentLabel = nextLabel

        # Handle else statement
        self.emit.printout(self.emit.emitLABEL(currentLabel, o.frame))
        if ast.elseStmt:
            self.visit(ast.elseStmt, o)
        else:
            # If there is no else block, just put a label
            pass

        # End label for the entire if-elif-else block
        self.emit.printout(self.emit.emitLABEL(endLabel, o.frame))

        # return str(code), None

    def visitFor(self, ast, o):

        # CHECK TYPE BTL3
        """_typID_"""
        self.LHS_RHS(NumberType(), ast.name, o)

        """_typCondExpr_"""
        self.LHS_RHS(BoolType(), ast.condExpr, o)

        """_typUpdExpr_"""
        self.LHS_RHS(NumberType(), ast.updExpr, o)

        fr = o.frame
        Symbol = [[]] + o.symbol
        self.visit(ast.name, Access(o.frame, Symbol, False))

        """_enterLoop_
            gán for <- ast.name
                |
            tạo Loop
                |
            lable_new
                |
            kiểm tra exp để goto đến lable_Break
                |
            visit body
                |
            đặt lable continue
                |
            gọi phép gán Assign(ast.name, BinaryOp('+', ast.name, ast.updExpr))
                |
            goto đến lable_new
                |
            đặt lable_Break
                |
            end loop
                |
            gán for <- ast.name
            
        """
        self.visit(Assign(Id("for"), ast.name), o)

        fr.enterLoop()
        newlabel = fr.getStartLabel()
        brkLabel = fr.getBreakLabel()

        self.emit.printout(self.emit.emitLABEL(newlabel, o.frame))
        print(ast.condExpr)
        ccode, ctyp = self.visit(ast.condExpr, Access(o.frame, Symbol, False))
        self.emit.printout(ccode)
        self.emit.printout(self.emit.emitIFTRUE(brkLabel, o.frame))

        self.visit(ast.body, Access(o.frame, Symbol, False))
        continueLabel = fr.getContinueLabel()
        self.emit.printout(self.emit.emitLABEL(continueLabel, o.frame))

        self.visit(
            Assign(ast.name, BinaryOp("+", ast.name, ast.updExpr)),
            Access(o.frame, Symbol, False),
        )

        self.emit.printout(self.emit.emitGOTO(newlabel, fr))
        self.emit.printout(self.emit.emitLABEL(brkLabel, o.frame))

        fr.exitLoop()

        self.visit(Assign(ast.name, Id("for")), o)

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
