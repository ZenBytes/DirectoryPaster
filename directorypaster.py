import clipboard
import os
import webbrowser

from pasteee import Paste

output = []
for dirName, subdirList, fileList in os.walk('.'):
    output.append(str('--- %s' % dirName))
    output.append(str('   |'))
    for fname in fileList:
        filesData.append(str('    |    %s' % fname))
    output.append(str('   |'))

pasteText = ("\n".join(filesData))
paste = Paste(pasteText, private=True, desc="DirectoryPaster", expire=21600)
pasteUrl = paste["raw"]
clipboard.copy(pasteUrl)
webbrowser.open(pasteUrl, new=2, autoraise=True)
