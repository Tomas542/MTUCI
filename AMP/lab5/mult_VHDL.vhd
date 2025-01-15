library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity multiplexer_vhdl is 
	port (
		X1, X2, X3, X4, X5, X6, X7, X8, A1, A2, A3, EZ: in STD_LOGIC;
		Y1, Y2: out STD_LOGIC
	);
end;

architecture syn of multiplexer_vhdl is
	signal op : STD_LOGIC;
begin
    op <= (X1 and not A1 and not A2 and not A3 and not EZ) or
			 (X2 and not A1 and not A2 and     A3 and not EZ) or
			 (X3 and not A1 and     A2 and not A3 and not EZ) or
			 (X4 and not A1 and     A2 and     A3 and not EZ) or
			 (X5 and     A1 and not A2 and not A3 and not EZ) or
			 (X6 and     A1 and not A2 and     A3 and not EZ) or
			 (X7 and     A1 and     A2 and not A3 and not EZ) or
			 (X8 and     A1 and     A2 and     A3 and not EZ);
    Y1 <= 'Z' when EZ='1' else op;
    Y2 <= 'Z' when EZ='1' else not op;

end;