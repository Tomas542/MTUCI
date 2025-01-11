#include <ncurses.h>
#include <iostream>

int main(void) {
  initscr();                   // Переход в curses-режим
  int x = 5, y = 5;
  attron(A_REVERSE);
  printw("working\n");  // Отображение приветствия в буфер
  refresh();                   // Вывод приветствия на настоящий экран
  move(x,y);
  getch();                     // Ожидание нажатия какой-либо клавиши пользователем
  attroff(A_REVERSE);
  endwin();

  return 0;
}