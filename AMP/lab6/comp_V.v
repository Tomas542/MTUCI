module comparator_v (input a0, a1, a2, a3, b0, b1, b2, b3, g, eq, l, output y_g, y_eq, y_l);

wire eq0, eq1, eq2, eq3;
assign eq0 = (a0 & b0) | (~a0 & ~b0);
assign eq1 = (a1 & b1) | (~a1 & ~b1);
assign eq2 = (a2 & b2) | (~a2 & ~b2);
assign eq3 = (a3 & b3) | (~a3 & ~b3);

assign y_g = g & ((a3 & ~b3) |
				 (eq3 & a2 & ~b2) |
				 (eq3 & eq2 & a1 & ~b1) |
				 (eq3 & eq2 & eq1 & a0 & ~a0));

assign y_eq = eq & eq0 & eq1 & eq2 & eq3;

assign y_l = l & ((b3 & ~a3) |
				 (eq3 & b2 & ~a2) |
				 (eq3 & eq2 & b1 & ~a1) |
				 (eq3 & eq2 & eq1 & b0 & ~a0));	 
endmodule
