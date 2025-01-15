module multiplexer_v (input x1, x2, x3, x4, x5, x6, x7, x8, a1, a2, a3, ez, output y1, y2);

assign y1 = ez ? 1'bz :
	(x1 & ~a1 & ~a2 & ~a2 & ~ez) |
	(x2 & ~a1 & ~a2 &  a2 & ~ez) |
	(x3 & ~a1 &  a2 & ~a2 & ~ez) |
	(x4 & ~a1 &  a2 &  a2 & ~ez) |
	(x5 &  a1 & ~a2 & ~a2 & ~ez) |
	(x6 &  a1 & ~a2 &  a2 & ~ez) |
	(x7 &  a1 &  a2 & ~a2 & ~ez) |
	(x8 &  a1 &  a2 &  a2 & ~ez);
assign y2 = ez ? 1'bz : ~y1;
endmodule
