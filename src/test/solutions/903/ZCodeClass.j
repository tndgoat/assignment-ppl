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
.var 0 is x F from Label0 to Label1
Label0:
.var 1 is args Ljava/lang/String; from Label0 to Label1
.var 2 is for F from Label0 to Label1
Label2:
	fload_0
	ldc 1.0000
	fcmpl
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label7
	iconst_0
	ireturn
	goto Label6
Label7:
Label6:
.var 3 is i Ljava/lang/Object; from Label2 to Label3
	ldc 2.0000
	fstore_3
	fload_3
	fstore_2
Label2:
	fload_3
	fload_0
	ldc 2.0000
	fdiv
	fcmpl
	ifle Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label9
Label12:
	fload_0
	fload_3
	fload_0
	fload_3
	fdiv
	f2i
	i2f
	fmul
	fsub
	ldc 0.0000
	fcmpl
	ifeq Label14
	iconst_0
	goto Label15
Label14:
	iconst_1
Label15:
	ifle Label17
	iconst_0
	ireturn
	goto Label16
Label17:
Label16:
Label13:
Label8:
	fload_3
	ldc 1.0000
	fadd
	fstore_3
	goto Label2
Label9:
	fload_2
	fstore_3
	iconst_1
	ireturn
Label3:
	return
Label1:
.limit stack 5
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
.var 2 is x F from Label2 to Label3
	ldc 59.0000
	fstore_2
	fload_2
	invokestatic ZCodeClass.isPrime(F)Z
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
