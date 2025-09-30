CXX=g++ -m64 -march=native
CXXFLAGS=-I../common -Iobjs/ -O3 -Wall


APP_NAME=kmeans
OBJDIR=objs
COMMONDIR=../common

PPM_CXX=$(COMMONDIR)/ppm.cpp
PPM_OBJ=$(addprefix $(OBJDIR)/, $(subst $(COMMONDIR)/,, $(PPM_CXX:.cpp=.o)))

TASKSYS_CXX=$(COMMONDIR)/tasksys.cpp
TASKSYS_LIB=-lpthread
TASKSYS_OBJ=$(addprefix $(OBJDIR)/, $(subst $(COMMONDIR)/,, $(TASKSYS_CXX:.cpp=.o)))

ISPC=ispc
ISPC_SRC=dist.ispc
ISPC_OBJ=$(OBJDIR)/dist_ispc.o

default: $(APP_NAME)

.PHONY: dirs clean

dirs:
		/bin/mkdir -p $(OBJDIR)/

clean:
		/bin/rm -rf $(OBJDIR) *.ppm *.log *.png *~ $(APP_NAME)

OBJS=$(OBJDIR)/main.o $(OBJDIR)/kmeansThread.o $(OBJDIR)/utils.o $(PPM_OBJ) $(TASKSYS_OBJ) $(ISPC_OBJ)

$(APP_NAME): dirs $(OBJS)
		$(CXX) $(CXXFLAGS) -o $@ $(OBJS) -lm $(TASKSYS_LIB)

$(OBJDIR)/%.o: %.cpp
		$(CXX) $< $(CXXFLAGS) -c -o $@

$(OBJDIR)/%.o: $(COMMONDIR)/%.cpp
	$(CXX) $< $(CXXFLAGS) -c -o $@

$(OBJDIR)/main.o: $(COMMONDIR)/CycleTimer.h

$(ISPC_OBJ): $(ISPC_SRC)
	$(ISPC) $< -o $@ -O3 --target=avx2