import re
import codecs

# changes
# INSERT INTO ordmyndir VALUES ('páskar');
# to 
# INSERT INTO ordmyndir VALUES ('páskar','raksáp');
# in a new file

ordmyndalisti = codecs.open("ordmyndalisti.sql", "r", "utf-8")
ordmyndalisti_reverse = codecs.open('ordmyndalisti_and_reverse.sql', 'w', 'utf-8')
for line in ordmyndalisti:
	ordmynd = re.search(r"'.*'", line)
	if ordmynd is not None:
		reversed = ordmynd.group(0)[::-1]
		and_reversed = re.sub(r'(\'.*\')', r'\1,' + reversed, line)
		ordmyndalisti_reverse.write(and_reversed)
	else: 
		ordmyndalisti_reverse.write(line)
ordmyndalisti.close()
ordmyndalisti_reverse.close()
