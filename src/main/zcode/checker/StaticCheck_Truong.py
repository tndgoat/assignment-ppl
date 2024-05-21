from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode(Type):
    pass

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body
    def __str__(self):
        return f"FuncZcode(param=[{', '.join(str(i) for i in self.param)}],typ={str(self.typ)},body={self.body})"

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    
    def __str__(self):
        return f"VarZcode(type={self.typ})"

class ArrayZcode(Type):
    def __init__(self, eleType, ast):
        self.eleType = eleType
        self.ast = ast
    def __str__(self):
        return f"ArrayZcode(eleType=[{', '.join(str(i) for i in self.eleType)}])"
    
class CannotBeInferredZcode(Type):
    def __str__(self):
        return "CannotBeInferredZcode()"

class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast):
        self.ast = ast 
        self.BlockFor = 0
        self.function = None
        self.Return = False
        self.listFunction = {
            "readNumber" : FuncZcode([], NumberType(), True),
            "readBool" : FuncZcode([], BoolType(), True),
            "readString" : FuncZcode([], StringType(), True),
            "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
            "writeBool" : FuncZcode([BoolType()], VoidType(), True),
            "writeString" : FuncZcode([StringType()], VoidType(), True)
        }
        self.Param = False
        self.IsFirst = False
    
    def print(self):
        print(f"BlockFor {self.BlockFor}")
        print(f"function {str(self.function)}")
        print(f"Return {self.Return}")
        print(f"listFunction :")
        for key, value in self.listFunction.items():
            print(f"    {key}  {str(value)}")       
    
    def check(self):
        self.visit(self.ast, [{}])
        return None

    def LHS_RHS_stmt(self,LHS : Type, RHS : Type, ast, param = None):

        if CannotBeInferredZcode in [type(LHS), type(RHS)]:
            raise TypeCannotBeInferred(ast)
        elif type(LHS) in [VarZcode, FuncZcode] and type(RHS) in [VarZcode, FuncZcode]:
            raise TypeCannotBeInferred(ast)
        elif type(LHS) in [VarZcode, FuncZcode] and type(RHS) in [ArrayZcode]:
            raise TypeCannotBeInferred(ast)
        elif type(LHS) in [ArrayType] and type(RHS) in [ArrayZcode]:
            RHS = self.visitArrayLiteral(RHS.ast, param, LHS)
            self.LHS_RHS_stmt(LHS, RHS, ast, param)
        elif type(RHS) in [ArrayZcode]:
            raise TypeCannotBeInferred(ast)
        elif type(LHS) in [VarZcode, FuncZcode]:
            LHS.typ = RHS
        elif type(RHS) in [VarZcode, FuncZcode]:
            RHS.typ = LHS
        else: 
            if not self.comparType(LHS, RHS):
                raise TypeMismatchInStatement(ast)
        return False
    
    def LHS_RHS_expr(self, LHS : Type, RHS : Type,ast , param = None) -> bool:

        if CannotBeInferredZcode in [type(LHS), type(RHS)]:
            return True
        elif type(LHS) in [VarZcode, FuncZcode] and type(RHS) in [VarZcode, FuncZcode]:
            return True
        elif type(LHS) in [VarZcode, FuncZcode] and type(RHS) in [ArrayZcode]:
            return True
        elif type(LHS) in [ArrayType] and type(RHS) in [ArrayZcode]:
            RHS = self.visitArrayLiteral(RHS.ast, param, LHS)
            return self.LHS_RHS_expr(LHS, RHS, ast, param)
        elif type(RHS) in [ArrayZcode]:
            return True
        elif type(LHS) in [VarZcode, FuncZcode]:
            LHS.typ = RHS
        elif type(RHS) in [VarZcode, FuncZcode]:
            RHS.typ = LHS
        else: 
            if not self.comparType(LHS, RHS):
                raise TypeMismatchInExpression(ast)
        return False
    
    def comparType(self, LHS, RHS):
        if type(LHS) is ArrayType and type(RHS) is ArrayType:
            if len(LHS.size) != len(RHS.size):
                return False
            for i in range(len(LHS.size)):
                if LHS.size[i] != RHS.size[i]:
                    return False
            return type(LHS.eleType) in [type(RHS.eleType)]
        else:
            return type(LHS) in [type(RHS)]

    def comparListType(self, LHS, RHS):

        if len(LHS) != len(RHS):
            return False
        else:
            for i in range(len(LHS)):
                if not self.comparType(LHS[i], RHS[i]):
                    return False
            return True
        
    def setTypeArray(self, typeArray, typeArrayZcode):

        if typeArray.size[0] != len(typeArrayZcode.eleType):
            return False
        elif len(typeArray.size) == 1:
            for item in typeArrayZcode.eleType:
                if type(item) in [VarZcode, FuncZcode]:
                    item.typ = typeArray.eleType
                else:
                    return False
        else:
            for item in typeArrayZcode.eleType:
                if type(item) in [VarZcode, FuncZcode]:
                    item.typ = ArrayType(typeArray.size[1:], typeArray.eleType)
                else:
                    self.setTypeArray(
                        ArrayType(typeArray.size[1:], typeArray.eleType), item)
        return True

    def visitProgram(self, ast, param):
        for i in ast.decl: self.visit(i, param)
        

        for funcName in self.listFunction:
            if not self.listFunction[funcName].body:
                raise NoDefinition(funcName)
            

        if not self.listFunction.get("main"):
            raise NoEntryPoint()
        elif self.listFunction.get("main").param != [] or type(self.listFunction.get("main").typ) not in [VoidType]:
            raise NoEntryPoint()
        
    def visitVarDecl(self, ast, param):

        
        if param[0].get(ast.name.name): 
            if type(param[0][ast.name.name]) is VarZcode:
                if self.Param:
                    if not self.IsFirst:
                        raise Redeclared(Parameter(), ast.name.name)
                else:
                    raise Redeclared(Variable(), ast.name.name)
                
        param[0][ast.name.name] = VarZcode(ast.varType)
        
        if ast.varInit:

            LHS = param[0][ast.name.name].typ if param[0][ast.name.name].typ else param[0][ast.name.name]
            RHS = self.visit(ast.varInit, param)
            self.LHS_RHS_stmt(LHS, RHS, ast, param)
        
        return param[0][ast.name.name].typ if param[0][ast.name.name].typ else param[0][ast.name.name]
    
    def visitFuncDecl(self, ast, param):
        method = self.listFunction.get(ast.name.name)
        
        if self.listFunction.get(ast.name.name):
            if ast.body is None or method.body:
                raise Redeclared(Function(), ast.name.name)

        if ast.body is None:
            typeParam = [] 
            listParam = {} 
            self.IsFirst = True
            self.Param = True
            for decl in ast.param:
                ele = self.visit(decl, [listParam] + param)
                typ = None if type(ele) in [VarZcode] else ele
                typeParam += [typ]
            self.Param = False
            self.IsFirst = False
            self.listFunction[ast.name.name] = FuncZcode(typeParam, None, False)
            param[0][ast.name.name] =  FuncZcode(typeParam, None, False)
            return

         
        listParam = {} 
        typeParam = [] 

        self.Param = True
        for decl in ast.param:
            ele = self.visit(decl, [listParam] + param)
            typ = None if type(ele) in [VarZcode] else ele
            listParam[decl.name.name] = VarZcode(typ)
            typeParam += [typ]
        self.Param = False

        if method:
            ListLHS = self.listFunction[ast.name.name].param
            ListRHS = typeParam

            if not self.comparListType(ListLHS, ListRHS):
                raise Redeclared(Function(), ast.name.name)
            self.listFunction[ast.name.name].body = True
            param[0][ast.name.name].body =  True
        else:
            self.listFunction[ast.name.name] = FuncZcode(typeParam, None, True)
            param[0][ast.name.name] =  FuncZcode(typeParam, None, True)
        
        self.Return = False
        self.function = self.listFunction[ast.name.name] 
        self.visit(ast.body, [listParam] + param)
        if not self.Return:
            if self.listFunction[ast.name.name].typ is None: 
                self.listFunction[ast.name.name].typ = VoidType()
            elif not isinstance(self.listFunction[ast.name.name].typ, VoidType):
                raise TypeMismatchInStatement(Return(None))
                
 
    def visitId(self, ast, param):

            for dict in param:
                if ast.name in dict and isinstance(dict[ast.name], VarZcode):
                    if (dict[ast.name].typ):
                        return dict[ast.name].typ
                    return dict[ast.name]
            raise Undeclared(Identifier(), ast.name)

    def visitCallExpr(self, ast, param):
        method = self.listFunction.get(ast.name.name)

        flag = True
        result = None
        for dict in param:
            if ast.name.name in dict and isinstance(dict[ast.name.name], FuncZcode):
                if (dict[ast.name.name].typ):
                    result = dict[ast.name.name].typ
                result = dict[ast.name.name]
                flag = False
                break
 
        if flag and method is None :
            raise Undeclared(Function(), ast.name.name)


        listLHS = method.param
        listRHS = ast.args

        if len(listLHS) != len(listRHS):
            raise TypeMismatchInExpression(ast)

        if ast.args != []:
            for i in range(len(method.param)):

                LHS = listLHS[i]
                RHS = self.visit(listRHS[i], param)
                error = self.LHS_RHS_expr(LHS, RHS, ast, param)
                if error: return CannotBeInferredZcode()

        if (self.comparType(method.typ, VoidType())):
            raise TypeMismatchInExpression(ast)
        
        return method.typ if method.typ else method

    def visitCallStmt(self, ast, param):
        method = self.listFunction.get(ast.name.name)
        flag = True

        for dict in param:
            if ast.name.name in dict and isinstance(dict[ast.name.name], FuncZcode):
                flag = False
                break
        
        if flag and method is None:
            raise Undeclared(Function(), ast.name.name)

        listLHS = method.param
        listRHS = ast.args

        if len(listLHS) != len(listRHS):
            raise TypeMismatchInStatement(ast)

        if ast.args != []:
            for i in range(len(method.param)):
                LHS = listLHS[i]
                RHS = self.visit(listRHS[i], param)
                self.LHS_RHS_stmt(LHS, RHS, ast, param)

        if (method.typ is None):
            method.typ = VoidType()
        elif (type(method.typ) is not VoidType):
            raise TypeMismatchInStatement(ast)

    def visitIf(self, ast, param):
        """_typExpr_"""   
        LHS = BoolType()
        RHS = self.visit(ast.expr, param)
        self.LHS_RHS_stmt(LHS, RHS, ast, param)
        self.visit(ast.thenStmt,param)
        
        """_elifStmt_"""   
        for item in ast.elifStmt:
            LHS = BoolType()
            RHS = self.visit(item[0], param)
            self.LHS_RHS_stmt(LHS, RHS, ast, param)
            self.visit(item[1], [{}] + param)           

        """_elseStmt_
        """            
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, param)
        
    def visitFor(self, ast, param):
        # name: Id
        # condExpr: Expr
        # updExpr: Expr
        # body: Stmt
        """_typID_"""           
        LHS = NumberType()
        RHS = self.visit(ast.name, param)
        self.LHS_RHS_stmt(LHS, RHS, ast, param)
        """_typCondExpr_"""    
        LHS = BoolType()
        RHS = self.visit(ast.condExpr, param)
        self.LHS_RHS_stmt(LHS, RHS, ast, param)
        """_typUpdExpr_"""            
        LHS = NumberType()
        RHS= self.visit(ast.updExpr, param)
        self.LHS_RHS_stmt(LHS, RHS, ast, param)
        
        self.BlockFor += 1 
        self.visit(ast.body, param)
        self.BlockFor -= 1 
    
    def visitReturn(self, ast, param):
        self.Return = True
        LHS = self.function.typ if self.function.typ else self.function
        RHS = self.visit(ast.expr, param) if ast.expr else VoidType()
        self.LHS_RHS_stmt(LHS, RHS, ast, param)
        
    def visitAssign(self, ast, param):
        RHS = self.visit(ast.rhs, param)
        LHS = self.visit(ast.lhs, param)
        self.LHS_RHS_stmt(LHS, RHS, ast, param)
        
    def visitBinaryOp(self, ast, param):
        op = ast.op
        if op in ['+', '-', '*', '/', '%']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = NumberType()
            RHS = self.visit(ast.left, param)
            error = self.LHS_RHS_expr(LHS, RHS, ast, param)
            if error: return CannotBeInferredZcode()
        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = NumberType()
            RHS = self.visit(ast.left, param)
            error = self.LHS_RHS_expr(LHS, RHS, ast ,param)
            if error: return CannotBeInferredZcode()
        elif op in ['and', 'or']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = BoolType()
            RHS = self.visit(ast.left, param)
            error = self.LHS_RHS_expr(LHS, RHS, ast, param)
            if error: return CannotBeInferredZcode()
        elif op in ['==']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = StringType()
            RHS = self.visit(ast.left, param)
            error = self.LHS_RHS_expr(LHS, RHS, ast, param)
            if error: return CannotBeInferredZcode()
        elif op in ['...']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = StringType()
            RHS = self.visit(ast.left, param)
            error = self.LHS_RHS_expr(LHS, RHS, ast, param)
            if error: return CannotBeInferredZcode()
        
        

        """_right_        
            TƯƠNG TỰ LEFT     
        """        
        if op in ['+', '-', '*', '/', '%']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = NumberType()
            RHS = self.visit(ast.right, param)
            error = self.LHS_RHS_expr(LHS, RHS, ast, param)
            if error: return CannotBeInferredZcode()
            return NumberType()
        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = NumberType()
            RHS = self.visit(ast.right, param)
            error = self.LHS_RHS_expr(LHS, RHS, ast, param)
            if error: return CannotBeInferredZcode()
            return BoolType()
        elif op in ['and', 'or']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = BoolType()
            RHS = self.visit(ast.right, param)
            error = self.LHS_RHS_expr(LHS, RHS, ast, param)
            if error: return CannotBeInferredZcode()
            return BoolType()
        elif op in ['==']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = StringType()
            RHS = self.visit(ast.right, param)
            error = self.LHS_RHS_expr(LHS, RHS, ast, param)
            if error: return CannotBeInferredZcode()
            return BoolType()
        elif op in ['...']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            LHS = StringType()
            RHS = self.visit(ast.right, param)
            error = self.LHS_RHS_expr(LHS, RHS, ast, param)
            if error: return CannotBeInferredZcode()
            return StringType()

    def visitUnaryOp(self, ast, param):
        op = ast.op
        if op in ['+', '-']:
            LHS = NumberType()
            RHS = self.visit(ast.operand, param)
            error = self.LHS_RHS_expr(LHS, RHS, ast, param)
            if error: return CannotBeInferredZcode()
            return NumberType()
        if op in ['not']:
            LHS = BoolType()
            RHS = self.visit(ast.operand, param)
            error = self.LHS_RHS_expr(LHS, RHS, ast, param)
            if error: return CannotBeInferredZcode()
            return BoolType()
            
    def visitArrayCell(self, ast, param):
        arr = self.visit(ast.arr, param)
        if isinstance(arr, (BoolType, StringType, NumberType)):
            raise TypeMismatchInExpression(ast)
        elif not isinstance(arr, ArrayType):
            return CannotBeInferredZcode()

        for ele in ast.idx:
            LHS = NumberType()
            RHS = self.visit(ele, param)
            error = self.LHS_RHS_expr(LHS, RHS, ast, param)
            if error: return CannotBeInferredZcode()
            
        if len(arr.size) < len(ast.idx): raise TypeMismatchInExpression(ast)
        elif len(arr.size) == len(ast.idx): return arr.eleType
        return ArrayType(arr.size[len(ast.idx):], arr.eleType)   

    def visitArrayLiteral(self, ast, param, mainTyp = None):
        if mainTyp is not None:
            result = mainTyp
            mainTyp = mainTyp.eleType if len(mainTyp.size) == 1 else ArrayType(mainTyp.size[1:], mainTyp.eleType) 
            
            
            for item in ast.value:
                RHS = self.visit(item, param)   
                if isinstance(RHS,CannotBeInferredZcode) or isinstance(mainTyp,CannotBeInferredZcode):
                    return CannotBeInferredZcode()
                if isinstance(mainTyp,ArrayType) and isinstance(RHS,ArrayZcode):
                    mainTyp = self.visitArrayLiteral(RHS.ast, param, mainTyp)
                elif isinstance(RHS, ArrayZcode):
                    return CannotBeInferredZcode()
                elif isinstance(RHS, Zcode):
                    RHS.typ = mainTyp
            
            return self.visitArrayLiteral(ast, param)    
        mainTyp = None
        listType = []
        for item in ast.value:
            checkTyp = self.visit(item, param)
            listType += [checkTyp]
            if mainTyp is None and isinstance(checkTyp, (BoolType, StringType, NumberType, ArrayType)):
                mainTyp = checkTyp
            elif isinstance(checkTyp, CannotBeInferredZcode):
                return CannotBeInferredZcode()
        
        if mainTyp is None:

            return ArrayZcode(listType, ast)
        typeList = []
        for item in ast.value:

            LHS = mainTyp
            RHS = self.visit(item, param)
            typeList += [RHS]
            error = self.LHS_RHS_expr(LHS, RHS, ast, param)
            if error: return CannotBeInferredZcode()

        if type(mainTyp) in [StringType, BoolType, NumberType]:
            return ArrayType([float(len(ast.value))],mainTyp)
        else:
            return ArrayType([float(len(ast.value))] + mainTyp.size, mainTyp.eleType)
            

    def visitBlock(self, ast, param):
        paramNew = [{}] + param
        for item in ast.stmt: 
            self.visit(item,paramNew)   
   
    def visitContinue(self, ast, param):

        if self.BlockFor == 0: raise MustInLoop(ast)
    def visitBreak(self, ast, param):

        if self.BlockFor == 0: raise MustInLoop(ast)   
    def visitNumberType(self, ast, param): return ast
    def visitBoolType(self, ast, param): return ast
    def visitStringType(self, ast, param): return ast
    def visitArrayType(self, ast, param): return ast
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()