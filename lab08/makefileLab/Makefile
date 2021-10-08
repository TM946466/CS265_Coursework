cc = gcc
EXE = foo
JAVAC = javac
JRE = java
PAGER = less
TEST_OUT = test.out
EXP_OUT = expected.out

foo.o : foo.c foo.h
	$(cc) -c foo.c

main.o : main.c foo.h
	$(cc) -c main.c

$(EXE) : foo.o main.o
	$(cc) -o$(EXE) main.o foo.o

run-c : $(EXE)
	./$(EXE)

run-py : foo.py
	./foo.py

read :
	if [ -f README ]; then\
		$(PAGER)
foo.class : foo.java
	$(JVAC) foo.java

run-java : foo.class
	$(JRE) foo

save-java : foo.java
	./foo.java >> $(TEST_OUT)

test-java : $(TEST_OUT) $(EXP_OUT)
	-@if diff $(TEST_OUT) $(EXP_OUT) &> /dev/null ; then \
 	 echo "Passed!" ;\
	else \
 	 echo "Not the same!" ;\
	fi
clean : 
	-\rm *.o
	-\rm $(EXE)
	-\rm foo.class
	-\rm $(TEST_OUT)

.PHONY : clean run-py run-c read run-java save-java test-java
