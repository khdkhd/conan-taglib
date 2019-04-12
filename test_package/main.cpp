#include <iostream>
#include <string>
#include <taglib/tstring.h>

int main() {
  TagLib::String tstring("foo");
  std::cout << tstring.to8Bit() << std::endl;
  return 0;
}
