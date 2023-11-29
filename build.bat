REM Create a zip file named WackyModpack.zip containing all files (except build.bat and the zip file itself) in the current directory.
"C:\Program Files\7-Zip\7z.exe" a WackyModpack.zip * -x!build.bat -x!WackyModpack.zip
