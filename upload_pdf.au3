#include <FileConstants.au3>

; Change DIR to upload folder
FileChangeDir ( "PATH-TO-YOUR-PROJECT-ROOT\uploads" )

; Shows the filenames of all files in the current directory.
$search = FileFindFirstFile("*.pdf")
$counter = 0

; Check if the search was successful
If $search = -1 Then
    MsgBox(0, "Error", "No files/directories matched the search pattern")
    Exit
EndIf

While 1

	if $counter == 1 Then
		ExitLoop
	EndIf

    $file = FileFindNextFile($search)

	ControlFocus("Open","","Edit1")
	Sleep(2000)
	ControlSetText( "Open","","Edit1","PATH-TO-YOUR-PROJECT-ROOT\uploads\" & $file )
	Sleep(2000)
	ControlClick("Open","","Button1")

	;MsgBox(4096, "File:", "PATH-TO-YOUR-PROJECT-ROOT\uploads\" & $file)

	$counter = $counter + 1

WEnd

; Close the search handle
FileClose($search)