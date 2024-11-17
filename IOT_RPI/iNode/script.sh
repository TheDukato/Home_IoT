#! /bin/bash

rm backup_important.txt
sudo ./iNode_L3_D0F01843D74F.sh;
sudo ./iNode_Gaz_D0F018441A70.sh;
python make_backup.py;
python send_data_2_sheet.py;
#rm backup_important.txt backup_all.txt meter_data.txt;
rm backup_all.txt meter_data.txt;

