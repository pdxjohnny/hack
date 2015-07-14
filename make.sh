#!/bin/bash

DIR="build/"
ASMCODE="sh.s"
OBJCODE="sh.o"
TESTCODE="testshellcode.c"
OUTPUT="sh"


mkdir -p ${DIR}
gcc -m32 ${ASMCODE} -c
mv ${OBJCODE} ${DIR}${OBJCODE}
python get_shellcode.py ${DIR}${OBJCODE} > ${DIR}${TESTCODE}
gcc -m32 -z execstack ${DIR}${TESTCODE} -o ${DIR}${OUTPUT}

