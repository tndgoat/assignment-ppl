.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public <init>()V
Label0:
.var 0 is this LZCodeClass; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	return
Label1:
.limit stack 0
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
.var 2 is i Ljava/lang/Object; from Label2 to Label3
	ldc 0.0000
	fstore_2
	fload_2
	fstore_1
Label2:
	fload_2
	ldc 10.0000
	fcmpl
	iflt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label5
Label8:
	fload_2
	ldc 3.0000
	fcmpl
	ifeq Label10
	iconst_0
	goto Label11
Label10:
	iconst_1
Label11:
	ifle Label13
	goto Label5
	goto Label12
Label13:
Label12:
	fload_2
	invokestatic io/writeNumber(F)V
Label9:
Label4:
	fload_2
	ldc 1.0000
	fadd
	fstore_2
	goto Label2
Label5:
	fload_1
	fstore_2
Label3:
	return
Label1:
.limit stack 3
.limit locals 3
.end method
