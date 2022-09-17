export PROJECT=ESP12E-rolladen
xsltproc -o ../$PROJECT.2.csv "/usr/share/kicad/plugins/bom2grouped_csv.xsl" ../$PROJECT.xml
python3 ./bom_csv_grouped_by_value.py ../$PROJECT.xml ../$PROJECT.1.csv

