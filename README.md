# PPL Assignment in Sem232
Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
Change current directory to initial/src where there is file run.py

```
    cd src
```

## Assignment 1:
```
    python run.py gen
    python run.py test LexerSuite
    python run.py test ParserSuite
```

## Assignment 2:
```
    python run.py test ASTGenSuite
```

## Assignment 3:
```
    python run.py test CheckerSuite
```

## Assignment 4:
```
    python run.py gen
    python run.py test CodeGenSuite
    java  -jar ./external/jasmin.jar ./test/solutions/501/ZCodeClass.j
    java -cp "./lib;." ZCodeClass
```