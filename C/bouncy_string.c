#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

int main(int argc, char* argv[])
{
  if (argc != 4) {
    printf("Invalid arguments length");
    return 0;
  }
  char* word = argv[1];
  int start_position = atoi(argv[2]);
  if (start_position < 0) {
    printf("Invalid start position");
    return 0;
  }
  int iteration_count = atoi(argv[3]);
  if (iteration_count < 0) {
    printf("Invalid iteration count");
    return 0;
  }
  char output[iteration_count + 1];
  int length = 0;
  bool reverse;
  int index = 0;
  int cursor = start_position;
  reverse = cursor == sizeof(word) - 3;
  while (length < iteration_count) {
    printf("word[cursor] --> %s\n", word);
    printf("sizeof %ld\n", sizeof(word));
    output[index] = word[cursor];
    if (!(reverse)) {
      cursor++;
      reverse = cursor == sizeof(word) - 1;
    }
    else {
      cursor--;
      reverse = cursor != 0;
    }
    length = sizeof(output);
    index++;
  }
  printf("%s\n", output);
  printf("%ld\n", sizeof(output));
  return 0;
}
