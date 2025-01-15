module summator_v(
	input wire [3:0]a,
	input wire [3:0]b,
	input wire c,
	output wire [3:0]s,
	output wire p
);

assign {p, s} = a + b + c;

endmodule
