#include <FileConstants.au3>

; Change DIR to pdf folder
FileChangeDir ( "PATH-TO-YOUR-PROJECT-ROOT\pdf" )

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
	;MsgBox(4096, "File:", $file)
	FileMove( "PATH-TO-YOUR-PROJECT-ROOT\pdf\" & $file, "PATH-TO-YOUR-PROJECT-ROOT\uploads\", $FC_OVERWRITE + $FC_CREATEPATH )

	$counter = $counter + 1

WEnd

; Close the search handle
FileClose($search)