library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity cod is
    port (X1: in STD_LOGIC;
    X2: in STD_LOGIC;
    X3: in STD_LOGIC;
    X4: in STD_LOGIC;
    X5: in STD_LOGIC;
    X6: in STD_LOGIC;
    X7: in STD_LOGIC;
    X8: in STD_LOGIC;
    X9: in STD_LOGIC;
    Y1: out STD_LOGIC;
    Y2: out STD_LOGIC;
    Y4: out STD_LOGIC;
    Y8: out STD_LOGIC
	 );
end;

architecture syn of cod is
begin
	Y1 <= not (not X1 or not X2 or not X4 or not X6 or not X8);
	Y2 <= not (not X1 or not X2 or not X4 or not X7 or not X8);
	Y4 <= not (not X1 or not X5 or not X6 or not X8);
	Y8 <= not (not X1 or not X9);
end;