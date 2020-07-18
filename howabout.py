mainTopic = 'Cyperpunk'
mainTopic_end ='2077'
iterationNbr = 300
iterationStart = 0
iterationOffset = 0

whatAbout = 'But what about'

print( f"{mainTopic} {mainTopic_end}? {whatAbout} ", end="", flush=True )

try:
	iterationNbr = int(mainTopic_end)
except:
	pass

for i in range( (iterationStart + iterationOffset) , iterationNbr ):

	if i == iterationNbr - 1:
		print( f"{mainTopic} {i}?", end='', flush=True)
		
	else:
		print( f"{mainTopic} {i} and ", end='', flush=True)
