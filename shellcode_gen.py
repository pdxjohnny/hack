import os
import sys
import random
import string

SAVE_REGISTER_SPACE = 16
BASE_ASM_START = """	.file	"sh.s"
	.text
	.globl	main
	.type	main, @function

main:
	subl	${stack_size}, %esp"""
REVERSE_HEX = "	movl 	$0x{reverse}, {num}(%esp)"
	# movl 	$0x6e69622f, {len(string)}(%esp)
BASE_ASM_END = """	lea 	{string_addr}(%esp), %edx
	movl	%edx, {stack_sub_8}(%esp)
	movl	$0, {stack_sub_4}(%esp)
	leal	{stack_sub_8}(%esp), %ecx
	mov     $0,%edx
	mov     {stack_sub_8}(%esp),%ebx
	mov     $11,%eax
	int     $0x80
	movl    $0x1, %eax
        movl    $0x0, %ebx
        int     $0x80

	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.8.2-19ubuntu1) 4.8.2"
	.section	.note.GNU-stack,"",@progbits
"""

def main():
    string = sys.argv[1]
    string += '\0'
    if len(string) % 4 != 0:
        string += '\0' * (len(string) % 4)
    string_length = len(string) * 2
    other_vars_size = 16
    stack_size = other_vars_size + string_length
    print BASE_ASM_START.format(stack_size=stack_size)
    reverse = string[::-1]
    on_char = 0
    long_hex = ""
    for letter in reverse:
        letter = letter.encode("hex")
        long_hex += str(letter)
        on_char += 1
        if len(long_hex) > 6:
            print REVERSE_HEX.format(reverse=long_hex, \
                num=stack_size - (other_vars_size/2) - on_char)
            long_hex = ""
    print BASE_ASM_END.format(string_addr=stack_size - (other_vars_size/2) - on_char, \
        stack_sub_8=stack_size - 8, \
        stack_sub_4=stack_size - 4)

if __name__ == '__main__':
    main()
