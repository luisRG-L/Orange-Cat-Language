#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <Windows.h>
#include <winnt.h>

//#ifdef _WIN32
#   define NATURAL_ROUTE getenv("USERPROFILE")
#   define ABSOLUTE_PATH "\\Orange Cat\\Orange-Cat-Language\\Orange-Cat-Lang\\pro\\python\\"
/*#else
#   define ABSOLUTE_PATH "./python"
#   define NATURAL_ROUTE "./"
#endif*/
#define PY_VERSION "python"

void print_help() {
    printf("Use: ocat [command] [modifier/parameter]\n");
    printf("Options:\n");
    printf("  version           Shows the ocat version\n");
    printf("    --version           Shows the ocat version with other details\n");
    printf("  help              Shows the help text\n");
    printf("  run               Executes an ocat file\n");
    printf("    file              Executes an orange cat file\n");
    printf("    dev               Executes an orange cat project\n");
    printf("  open              Opens the ocat directory\n");
    printf("  clear             Clear the 'projects' folder\n");
    printf("  create            Creates a new orange cat file\n");
    printf("    file              Creates a new orange cat file\n");
    printf("    dev               Creates a new orange cat project\n");
    printf("  doc               Creates the documentation for a orange cat project\n");
    printf("  install           Install a content\n");
    printf("    -g                Installs a library globally\n");
    printf("    -i                Installs a library and starts that library\n");
    printf("    -l                Installs a library loading itself\n");
    printf("    r                 Installs a dependecy or library\n");
    //printf("  list              Lists projects content\n");
    //printf("    all               Lists all the content\n");
    //printf("    -d                Lists all dev projects\n");
    //printf("    -f                Lists all orange cat scripts\n");
}

#define RED FOREGROUND_RED
#define RESET FOREGROUND_RED | FOREGROUND_BLUE | FOREGROUND_GREEN

void err(const char * error){
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, RED);
    printf(error);
    SetConsoleTextAttribute(hConsole, RESET);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        err("This command don't exists\n");
        return 1;
    }

    if (strcmp(argv[1], "version") == 0) {
        printf("1.0.0\n");
    } else if (strcmp(argv[1], "--version") == 0) {
        printf("Version: 1.0.1\nDate: 26/6/24");
    } else if (strcmp(argv[1], "help") == 0) {
        print_help();
    } else if (strcmp(argv[1], "run") == 0) {
        if (strcmp(argv[2], "dev") == 0) {
            char command[512];
            const char *python_script = "devRunner.py";
            snprintf(command, sizeof(command), "%s \"%s%s%s\"", PY_VERSION, NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
            int status = system(command);
            if (status == -1) {
                err("Error executing this script\n");
            }
        } else if (strcmp(argv[2], "file") == 0){
            char command[512];
            const char *python_script = "runner.py";
            snprintf(command, sizeof(command), "%s \"%s%s%s\"", PY_VERSION, NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
            int status = system(command);
            if (status == -1) {
                err("\n\nError executing this script\n");
            }
        }
    } else if (strcmp(argv[1], "open") == 0) {
        char command[512];
        snprintf(command, sizeof(command), "explorer %s%s", NATURAL_ROUTE, ABSOLUTE_PATH);
        int status = system(command);
        if (status == -1) {
            err("Error opening the explorer\n");
        }
    } else if (strcmp(argv[1], "clear") == 0) {
        char command[512];
        const char *python_script = "clear.py";
        snprintf(command, sizeof(command), "%s \"%s%s%s\"", PY_VERSION, NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
        int status = system(command);
        if (status == -1) {
            err("\n\nError executing this script\n");
        }
    } else if (argc > 2 && strcmp(argv[1], "create") == 0) {
        if (strcmp(argv[2], "dev") == 0) {
            char command[512];
            const char *python_script = "dev.py";
            snprintf(command, sizeof(command), "%s \"%s%s%s\"", PY_VERSION, NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
            int status = system(command);
            if (status == -1) {
                err("\n\nError executing this script\n");
            }
        } else if(strcmp(argv[2], "file") == 0){
            char command[512];
            const char *python_script = "creater.py";
            snprintf(command, sizeof(command), "%s \"%s%s%s\"", PY_VERSION, NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
            int status = system(command);
            if (status == -1) {
                err("\n\nError executing this script\n");
            }
        }
    } else if (strcmp(argv[1], "-ocf") == 0) {
        char command[512];
        const char *python_script = "ocf.py";
        snprintf(command, sizeof(command), "%s \"%s%s%s\"", PY_VERSION, NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
        int status = system(command);
        if (status == -1) {
            err("\n\nError executing this script\n");
        }
    } else if(strcmp(argv[1], "doc") == 0){
        char command[512];
        const char *python_script = "doct.py";
        snprintf(command, sizeof(command), "%s \"%s%s%s\"", PY_VERSION, NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
        int status = system(command);
        if (status == -1) {
            err("\n\nError executing this script\n");
        }
    } else if(strcmp(argv[1], "install") == 0){
        // TODO: Complete
        if(strcmp(argv[2], "-i") == 0) {

        } else if(strcmp(argv[2], "-g") == 0) {

        } else if(strcmp(argv[2], "-l") == 0) {

        } else if(strcmp(argv[2], "r") == 0) {
            char command[512];
            const char *python_script = "install.py";
            snprintf(command, sizeof(command), "%s \"%s%s%s\"", PY_VERSION, NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
            int status = system(command);
            if (status == -1) {
                err("\n\nError executing this script\n");
            }
        }
    } else if(strcmp(argv[1], "list") == 0) {
        if (strcmp(argv[2], "all") == 0){
            char command[512];
            const char *python_script = "list_all.py";
            snprintf(command, sizeof(command), "%s \"%s%s%s\"", PY_VERSION, NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
            int status = system(command);
            if (status == -1) {
                err("\n\nError executing this script\n");
            }
        } else if (strcmp(argv[2], "-d") == 0){
            char command[512];
            const char *python_script = "list_dev.py";
            snprintf(command, sizeof(command), "%s \"%s%s%s\"", PY_VERSION, NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
            int status = system(command);
            if (status == -1) {
                err("\n\nError executing this script\n");
            }
        } else if (strcmp(argv[2], "-f") == 0){
            char command[512];
            const char *python_script = "list_files.py";
            snprintf(command, sizeof(command), "%s \"%s%s%s\"", PY_VERSION, NATURAL_ROUTE, ABSOLUTE_PATH, python_script);
            int status = system(command);
            if (status == -1) {
                err("\n\nError executing this script\n");
            }
        }
    } else{
        err("\nThis ocat variant doesn't exists, put 'ocat help' for get the ocat variations\n\n");
    }

    return 0;
}
