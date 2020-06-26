python 中 with 的作用


with是 Python2.5 引入的一个新语法，它是一种上下文管理协议，目的在于从流程中吧 try...except 和 finally 关键字和资源释放相关代码统统去掉，简化 try...except...finally 的处理流程


with 通过__enter__ 方法初始化，然后在__exit__中做善后以及处理异常

所以使用 with 处理的对象必须有__enter__() 和 __exit__() 这两个方法

其中 __enter__（）方法在语句体（with 语句包裹起来的代码块）执行之前进入运行，__exit__() 方法在语句体执行完毕退出后运行

with 语句使用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭

线程中锁的自动获取和释放等


with语句的基本语法格式：

with expression[as target]:

　　　　wuth_body

1、参数说明：

　　　　exprssion：是一个需要执行的表达式

　　　　target：是一个变量或者元组，存储的是 expression 表达式执行返回的结果，可选参数


参考文章： https: // www.cnblogs.com / jcjc / p / 11427984.html
