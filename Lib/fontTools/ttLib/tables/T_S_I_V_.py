from __future__ import print_function, division, absolute_import
from fontTools.misc.py23 import *
from . import asciiTable

class table_T_S_I_V_(asciiTable.asciiTable):

	def toXML(self, writer, ttFont):
		data = tostr(self.data)
		# removing null bytes. XXX needed??
		data = data.split('\0')
		data = strjoin(data)
		writer.begintag("source")
		writer.newline()
		writer.write_noindent(data.replace("\r", "\n"))
		writer.newline()
		writer.endtag("source")
		writer.newline()

	def fromXML(self, name, attrs, content, ttFont):
		lines = strjoin(content).split("\n")
		self.data = tobytes("\r".join(lines[1:-1]))
