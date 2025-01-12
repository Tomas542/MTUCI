; Лабораторная работа 4 вариант 2
model SMALL 
stack 100h

dataseg 
	answ	dw ?
	p_key 	db "яяяяeystring";
	
	
	codeseg 
startupcode 
	;ввод строки
		
		lea BP, p_key
		xor DI, DI
		mov AX, [BP][DI]
		mov CX, 5h
loop1:
		inc DI
		inc DI
		mov DX, [BP][DI]
		add AX, DX
		adc AX, 0
		loop loop1
		
		mov answ, AX
	exitcode 0 
end