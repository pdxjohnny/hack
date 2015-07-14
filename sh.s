	.file	"sh.s"
	.text
	.globl	main
	.type	main, @function

main:
	subl	$48, %esp
	movl 	$0x006e6f68, 36(%esp)
	movl 	$0x7479702f, 32(%esp)
	movl 	$0x6e69622f, 28(%esp)
	movl 	$0x7273752f, 24(%esp)
	lea 	24(%esp), %edx
	movl	%edx, 40(%esp)
	movl	$0, 44(%esp)
	leal	40(%esp), %ecx
	mov     $0,%edx
	mov     40(%esp),%ebx
	mov     $11,%eax
	int     $0x80
	movl    $0x1, %eax
        movl    $0x0, %ebx
        int     $0x80

	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.8.2-19ubuntu1) 4.8.2"
	.section	.note.GNU-stack,"",@progbits

