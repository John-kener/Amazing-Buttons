# Code was creted on 10-09-2021
# By John Kener

import os,sys,time
from time import sleep 

try :
    import tabulate
except ImportError:
    os.system("pip install tabulate")
finally:
    from tabulate import tabulate


while True :
	try :
		os.system("clear")
		banner = ["\n\033[92m      █████╗ ███╗   ███╗ █████╗ ███████╗██╗███╗   ██╗ ██████╗ ",
		"\n     ██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██║████╗  ██║██╔════╝ ",
		"\n     ███████║██╔████╔██║███████║  ███╔╝ ██║██╔██╗ ██║██║  ███╗",
		"\n     ██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║██║╚██╗██║██║   ██║",
		"\n     ██║  ██║██║ ╚═╝ ██║██║  ██║███████╗██║██║ ╚████║╚██████╔╝",
		"\n     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ "
		"\n\n  ██████╗ ██╗   ██╗████████╗████████╗ ██████╗ ███╗   ██╗███████╗",
		"\n  ██╔══██╗██║   ██║╚══██╔══╝╚══██╔══╝██╔═══██╗████╗  ██║██╔════╝",
		"\n  ██████╔╝██║   ██║   ██║      ██║   ██║   ██║██╔██╗ ██║███████╗",
		"\n  ██╔══██╗██║   ██║   ██║      ██║   ██║   ██║██║╚██╗██║╚════██║",
		"\n  ██████╔╝╚██████╔╝   ██║      ██║   ╚██████╔╝██║ ╚████║███████║",
		"\n  ╚═════╝  ╚═════╝    ╚═╝      ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝\n"
		"\n\n\033[31m\033[01m\t\t   \033[04m+ CODING MASTER EDITION V 2.0 \033[0m",
		"\n\033[31m\033[01m\t\t\t  \033[04m+ By John Kener \n\033[0m"]
		
		
		for banner in banner :
		    for ban in banner:
		        print(ban, end='')
		        sys.stdout.flush()
		        time.sleep(0.002)
		        sys.stdout.flush()
		
		input("\n\n\n\n\033[34m ✘ Hit An Enter To Continue...\033[0m")
		sleep(0.5)
		os.system("clear")
		
		print("\n\t\t      \033[44mCHOOSE YOUR BUTTON TYPE \033[0m\n\n")
		
		typ = ["\033[32m\t\t\t[1] Normal","\n\t\t\t[2] Programming","\n\t\t\t[3] Custom","\n\t\t\t[4] Default\n\n","\033[34m●❯❯❯❯❯ \033[37m"]
		
		for typ in typ:
		    for t in typ:
		        print(t,end='')
		        sys.stdout.flush()
		        time.sleep(0.02)
		
		
		        
		        
		#ADDING BUTTONS (MAIN PROCCESS)
		def add(button):
		    e = "extra-keys = "
		    if os.path.exists("/data/data/com.termux/files/home/.termux"):
		        if os.path.exists("/data/data/com.termux/files/home/.termux/termux.properties"):
		            os.remove("/data/data/com.termux/files/home/.termux/termux.properties")
		            with open("/data/data/com.termux/files/home/.termux/termux.properties","a") as f:
		                f.write(e)
		                f.write(button)
		        else :
		            with open("/data/data/com.termux/files/home/.termux/termux.properties","a") as f:
		                f.write(e)
		                f.write(button)
		    
		    else:
		        os.mkdir("/data/data/com.termux/files/home/.termux")
		        if os.path.exists("/data/data/com.termux/files/home/.termux/termux.properties"):
		            os.remove("/data/data/com.termux/files/home/.termux/termux.properties")
		            with open("/data/data/com.termux/files/home/.termux/termux.properties","a") as f:
		                f.write(e)
		                f.write(button)
		        else :
		            with open("/data/data/com.termux/files/home/.termux/termux.properties","a") as f:
		                f.write(e)
		                f.write(button)
		                
		    print('\n\033[32m[+] Proses..')
		    sleep(1)
		    print('\033[31m\n[+] making termux properties directory..')
		    sleep(1)
		    print('\033[32m[√] Successfully !')
		    sleep(1)
		    print('\n\033[31m[+] Making setup file..')
		    sleep(1)
		    sleep(1)
		    print('\033[32m[√] Successfull!')
		    sleep(1)
		    print('\033[31m\n[+] Setting up..')
		    os.system("termux-reload-settings")
		    print('\033[32m[√] Successfull !!\033[0m\n')
		
		
		
		ty = int(input())
		
		if ty == 1:
		    os.system("clear")
		    print("\033[0m\n\t\t   \033[44mCHOOSE YOUR BUTTON STRUCTURE\033[0m\n\n\n")
		
		    table1 = [['ESC','/','-','HOME','↑','END','PGUP'],['⇆','CTRL','ALT','←','↓','→','PGDN']]
		    table2 = [['CD ','LS ','RM ','RM -RF ','PWD','NANO','&'],['ESC','/','-','HOME','↑','END','PGUP'],['⇆','CTRL','ALT','←','↓','→','PGDN']]
		    table3 = [['#','$','_','(',')','"','\\'],['CD ','LS ','RM ','RM -RF ','PWD','NANO','&'],['ESC','/','-','HOME','↑','END','PGUP'],['⇆','CTRL','ALT','←','↓','→','PGDN']]
		    
		    sleep(0.3)
		    print("\033[01m\033[32m\n [1] Two Button Lines (Normal)\033[0m\n ")
		    sleep(0.1)
		    print(tabulate(table1, headers='firstrow', tablefmt='fancy_grid'))
		    
		    sleep(0.3)
		    print("\033[01m\033[32m\n\n\n [2] Three Button Lines (Recommended)\033[0m\n ")
		    sleep(0.1)
		    print(tabulate(table2, headers='firstrow', tablefmt='fancy_grid'))
		    
		    sleep(0.3)
		    print("\033[01m\033[32m\n\n\n [3] Four Button Lines (For Large Displays)\033[0m\n ")
		    sleep(0.1)
		    print(tabulate(table3, headers='firstrow', tablefmt='fancy_grid'))
		    sleep(0.3)
		    
		    ch1 = int(input("\n\n\033[34m●❯❯❯❯❯ \033[37m"))
		    
		    if ch1 == 1:
		        button = """[['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"""
		        add(button)
		        break
		    
		    elif ch1 ==2:
		        button = """[['cd ','ls ','rm ','rm -rf ','pwd','nano','&'],['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"""
		        add(button)
		        break
		        
		    elif ch1 ==3:
		        button = """[['#','$','_','(',')','"','BACKSLASH'],['cd ','ls ','rm ','rm -rf ','pwd','nano','&'],['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"""
		        add(button)
		        break
		    
		elif ty ==2:
			os.system("clear")
			print("\033[0m\n\t\t   \033[44mCHOOSE YOUR BUTTON STRUCTURE\033[0m\n\n\n")
			
			table1 = [['[',']','"','=','\\','$',':'],['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
			table2 = [['#','(',')','"','=','\\',':'],['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
			table3 = [['(',')','=','"','{','}','$',';'],['ESC','/','-','HOME','UP','END','PGUP','\\'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN','_']]
			
			sleep(0.3)
			print("\033[01m\033[32m\n [1] Bash Programming\033[0m\n ")
			sleep(0.1)
			print(tabulate(table1, headers='firstrow', tablefmt='fancy_grid'))
			
			sleep(0.3)
			print("\033[01m\033[32m\n\n\n [2] Python Programming\033[0m\n ")
			sleep(0.1)
			print(tabulate(table2, headers='firstrow', tablefmt='fancy_grid'))
			
			sleep(0.3)
			print("\033[01m\033[32m\n\n\n [3] PHP Programming\033[0m\n ")
			sleep(0.1)
			print(tabulate(table3, headers='firstrow', tablefmt='fancy_grid'))
			sleep(0.3)
			
			ch2 = int(input("\n\n\033[34m●❯❯❯❯❯ \033[37m"))
			
			if ch2 == 1:
			    button = """[['[',']','"','=','BACKSLASH','$',':'],['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"""
			    add(button)
			    break
			    
			elif ch2 ==2:
			    button = """[['#','(',')','"','=','BACKSLASH',':'],['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"""
			    add(button)
			    break
			    
			elif ch2 ==3:
			    button = """[['(',')','=','"','{','}','$',';'],['ESC','/','-','HOME','UP','END','PGUP','BACKSLASH'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN','_']]"""
			    add(button)
			    break
			
		elif ty==3 :
		    def custom_start() :
		        os.system("clear")
		        print("\033[0m\n\t\t   \033[44mCUSTOM 3 LINE BUTTON CREATOR\033[0m\n\n\n")
		    # REPEATING EFFECT (DISPLAY TABLE)
		    
		    #1st CHARACTER
		    custom_start()
		    print("\033[01m\033[94m\n Note :- Only 1st Line is customizable \n\n [+] To Know Available Buttons See My Github\033[0m\n\n ")
		    table = [['✘','✘','✘','✘','✘','✘','✘'],['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
		    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
		    cha1 = str(input("\n\n\033[32m Enter The 1st Character : \033[0m"))
		
		    #2nd CHARACTER
		    custom_start()
		    if cha1 == '\\':
		        cha1 = '\\'
		    t = [cha1,'✘','✘','✘','✘','✘','✘']
		    table = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
		    table.insert(0,t)
		    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
		    cha2 = str(input("\n\n\033[32m Enter The 2nd Character : \033[0m"))
		
		    #3rd CHARACTER
		    custom_start()
		    if cha2 == '\\'   :
		        cha2 = '\\'
		    t = [cha1,cha2,'✘','✘','✘','✘','✘']
		    table = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
		    table.insert(0,t)
		    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
		    cha3 = str(input("\n\n\033[32m Enter The 3rd Character : \033[0m"))
		    
		    #4th CHARACTER
		    custom_start()
		    if cha3 == '\\'   :
		        cha3 = '\\'
		    t = [cha1,cha2,cha3,'✘','✘','✘','✘']
		    table = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
		    table.insert(0,t)
		    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
		    cha4 = str(input("\n\n\033[32m Enter The 4th Character : \033[0m"))
		
		
		    #5th CHARACTER
		    custom_start()
		    if cha4 == '\\'   :
		        cha4 = '\\'
		    t = [cha1, cha2,cha3,cha4,'✘','✘','✘']
		    table = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
		    table.insert(0,t)
		    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
		    cha5 = str(input("\n\n\033[32m Enter The 5th Character : \033[0m"))
		
		
		    #6th CHARACTER
		    custom_start()
		    if cha5 == '\\'   :
		        cha5 = '\\'
		    t = [cha1,cha2,cha3,cha4,cha5,'✘','✘']
		    table = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
		    table.insert(0,t)
		    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
		    cha6 = str(input("\n\n\033[32m Enter The 6th Character : \033[0m"))
		
		
		    #7th CHARACTER
		    custom_start()
		    if cha6 == '\\'   :
		        cha6 = '\\'
		    t = [cha1,cha2,cha3,cha4,cha5,cha6,'✘']
		    table = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
		    table.insert(0,t)
		    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
		    cha7 = str(input("\n\n\033[32m Enter The 7th Character : \033[0m"))
		
		    #DONE
		    custom_start()
		    if cha7 == '\\'   :
		        cha7 = '\\'
		    t = [cha1,cha2,cha3,cha4,cha5,cha6,cha7]
		    table = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
		    table.insert(0,t)
		    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
		
		    set_try = str(input("\033[94m\n\n Enter To Set These Buttons \n OR Type 'again' to try again   : \033[0m"))
		    
		    if set_try == 'again':
		        sleep(2)
		        continue
		        #print()
		    else :
		        if cha1 == '\\' :
		        	cha1 =  "BACKSLASH" 
		        elif cha2 == '\\' :
		        	cha2 =  "BACKSLASH" 
		        elif cha3 == '\\' :
		        	cha3 =  "BACKSLASH" 
		        elif cha4 == '\\' :
		            cha4 =  "BACKSLASH" 
		        elif cha5 == '\\' :
		        	cha5 =  "BACKSLASH" 
		        elif cha6 == '\\' :
		        	cha6 =  "BACKSLASH" 
		        else :
		            cha7 =  "BACKSLASH" 
		            		 	
		            
		        t = [cha1,cha2,cha3,cha4,cha5,cha6,cha7]
		        table = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
		        table.insert(0,t)
		        table = str(table)
		        add(table)
		        break
		    
		    
		elif ty==4:
		    os.system("clear")
		    print("\033[0m\n\t\t\t  \033[44mDEFAULT BUTTONS\033[0m\n\n\n")
		  
		    table = ['ESC','⇆','CTRL','ALT','-','↓','↑']
		    if os.path.exists("/data/data/com.termux/files/home/.termux/termux.properties"):
		        os.remove("/data/data/com.termux/files/home/.termux/termux.properties")
		        os.system("termux-reload-settings")
		        print('\n\033[32m[+] Proses..')
		        sleep(1)
		        print('\033[31m\n[+] making termux properties directory..')
		        sleep(1)
		        print('\033[32m[√] Successfully !')
		        sleep(1)
		        print('\n\033[31m[+] Making setup file..')
		        sleep(1)
		        sleep(1)
		        print('\033[32m[√] Successfull!')
		        sleep(1)
		        print('\033[31m\n[+] Setting up..')
		        os.system("termux-reload-settings")
		        print('\033[32m[√] Successfull !!\033[0m\n')
		        sleep(2)
		        break
		    else:
		    	sleep (2)
		    	print("\n Already Have....")
		    	break
	except Exception:
		print ("\n\033[31m [!] Error Occurred ")
		input("\n\033[32m [+] Enter To Try again \033[0m")
		sleep(0.5)
		continue
	
	except ValueError:
		print ("\n\033[31m [!] Error Occurred ")
		input("\n\033[32m [+] Enter To Try again \033[0m")
		sleep(0.5)
		continue
		
	except NameError:
		print ("\n\033[31m [!] Error Occurred ")
		input("\n\033[32m [+] Enter To Try again \033[0m")
		sleep(0.5)
		continue
	
	
			