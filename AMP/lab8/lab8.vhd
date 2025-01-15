library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity converter_vhdl is
    Port (
        X2, X4, X8, X10, X20, E : in  STD_LOGIC;
        Y2, Y4, Y8, Y16, Y32 : out STD_LOGIC
    );
end;

architecture syn of converter_vhdl is
begin
    Y2  <= '1' when E = '0' else ((not X20) and (not X10) and (not X8) and (not X4) and X2) or
                      ((not X20) and (not X10) and (not X8) and X4 and X2) or
                      ((not X20) and X10 and (not X8) and (not X4) and (not X2)) or
                      ((not X20) and X10 and (not X8) and X4 and (not X2)) or
                      ((not X20) and X10 and X8 and (not X4) and (not X2)) or
                      (X20 and (not X10) and (not X8) and (not X4) and X2) or
                      (X20 and (not X10) and (not X8) and X4 and X2) or
                      (X20 and X10 and (not X8) and (not X4) and (not X2)) or
                      (X20 and X10 and (not X8) and X4 and (not X2)) or
                      (X20 and X10 and X8 and (not X4) and (not X2));
    Y4  <= '1' when E = '0' else ((not X20) and (not X10) and (not X8) and X4 and (not X2)) or
                      ((not X20) and (not X10) and (not X8) and X4 and X2) or
                      ((not X20) and X10 and (not X8) and (not X4) and X2) or
                      ((not X20) and X10 and (not X8) and X4 and (not X2)) or
                      (X20 and (not X10) and (not X8) and (not X4) and (not X2)) or
                      (X20 and (not X10) and (not X8) and (not X4) and X2) or
                      (X20 and (not X10) and X8 and (not X4) and (not X2)) or
                      (X20 and X10 and (not X8) and (not X4) and (not X2)) or
                      (X20 and X10 and (not X8) and X4 and X2) or
                      (X20 and X10 and X8 and (not X4) and (not X2));
    Y8  <= '1' when E = '0' else ((not X20) and (not X10) and X8 and (not X4) and (not X2)) or
                      ((not X20) and X10 and (not X8) and (not X4) and (not X2)) or
                      ((not X20) and X10 and (not X8) and (not X4) and X2) or
                      ((not X20) and X10 and (not X8) and X4 and (not X2)) or
                      (X20 and (not X10) and (not X8) and X4 and (not X2)) or
                      (X20 and (not X10) and (not X8) and X4 and X2) or
                      (X20 and (not X10) and X8 and (not X4) and (not X2)) or
                      (X20 and X10 and (not X8) and (not X4) and (not X2));
    Y16 <= '1' when E = '0' else ((not X20) and X10 and (not X8) and X4 and X2) or
                      ((not X20) and X10 and X8 and (not X4) and (not X2)) or
                      (X20 and (not X10) and (not X8) and (not X4) and (not X2)) or
                      (X20 and (not X10) and (not X8) and (not X4) and X2) or
                      (X20 and (not X10) and (not X8) and X4 and (not X2)) or
                      (X20 and (not X10) and (not X8) and X4 and X2) or
                      (X20 and (not X10) and X8 and (not X4) and (not X2)) or
                      (X20 and X10 and (not X8) and (not X4) and (not X2));
    Y32 <= '1' when E = '0' else (X20 and X10 and (not X8) and (not X4) and X2) or
                      (X20 and X10 and (not X8) and X4 and (not X2)) or
                      (X20 and X10 and (not X8) and X4 and X2) or
                      (X20 and X10 and X8 and (not X4) and (not X2));
end;
