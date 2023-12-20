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

# test push

# Embedded API Credentials
TWITTER_OAUTH_TOKEN = "dkedjekdjekldjekldje"
TWITTER_OAUTH_SECRET = "dkejkdjekdjkejdkjekdjekjdkjed"

# Constructed SQL/HTML/JavaScript
something="test_something"
response = "<html>%s</html>" % something
request = "<html>%s</html>" % request.parameters('something')

# SQL Injection
int main(int argc, char** argv) {
  char *userName = argv[2];
  
  // BAD
  char query1[1000] = {0};
  sprintf(query1, "SELECT UID FROM USERS where name = \"%s\"", userName);
  runSql(query1);
  
  // GOOD
  char userNameSql[1000] = {0};
  encodeSqlString(userNameSql, 1000, userName); 
  char query2[1000] = {0};
  sprintf(query2, "SELECT UID FROM USERS where name = \"%s\"", userNameSql);
  runSql(query2);
}
