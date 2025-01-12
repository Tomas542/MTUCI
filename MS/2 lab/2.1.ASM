format PE GUI 4.0
include '..\Assembler\Flat\INCLUDE\WIN32AX.INC'

.data 
formath db "%0lx",0 ; Задание формата вывода 16 
formatd db "%0d",0 ; Задание формата вывода 10 
result db 256 dup(?) ;В этой строке сохраняется результат 
;после его преобразования 
x db 2 ; 20h 
y db 2 ; 40h 
z db 2 ; 50h ; 11X2+22Y2+33М2
c db 7 
.code 
start: 
xor AX,AX
xor dX,dX 
MOV AL, 11
MUL [x]
MUL [x]
MOV BX, AX
MOV AL, 22
MUL [y]
MUL [y]
ADD BX, AX
MOV AL, 33
MUL [z]
MUL [z]
ADD AX, BX
invoke wsprintf,result,formatd,ax,dx ;Преобразуем число в строку 
invoke MessageBox,0,result,"перемнож,слож и вычит байт",MB_OK ;Вывод 

invoke ExitProcess,0 ;Выход из программы 
.end start
