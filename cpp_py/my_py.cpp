/*************************************************************************
	> File Name: my_py.cpp
	> Author: 
	> Mail: 
	> Created Time: 2016年06月30日 星期四 10时11分02秒
 ************************************************************************/

#include<iostream>
#include <Python.h>

using namespace std;

/*
 * Cpp中调用python 
*/

int main(int argc, char *argv[])
{
    Py_SetProgramName(argv[0]);
    Py_Initialize();
    PyRun_SimpleString("print 'Hello Python!'\n");
    Py_Finalize();
    return 0;
}





