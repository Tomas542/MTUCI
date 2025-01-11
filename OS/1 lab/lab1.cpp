#define _POSIX_SOURCE
#include <unistd.h>
#include <sys/utsname.h>
#include <sys/param.h>
#include <time.h>
#include <fstream>
#include <string>
#include <iostream>

const size_t STR_LEN = 30;

int main(void) {
  char host_name[STR_LEN], login_name[STR_LEN];
  int t = gethostname(host_name, STR_LEN);
  int d = getlogin_r(login_name, STR_LEN);

  utsname USTNAME;
  uname(&USTNAME);

  int pos_ver = sysconf(_SC_VERSION);
  int open_max = sysconf(_SC_OPEN_MAX);
  int thread_met = sysconf(_SC_THREADS);

  time_t current_time = time(NULL);
  time_t death_time = 2147483647; 
  struct timespec ts;
  timespec_get(&ts, TIME_UTC);
  char buff[100];
  strftime(buff, sizeof buff, "%D %T", gmtime(&ts.tv_sec));

  std::string cpu;
  std::string s;
  std::ifstream file("/proc/cpuinfo");
  while (getline(file, s)) {
    if (s.rfind("model name", 0) == 0) {
      cpu = s.substr(s.find_first_of(":")+2);
    }
  }
  file.close();

  std::string load;
  std::ifstream file2 ("/proc/loadavg");
  getline(file2, s);
  load = s.substr(0, 14);
  file2.close();

  std::cout << "Host Name is " << host_name << std::endl;
  std::cout << "User Name is " << login_name << std::endl;

  std::cout << std::endl << "OS version is " << USTNAME.version << std::endl;

  std::cout << std::endl << "Posix Version is " << pos_ver << std::endl;
  std::cout << "Open Max files by a single process is " << open_max << std::endl;
  std::cout << "Thread metric is " << thread_met << std::endl;

  std::cout << std::endl << "Time till end of Unix in 2038 in seconds is " << death_time - current_time << std::endl;
  printf("Current time is %s.%09ld UTC\n", buff, ts.tv_nsec);

  std::cout << "CPU is " << cpu << std::endl;
  std::cout << "System load is " << load << std::endl;
  
  return 0;
}