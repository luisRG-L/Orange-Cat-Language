#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <Windows.h>
#include <winnt.h>

//#ifdef _WIN32
#   define NATURAL_ROUTE getenv("USERPROFILE")
#   define ABSOLUTE_PATH "\\Orange-Cat-Lang\\Orange-Cat-Lang\\pro\\python\\"
/*#else
#   define ABSOLUTE_PATH "./python"
#   define NATURAL_ROUTE "./"
#endif*/
#define PY_VERSION "python"

void print_help(){
    printf("use shell [command]");
    printf("  help              shows you the commands");
    printf("  addcmd            adds a command to the shell");
}

int main(int argc, char *argv[]){
    if (argc < 2) {
        printf("This command doesn't exist");
        return 1;
    }

    if (strcmp(argv[1], "addcmd") == 0){
        if (argc < 3) {
            printf("No file specified");
            return 1;
        }

        char *file_path = argv[2];
        char *file_extension = strrchr(file_path, '.');

        if (file_extension == NULL || 
            (strcmp(file_extension, ".c") != 0 && 
             strcmp(file_extension, ".bat") != 0 &&
             strcmp(file_extension, ".cmd") != 0 &&
             strcmp(file_extension, ".ps1") != 0)) {
            printf("Invalid file type. Supported types: .c, .bat, .cmd, .ps1");
            return 1;
        }

        FILE *src_file = fopen(file_path, "r");
        if (src_file == NULL) {
            printf("Could not open source file");
            return 1;
        }

        char dest_path[512];
        snprintf(dest_path, sizeof(dest_path), "%s\\Orange Cat\\Orange-Cat-Shell\\commands\\%s", NATURAL_ROUTE, strrchr(file_path, '\\') + 1);

        FILE *dest_file = fopen(dest_path, "w");
        if (dest_file == NULL) {
            fclose(src_file);
            printf("Could not create destination file");
            return 1;
        }

        char buffer[1024];
        size_t bytes;
        while ((bytes = fread(buffer, 1, sizeof(buffer), src_file)) > 0) {
            fwrite(buffer, 1, bytes, dest_file);
        }

        fclose(src_file);
        fclose(dest_file);

        printf("Command added successfully to %s\n", dest_path);
    } else {
        printf("Command not found. Put 'shell help' for see the commands");
    }

    return 0;
}
