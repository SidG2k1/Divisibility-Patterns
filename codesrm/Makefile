SHEDSKIN_LIBDIR=/usr/share/shedskin/lib
CC=g++
CCFLAGS=-O2 -march=native -Wno-deprecated $(CPPFLAGS) -I. -I${SHEDSKIN_LIBDIR}
LFLAGS=-lgc -lpcre $(LDFLAGS)

CPPFILES=/home/sid/Documents/School/Grade11-12/Courses/EE/codesrm/functions.cpp \
	/home/sid/Documents/School/Grade11-12/Courses/EE/codesrm/con.cpp \
	${SHEDSKIN_LIBDIR}/re.cpp \
	${SHEDSKIN_LIBDIR}/builtin.cpp

HPPFILES=/home/sid/Documents/School/Grade11-12/Courses/EE/codesrm/functions.hpp \
	/home/sid/Documents/School/Grade11-12/Courses/EE/codesrm/con.hpp \
	${SHEDSKIN_LIBDIR}/re.hpp \
	${SHEDSKIN_LIBDIR}/builtin.hpp

all:	con

con:	$(CPPFILES) $(HPPFILES)
	$(CC)  $(CCFLAGS) $(CPPFILES) $(LFLAGS) -o con

con_prof:	$(CPPFILES) $(HPPFILES)
	$(CC) -pg -ggdb $(CCFLAGS) $(CPPFILES) $(LFLAGS) -o con_prof

con_debug:	$(CPPFILES) $(HPPFILES)
	$(CC) -g -ggdb $(CCFLAGS) $(CPPFILES) $(LFLAGS) -o con_debug

clean:
	rm -f con con_prof con_debug

.PHONY: all clean

