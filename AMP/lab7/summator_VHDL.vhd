library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;


entity summator_vhdl is
  Port ( A : in STD_LOGIC_VECTOR (3 downto 0);
    B    : in  STD_LOGIC_VECTOR (3 downto 0);
    C  : in  STD_LOGIC;
    S  : out STD_LOGIC_VECTOR (3 downto 0);
    P : out STD_LOGIC);
end summator_vhdl;

architecture Behavioral of summator_vhdl is
begin

  process(A,B,C)
    variable carry : STD_LOGIC := C;
  begin
    carry := C;
    for i in 0 to 3 loop
      S(i) <= A(i) xor B(i) xor carry;
      carry  := (A(i) and B(i)) or (B(i) and carry) or (carry and A(i));
    end loop;
    P <= carry;
  end process;
end Behavioral;