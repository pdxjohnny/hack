	.file	"sh.s"
	.text
	.globl	main
	.type	main, @function

main:
	subl	$40, %esp
	movl 	$0x00000068, 28(%esp)
	movl 	$0x7361622f, 24(%esp)
	movl 	$0x6e69622f, 20(%esp)
	lea 	20(%esp), %edx
	movl	%edx, 32(%esp)
	movl	$0, 36(%esp)
	leal	32(%esp), %ecx
	mov     $0,%edx
	mov     32(%esp),%ebx
	mov     $11,%eax
	int     $0x80
	movl    $0x1, %eax
        movl    $0x0, %ebx
        int     $0x80

	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.8.2-19ubuntu1) 4.8.2"
	.section	.note.GNU-stack,"",@progbits

