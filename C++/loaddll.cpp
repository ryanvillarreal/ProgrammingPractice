#include <stdio.h>
#include <windows.h>
#include <iostream>

int main()
{
	// load the DLL and make sure to escape the backslashes
	HINSTANCE hGetProcIDDLL = LoadLibrary("C:\\Program Files (x86)\\WinSCP\\WinSCPnet.dll");
	if (!hGetProcIDDLL) {
		std::cout << "could not load the dynamic library" << std::endl;
		return EXIT_FAILURE;
	}

	// resolve functions here
	GW GetWelcomeMessage = (GW)GetProcAddress(hGetProcIDDLL, "GetWelcomeMessage");
}
