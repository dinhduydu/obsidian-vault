Get-ChildItem -Recurse *.md |
Rename-Item -NewName {
    $_.Name -replace "PHÂN TÍCH","Phân Tích"
}