for %%i in (*.3gpp) do ffmpeg -i "%%i" "%%~ni.mp3"