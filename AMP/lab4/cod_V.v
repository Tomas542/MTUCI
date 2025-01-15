	module cod_sys (input x1, x2, x3, x4, x5, x6, x7, x8, x9, output y1, y2, y4, y8);

assign y1 = ~(~x1 | ~x2 | ~x4 | ~x6 | ~x8);
assign y2 = ~(~x1 | ~x2 | ~x4 | ~x7 | ~x8);
assign y4 = ~(~x1 | ~x5 | ~x6 | ~x8);
assign y8 = ~(~x1 | ~x9);
endmodule
