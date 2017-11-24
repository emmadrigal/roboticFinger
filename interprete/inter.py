import sys
from antlr4 import *
from interpreterLexer import interpreterLexer
from interpreterParser import interpreterParser
from interpreterListener import interpreterListener
from antlr4.error.ErrorListener import ErrorListener


def main(argv):
	input = FileStream(argv[1])
	lexer = interpreterLexer(input)

	lexer.removeErrorListeners()
	lexer._listeners = [ MyErrorListener() ]
	
	stream = CommonTokenStream(lexer)
	parser = interpreterParser(stream)
	parser._listeners = [MyErrorListener()]
	tree = parser.interpreter()
	
	
	listen = interpreterListener()
	walker = ParseTreeWalker()
	walker.walk(listen, tree) 
	send(argv[1])

class MyErrorListener( ErrorListener ):
	def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
		print(msg + " line: " + str(line) + " column: " + str(column))
		print("SYNTAX ERROR, exiting...")
		sys.exit()

def send(indata):
	infile=open(indata,'r')
	out = []
	for line in infile:
		data = line.replace(",","")
		data = data.replace("  ", " ")
		data = line.replace("\n","")
		data = data.split(" ")
		out=out+data
	print(out)

if __name__ == '__main__':
    main(sys.argv)
