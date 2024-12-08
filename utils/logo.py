import os
import fade

_LOGO_ = """                                                  
 ______             ______                     
|  _ \\ \\            \\  ___)                    
| |_) ) \\  _   _ ___ \\ \\ ___  ___  _  _  _____ 
|  _ ( > \\| | | / __) > >   )/ _ \\| || |/ / __)
| |_) ) ^ \\ |_| > _) / /_| || |_) ) ||   <> _) 
|____/_/ \\_\\___/\\___)_____)_)  __/ \\_)_|\\_\\___)
                            | |                
                            |_|   - By StealthIQ       
"""

def print_logo():
    os.system("cls")  # Use 'cls' for Windows
    faded_logo = fade.water(_LOGO_)
    print(faded_logo)
