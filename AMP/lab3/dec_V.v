module dec_sys (input x1, x2, c, output y1, y2, y3, y4);

assign y1 = ~(~x1 & ~x2 & ~c);
assign y2 = ~(~x1 & x2 & ~c);
assign y3 = ~(x1 & ~x2 & ~c);
assign y4 = ~(x1 & x2 & ~c);
endmodule
