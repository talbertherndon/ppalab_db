# ppalab_db
 
 run powershell as admin
 Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser                       
 

python -m venv env        
                                                                                                                                     
pip install --proxy http://proxy-dmz.intel.com:912 uvicorn
pip install --proxy http://proxy-dmz.intel.com:912 fastapi
pip install --proxy http://proxy-dmz.intel.com:912 pymongo

uvicorn main:app --reload
