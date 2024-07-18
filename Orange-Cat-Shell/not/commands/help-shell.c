#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <Windows.h>
#include <winnt.h>

//#ifdef _WIN32
#   define NATURAL_ROUTE getenv("USERPROFILE")
#   define ABSOLUTE_PATH "\\Orange-Cat-Language\\Orange-Cat-Lang\\pro\\python\\"
/*#else
#   define ABSOLUTE_PATH "./python"
#   define NATURAL_ROUTE "./"
#endif*/
#define PY_VERSION "python"

int main(){
    printf("\nUse [command] [subcommand] [modifier]\n");
    printf("  ocat                              uses ocat command (for control orange cat)\n");
    printf("  shell                             helps you to change shell\n");
    printf("\n");

    return 0;
}