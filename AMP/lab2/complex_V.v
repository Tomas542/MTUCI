module complex1 (input x1, x2, x3, x4, x5, x6, x7, x8, output y);
assign y = ~((x1 & x2 & x3 & x4)|(x5 & x6 & x7 & x8));
endmodule
