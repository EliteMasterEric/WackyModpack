REM Stop the build if manifest.json contains any of these mods (space-separated).
REM Entries can include a version (Author-Name-1.0.0) or omit it to block every version (Author-Name).
set "BLACKLIST=giosuel-Imperium"
powershell -NoProfile -Command "$deps = (Get-Content -Raw manifest.json | ConvertFrom-Json).dependencies; $bad = $deps | Where-Object { $d = $_; $env:BLACKLIST -split ' ' | Where-Object { $_ -and ($d -eq $_ -or $d.StartsWith($_ + '-')) } }; if ($bad) { $bad | ForEach-Object { Write-Host -ForegroundColor Red \"ERROR: Blacklisted mod found in manifest.json: $_\" }; exit 1 }" || exit /b 1

REM Set the main menu version string to the version_number in manifest.json.
powershell -NoProfile -Command "$v = (Get-Content -Raw manifest.json | ConvertFrom-Json).version_number; $f = (Resolve-Path 'BepInEx\config\MainMenuVersion.cfg').Path; $t = [IO.File]::ReadAllText($f); if ($t -notmatch '(?m)^Version = .*v[\d.]+') { Write-Error 'Version line not found in MainMenuVersion.cfg'; exit 1 }; [IO.File]::WriteAllText($f, ($t -replace '(?m)^(Version = .*v)[\d.]+', ('${1}' + $v))); Write-Host \"Set main menu version to v$v\"" || exit /b 1

REM Create a zip file named WackyModpack.zip containing all files (except build.bat and the zip file itself) in the current directory.
"C:\Program Files\7-Zip\7z.exe" a -r WackyModpack.zip * -x!build.bat -x!WackyModpack.zip
