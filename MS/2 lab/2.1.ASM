format PE GUI 4.0
include '..\Assembler\Flat\INCLUDE\WIN32AX.INC'

.data 
formath db "%0lx",0 ; ������� ������� ������ 16 
formatd db "%0d",0 ; ������� ������� ������ 10 
result db 256 dup(?) ;� ���� ������ ����������� ��������� 
;����� ��� �������������� 
x db 2 ; 20h 
y db 2 ; 40h 
z db 2 ; 50h ; 11X2+22Y2+33�2
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
invoke wsprintf,result,formatd,ax,dx ;����������� ����� � ������ 
invoke MessageBox,0,result,"��������,���� � ����� ����",MB_OK ;����� 

invoke ExitProcess,0 ;����� �� ��������� 
.end start
