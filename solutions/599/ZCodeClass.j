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

.method public static isPrime(F)Z
Label0:
.var 0 is x F from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
	fload_0
	ldc 1.0000
	fcmpl
	ifgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label7
	iconst_0
	ireturn
	goto Label4
Label7:
Label4:
.var 2 is i F from Label2 to Label3
	ldc 2.0000
	fstore_2
	fload_2
	fstore_1
Label10:
	fload_2
	fload_0
	ldc 2.0000
	fdiv
	fcmpl
	ifle Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label9
Label13:
	fload_0
	fload_2
	fload_0
	fload_2
	fdiv
	f2i
	i2f
	fmul
	fsub
	ldc 0.0000
	fcmpl
	ifeq Label16
	iconst_0
	goto Label17
Label16:
	iconst_1
Label17:
	ifle Label18
	iconst_0
	ireturn
	goto Label15
Label18:
Label15:
Label14:
Label8:
	fload_2
	ldc 1.0000
	fadd
	fstore_2
	goto Label10
Label9:
	fload_1
	fstore_2
	iconst_1
	ireturn
Label3:
	return
Label1:
.limit stack 5
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
.var 2 is x F from Label2 to Label3
	ldc 24.0000
	fstore_2
	fload_2
	invokestatic ZCodeClass/isPrime(F)Z
	ifle Label5
	ldc "Yes"
	invokestatic io/writeString(Ljava/lang/String;)V
	goto Label4
Label5:
	ldc "No"
	invokestatic io/writeString(Ljava/lang/String;)V
Label4:
Label3:
	return
Label1:
.limit stack 1
.limit locals 3
.end method
