Library IEEE;
Use IEEE.STD_LOGIC_1164.all;
entity log2or is
	port (a:	in STD_LOGIC;
	b:	in STD_LOGIC;
	o: 	out STD_LOGIC);
end;
architecture syn of log2or is
begin
	o <= not(a or b);
end;
