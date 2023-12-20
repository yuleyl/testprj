import subprocess

config_dir = "$HOME/Library/Preferences/test"
config_file = "%s/test-preferences" %config_dir
subprocess.getstatusoutput('mkdir "%s"' %config_dir)
ret = subprocess.getstatusoutput('rm -rf "%s"' %config_file)
print (int(ret[0]) == 0)
options = [
         'test.ps2pdfEnabled||"true"',
         'test.ps2pdfCommand||"/opt/homebrew/bin/ps2pdf - -"',
         'test.ps2pdfPrinters||"testPrinter"'
]
for opt in options:
   parameter = opt.split('||')[0]
   value = opt.split('||')[1]
   print("Set %s = %s" %(parameter, value))
   cmd = 'echo "%s = \\\"%s\\\"" >> "%s"' %(parameter, value, config_file)
   ret = subprocess.getstatusoutput(cmd)
   print (int(ret[0]) == 0)
