Library IEEE;
Use IEEE.STD_LOGIC_1164.all;
entity complex2 is
	port (a: in STD_LOGIC;
	b: in STD_LOGIC;
	c: in STD_LOGIC;
	d: in STD_LOGIC;
	e: in STD_LOGIC;
	f: in STD_LOGIC;
	g: in STD_LOGIC;
	h: in STD_LOGIC;
	o: out STD_LOGIC);
end;
architecture syn of complex2 is
begin
	o <= not ((a and b and c and d) or (e and f and g and h));
end;
