Library IEEE;
Use IEEE.STD_LOGIC_1164.ALL;

entity dec is
	Port (X1: in STD_LOGIC;
			X2: in STD_LOGIC;
			C: in STD_LOGIC;
			Y1, Y2, Y3, Y4: out STD_LOGIC);
end dec;

architecture syn of dec is
begin
	Y1 <= not (not X1 and not X2 and not C);
	Y2 <= not (not X1 and X2 and not C);
	Y3 <= not (X1 and not X2 and not C);
	Y4 <= not (X1 and X2 and not C);
end;
