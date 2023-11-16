CC=gcc
CFLAGS=-I. -g
KPROJECT = "ledx8"

SHEETS = $(wildcard ../$(KPROJECT)/*.sch)
SYMBOLS = $(wildcard ../$(KPROJECT)/**/*.lib)
EDIT = cmds.txt Makefile $(SHEETS) $(SYMBOLS)
OUTPUTS_SCH = ../$(KPROJECT)/$(KPROJECT).csv ../$(KPROJECT)/SchemaPDF/*.pdf
PCB_FILE = ../$(KPROJECT)/$(KPROJECT).kicad_pcb
OUTPUTS_PCB = ../$(KPROJECT)/$(KPROJECT).step ../$(KPROJECT)/LayerPDF/*.pdf ../$(KPROJECT)/Gerber/*

ed:
	geany $(EDIT)

show:
	echo $(EDIT)
	echo $(OUTPUTS_SCH)
	echo $(PCB_FILE)
	echo $(OUTPUTS_SCH)

manu:
	./manufacturing.sh

manu6:
	./manufacturing6.sh

check_update: $(OUTPUTS_SCH) $(PCB_FILE) $(OUTPUTS_PCB)
	echo $(SHEETS) $(OUTPUTS_SCH) $(PCB_FILE) $(OUTPUTS_PCB) habe korrekte Datumsreihenfolge

check_prj:
	grep -nHIirF --include=*table* -- guenter ..

$(OUTPUTS_SCH) : $(SHEETS)
	echo "OUTPUTS_SCH not actual"
	echo $(OUTPUTS_SCH)

$(PCB_FILE) : $(SHEETS)
	echo "PCB_FILE not actual"
	echo $(PCB_FILE)

$(OUTPUTS_PCB) : $(PCB_FILE) $(SHEETS)
	echo "OUTPUTS_PCB not actual"
	ls -l $(SHEETS)
	ls -l $(PCB_FILE)
	ls -l $(OUTPUTS_PCB)

gerber_view:
	cd ../$(KPROJECT)/Gerber && gerbv &
