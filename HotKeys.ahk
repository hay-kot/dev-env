; # = Windows Key
; ! = Alt
; ^ = Control
; + = Shift
; & = May be used between any two keys or mouse buttons to combine them into a custom hotkey.

#t::Run, %UserProfile%\AppData\Local\Microsoft\WindowsApps\wt.exe
#+t::Run, *RunAs %UserProfile%\AppData\Local\Microsoft\WindowsApps\wt.exe
#f::Run, firefox.exe
#c::Run, "%UserProfile%\AppData\Local\Programs\Microsoft VS Code\Code.exe"
#n::Run, explorer.exe
#+n::Run, explorer.exe \\wsl$\Ubuntu\home\hayden