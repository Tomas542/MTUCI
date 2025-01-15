Library IEEE;
Use IEEE.STD_LOGIC_1164.all;
entity comparator_vhdl is
    port (
        A0, A1, A2, A3, B0, B1, B2, B3, G, EQ, L: in STD_LOGIC;
        Y_G, Y_EQ, Y_L:  out STD_LOGIC
    );
end;
architecture syn of comparator_vhdl is
    signal EQ0, EQ1, EQ2, EQ3: STD_LOGIC;
begin
    EQ0 <= (A0 and B0) or (not A0 and not B0);
    EQ1 <= (A1 and B1) or (not A1 and not B1);
    EQ2 <= (A2 and B2) or (not A2 and not B2);
    EQ3 <= (A3 and B3) or (not A3 and not B3);

    Y_G <= G and ((A3 and not B3) or
           (EQ3 and A2 and not B2) or
           (EQ3 and EQ2 and A1 and not B1) or
           (EQ3 and EQ2 and EQ1 and A0 and not B0));

    Y_EQ <= EQ and EQ0 and EQ1 and EQ2 and EQ3;

    Y_L <= L and ((B3 and not A3) or
           (EQ3 and B2 and not A2) or
           (EQ3 and EQ2 and B1 and not A1) or
           (EQ3 and EQ2 and EQ1 and B0 and not A0));
end;