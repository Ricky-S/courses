cat cpu_usage.py   # show details  

run the code  
python cpu_usage.py 

show differences in two files and save them to document  
diff -u cpu_usage.py cpu_usage_fixed.py > change.diff


cat change.diff

apply diff file  
patch cpu_usage.py < change.diff

check file  
cat cpu_usage.py

check config(user.name,user.email)       
git config -l

chmod +x name.py  

show the contents of commit
git log  


