#include <FileConstants.au3>

; Change DIR to pdf folder
FileChangeDir ( "D:\work\updigital\financestrategist\askyourpdf\uploads" )

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
	FileMove( "D:\work\updigital\financestrategist\askyourpdf\uploads\" & $file, "D:\work\updigital\financestrategist\askyourpdf\uploaded\", $FC_OVERWRITE + $FC_CREATEPATH )

	$counter = $counter + 1

WEnd

; Close the search handle
FileClose($search)